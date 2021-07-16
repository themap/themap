
import requests

def delete_link_layer(id,token):
    print('Deleting Layer : '+str(id))
    payload = {
        "layerID" : id,
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/DeleteLinkLayer',params=payload, headers = headers)
    return r.json()
