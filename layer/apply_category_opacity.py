import json
import random
import requests

def apply_category_opacity(layer, field, token, opacities = {}): 
    print('Appling Category opacity by '+field+'...')
    style = json.loads(layer["GLStyle"])
    style['legend']['opacity']['field'] = field
    style['legend']['opacity']['type'] = 'category'
    
    style['common']['common-opacity'] = {
        'type' : "categorical",
        'property' : "dynaID",
        'stops' : []
    }
    category_data = generate_categories(layer["ID"], field, token,opacities)
    style['legend']['opacity']['categories'] = category_data['categories']
    style['common']['common-opacity']['stops'] = category_data['stops']
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
    return random.uniform(0, 1)
    
def generate_categories(layer_id, field, token,opacities): 
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
            "opacity" : opacities[value] if value in opacities else random_color()
        })
    stops = []
    for item in data:
        for category in categories:
            if item["Value"] == category["value"]:
                stops.append([item["dynaID"],category["opacity"]])
                break

    return {'categories' : categories, 'stops' : stops}
