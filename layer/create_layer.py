import requests
from .layer_class import Layer
from ..common import config

def create_layer(layer):
    print('Creating Layer : '+ layer['Name'])
    headers = {'authorization': 'Bearer '+config.token}
    r = requests.post('https://api.themap.net/api/Tour2/AddLayer', data = layer, headers = headers)
    return Layer(r.json())
