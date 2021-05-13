
import requests

def delete_layer(id,source_file,token):
    print('Deleting Layer : '+str(id))
    payload = {
        "layerID" : id,
        "GLSource" : source_file
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/DeleteLayer',params=payload, headers = headers)
    return r.json()
