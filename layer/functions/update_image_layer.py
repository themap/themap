import requests

def update_image_layer(layer,token):
    print('Updating Layer : '+layer["Name"])
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/UpdateImageLayer', data = layer, headers = headers)
    return r.json()
