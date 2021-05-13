
import requests

def transfer_map(map_id,user_id,token):
    payload = {
        "userId" : user_id,
        "mapId" : map_id
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/Transfer',params=payload, headers = headers)
    return r.text
