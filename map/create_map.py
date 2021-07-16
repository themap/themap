import requests
from ..common import config
from .map_class import Map

def create_map(options):
    print('Creating Map : '+ options['Title'])
    headers = {'authorization': 'Bearer '+config.token}
    r = requests.post('https://api.themap.net/api/Tour2/AddTourMap', data = options, headers = headers)
    return Map(r.json())
