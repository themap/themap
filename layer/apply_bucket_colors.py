import json
import math
import requests
from ..common import filter_outliers

def apply_bucket_colors(layer, field, colors, token): 
    print('Appling Bucket colors by '+field+'...')
    style = {
        'colorType' : 'buckets',
        'legend' : {
            'showLegend' : True,
            'color' : {
                'type' : "buckets",
                'field' : field,
                'ranges' :[]
            }
        },
        'common' : {
            'common-color'  : {
                'type' : "categorical",
                'property' : "dynaID",
                'stops' : []
            },
            "common-image": "marker",
            "common-opacity": 0.7,
            "common-size": 0.5,
            "common-width": 3,
            "image-marker": None
        }
    }

    style['legend']['color']['ranges'] = generate_bucket_ranges(layer["ID"], field,colors, token)

    for r in style['legend']['color']['ranges']:
        for i in r["IDs"]:
            style['common']['common-color']['stops'].append([i,r['color']])
            
    layer["GLStyle"] = json.dumps(style)
    layer["HoverField"] = field
    layer["IsShowProperties"] = True
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/UpdateTourMapLayer', data = layer, headers = headers)
    return r.json()

def parse_number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0
    
def generate_bucket_ranges(layer_id, field,colors, token): 
    headers = {'authorization': 'Bearer '+token}
    payload = {
        "layerID" : layer_id,
        "property" : field
    }
    print("Loading "+field+" data...")
    r = requests.get('https://api.themap.net/api/Tour2/GetLayerPropertyValues',params=payload, headers = headers)
    data = r.json()
    sorted_data = newlist = filter_outliers(data, value_fn=lambda x: parse_number(x["Value"]),threshold=5)
    total = len(sorted_data)
    point1 = math.floor(total / 4) - 1
    point2 = math.floor(total / 2) - 1
    point3 = math.floor((total) * (3 / 4)) - 1
    ranges = []
    colors = colors or "#0000ff-#00ff00-#ffff00-#0000ff"
    color_set = colors.split("-")
    ranges.append({
                    'start': float(sorted_data[0]["Value"] or 0),
                    'stop': float(sorted_data[point1]["Value"] or 0),
                    'color': color_set[0],
                    'IDs': []
                })
    ranges.append({
                    'start': float(sorted_data[point1]["Value"] or 0),
                    'stop': float(sorted_data[point2]["Value"] or 0),
                    'color': color_set[1],
                    'IDs': []
                })
    ranges.append({
                    'start': float(sorted_data[point2]["Value"] or 0),
                    'stop': float(sorted_data[point3]["Value"] or 0),
                    'color': color_set[2],
                    'IDs': []
                })
    ranges.append({
                    'start': float(sorted_data[point3]["Value"] or 0),
                    'stop': float(sorted_data[total - 1]["Value"] or 0),
                    'color': color_set[3],
                    'IDs': []
                })
    for f in sorted_data:
        matched = next(x for x in ranges if (x["start"] <= parse_number(f["Value"])) and (x["stop"] >= parse_number(f["Value"])))
        matched['IDs'].append(f["dynaID"])
    #print(*ranges, sep = "\n")
    return ranges
