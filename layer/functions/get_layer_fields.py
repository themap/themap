
import requests

def get_layer_fields(layer_id,token):
    print('Retriving Fields : '+str(layer_id))
    payload = {
        "layerID" : map_id
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/GetLayerProperties',params=payload, headers = headers)
    return r.json()
