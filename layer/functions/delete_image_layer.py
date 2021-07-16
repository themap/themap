
import requests

def delete_image_layer(id,token):
    print('Deleting Layer : '+str(id))
    payload = {
        "layerID" : id
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/DeleteImageLayer',params=payload, headers = headers)
    return r.json()
