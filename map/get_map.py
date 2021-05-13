
import requests

def get_map(handle,token):
    print('Retriving Map : '+handle)
    payload = {
        "handle" : handle
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/ResolveTourMapID',params=payload, headers = headers)
    payload = {
        "tourmapID" : r.json()
    }
    r = requests.get('https://api.themap.net/api/Tour2/GetTourMap',params=payload, headers = headers)
    return r.json()
