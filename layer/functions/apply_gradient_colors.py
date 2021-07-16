import json
import math
import requests
from ...common import color_fader
from ...common import filter_outliers
from numpy import interp

def apply_gradient_colors(layer, field, colors, token): 
    print('Appling Gradient colors by '+field+'...')
    style = {
        'colorType' : 'gradient',
        'legend' : {
            'showLegend' : True,
            'color' : {
                'type' : "gradient",
                'field' : field,
                'min' :{
                    'value' : 0,
                    'color' : '#ff000'
                },
                'max' :{
                    'value' : 100,
                    'color' : '#00ff00'
                }
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

    ranges = generate_gradient_ranges(layer["ID"], field,colors, token)
    style['legend']['color']['min'] = ranges['min']
    style['legend']['color']['max'] = ranges['max']
    style['common']['common-color']['stops'] = ranges['stops']

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
    
def generate_gradient_ranges(layer_id, field,colors, token): 
    headers = {'authorization': 'Bearer '+token}
    payload = {
        "layerID" : layer_id,
        "property" : field
    }
    print("Loading "+field+" data...")
    r = requests.get('https://api.themap.net/api/Tour2/GetLayerPropertyValues',params=payload, headers = headers)
    data = r.json()
    sorted_data = newlist = filter_outliers(data, value_fn=lambda x: parse_number(x["Value"]), threshold=5)
    total = len(sorted_data)
    
    colors = colors or "#ff0000-#00ff00"
    color_set = colors.split("-")

    ranges = {
        'min' : {
            'value' : sorted_data[0]["Value"] or 0,
            'color' : color_set[0]
        },
        'max' : {
            'value' : sorted_data[total-1]["Value"] or 0,
            'color' : color_set[1]
        },
        'stops' : []
    }
    
    for f in sorted_data:
        value = interp(f["Value"],[sorted_data[0]["Value"],sorted_data[total-1]["Value"]],[0,1])
        color = color_fader(color_set[0],color_set[1],value)
        ranges['stops'].append([f["dynaID"],color])
    #print(*ranges, sep = "\n")
    return ranges
