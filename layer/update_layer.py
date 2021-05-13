import requests

def update_layer(layer,token):
    print('Updating Layer : '+layer["Name"])
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/UpdateTourMapLayer', data = layer, headers = headers)
    return r.json()
