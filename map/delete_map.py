
import requests

def delete_map(id,token):
    print('Deleting Map : '+str(id))
    payload = {
        "tourmapID" : id
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/DeleteTourMap',params=payload, headers = headers)
    return r.json()
