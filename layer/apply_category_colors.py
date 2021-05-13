import json
import random
import requests

def apply_category_colors(layer, field, token): 
    print('Appling Category colors by '+field+'...')
    style = json.loads(layer["GLStyle"])
    style['legend']['color']['field'] = field
    style['legend']['color']['type'] = 'category'
    
    style['common']['common-color'] = {
        'type' : "categorical",
        'property' : "dynaID",
        'stops' : []
    }
    category_data = generate_categories(layer["ID"], field, token)
    style['legend']['color']['categories'] = category_data['categories']
    style['common']['common-color']['stops'] = category_data['stops']
    layer["GLStyle"] = json.dumps(style)
    layer["HoverField"] = field
    layer["IsShowProperties"] = True
    return layer

def parse_number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0

def random_color():
    return "#"+("%06x" % random.randint(0, 0xFFFFFF))
    
def generate_categories(layer_id, field, token): 
    headers = {'authorization': 'Bearer '+token}
    payload = {
        "layerID" : layer_id,
        "property" : field
    }
    print("Loading "+field+" data...")
    r = requests.get('https://api.themap.net/api/Tour2/GetLayerPropertyValues',params=payload, headers = headers)
    data = r.json()
    value_set = set([])
    categories = []
    for item in data:
        value_set.add(item["Value"])
    for value in value_set:
        categories.append({
            "value" : value,
            "color" : random_color()
        })
    stops = []
    for item in data:
        for category in categories:
            if item["Value"] == category["value"]:
                stops.append([item["dynaID"],category["color"]])
                break

    return {'categories' : categories, 'stops' : stops}
