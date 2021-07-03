import json
import random
import requests

def apply_category_stroke_colors(layer, field, token, colors = {}): 
    print('Appling Category stroke colors by '+field+'...')
    style = json.loads(layer["GLStyle"])
    style['legend']['stroke-color']['field'] = field
    style['legend']['stroke-color']['type'] = 'category'
    
    style['common']['common-stroke-color'] = {
        'type' : "categorical",
        'property' : "dynaID",
        'stops' : []
    }
    category_data = generate_categories(layer["ID"], field, token,colors)
    style['legend']['stroke-color']['categories'] = category_data['categories']
    style['common']['common-stroke-color']['stops'] = category_data['stops']
    layer["GLStyle"] = json.dumps(style)
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/UpdateTourMapLayer', data = layer, headers = headers)
    return r.json()

def parse_number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0

def random_color():
    return "#"+("%06x" % random.randint(0, 0xFFFFFF))
    
def generate_categories(layer_id, field, token,colors): 
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
            "color" : colors[value] if value in colors else random_color()
        })
    stops = []
    for item in data:
        for category in categories:
            if item["Value"] == category["value"]:
                stops.append([item["dynaID"],category["color"]])
                break

    return {'categories' : categories, 'stops' : stops}
