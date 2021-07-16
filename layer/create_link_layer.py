import requests
from .link_layer_class import LinkLayer
from ..common import config

def create_link_layer(layer):
    print('Creating Layer : '+ layer['Name'])
    headers = {'authorization': 'Bearer '+config.token}
    r = requests.post('https://api.themap.net/api/Tour2/AddLinkLayer', data = layer, headers = headers)
    return LinkLayer(r.json())
