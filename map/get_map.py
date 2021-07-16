
import requests
from .map_class import Map
from ..common import config

def get_map(handle):
    print('Retriving Map : '+handle)
    payload = {
        "handle" : handle
    }
    headers = {'authorization': 'Bearer '+config.token}
    r = requests.get('https://api.themap.net/api/Tour2/ResolveTourMapID',params=payload, headers = headers)
    payload = {
        "tourmapID" : r.json()
    }
    r = requests.get('https://api.themap.net/api/Tour2/GetTourMap',params=payload, headers = headers)
    return Map(r.json())
