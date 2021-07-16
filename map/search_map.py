import requests
from ..common import config
from .map_class import Map

def search_map(search_key,take = 20,skip = 0):
    print('Searching Map : '+ search_key)
    headers = {'authorization': 'Bearer '+config.token}
    search = {
        'SearchKey' : search_key,
        'Take' : take,
        'Skip' : skip
    }
    r = requests.post('https://api.themap.net/api/Tour2/SearchTours', data = search, headers = headers)
    result = map(lambda x: Map(x),r.json())
    return list(result)
