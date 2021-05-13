import json
import requests
from numpy import interp

def apply_gradient_sizes(layer, field, sizes, token): 
    print('Appling size by '+field+'...')
    style = None
    if layer["GLStyle"] is None:
        style = {
            'colorType' : 'uniform',
            'legend' : {
                'showLegend' : True,
                'color' : {
                    'type' : "uniform",
                    'field' : None,
                    'ranges' :[]
                },
                "size": {

                }
            },
            'common' : {
                'common-color': '#074223',
                'common-stroke-color': '#ffffff',
                'common-opacity': 0.7,
                'common-width': 3,
                'common-size': 0.5,
                'common-height': 1000,
                'common-image': None
            }
        }
    else :
        style = json.loads(layer["GLStyle"])
        
    style['legend']['size'] = {
        'type': "gradient",
        "size": 0.5,
        "field": field,
        "min": {
            "value" : 0,
            "size" : 5
        },
        "max": {
            "value" : 100,
            "size" : 10
        }
    }
    style['common']['common-size'] = {
        'type' : "categorical",
        'property' : "dynaID",
        'stops' : []
    }

    style['common']['common-image'] = None

    ranges = generate_gradient_ranges(layer["ID"], field,sizes, token)
    style['legend']['size']['min'] = ranges['min']
    style['legend']['size']['max'] = ranges['max']
    style['common']['common-size']['stops'] = ranges['stops']
            
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
    
def generate_gradient_ranges(layer_id, field,sizes, token): 
    headers = {'authorization': 'Bearer '+token}
    payload = {
        "layerID" : layer_id,
        "property" : field
    }
    print("Loading "+field+" data...")
    r = requests.get('https://api.themap.net/api/Tour2/GetLayerPropertyValues',params=payload, headers = headers)
    data = r.json()
    sorted_data = newlist = sorted(data, key=lambda x: parse_number(x["Value"]), reverse=False)
    total = len(sorted_data)
    
    sizes = sizes or "0.5-1.5"
    size_set = sizes.split("-")

    ranges = {
        'min' : {
            'value' : sorted_data[0]["Value"] or 0,
            'size' : size_set[0]
        },
        'max' : {
            'value' : sorted_data[total-1]["Value"] or 0,
            'size' : size_set[1]
        },
        'stops' : []
    }
    
    for f in sorted_data:
        value = interp(f["Value"],[sorted_data[0]["Value"],sorted_data[total-1]["Value"]],[parse_number(size_set[0]),parse_number(size_set[1])])
        ranges['stops'].append([f["dynaID"],value*20])
    #print(*ranges, sep = "\n")
    return ranges
