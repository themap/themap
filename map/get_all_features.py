
import requests

def get_all_features(map_id,token):
    print('Retriving Features : '+str(map_id))
    payload = {
        "tourmapID" : map_id
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/GetAllFeatures',params=payload, headers = headers)
    return r.json()
