import requests

def create_link_layer(layer,token):
    print('Creating Layer : '+ layer['Name'])
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/AddLinkLayer', data = layer, headers = headers)
    return r.json()
