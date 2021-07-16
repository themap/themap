import requests
from .image_layer_class import ImageLayer
from ..common import config

def create_image_layer(layer):
    print('Creating Layer : '+ layer['Name'])
    headers = {'authorization': 'Bearer '+config.token}
    r = requests.post('https://api.themap.net/api/Tour2/AddTourMapImageLayer', data = layer, headers = headers)
    return ImageLayer(r.json())
