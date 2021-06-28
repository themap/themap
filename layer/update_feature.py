import requests
from . import generate_feature_html

# Template would be array of elements here.
# Each element starts with element type. e.g. type:value
# type here can be : heading,link,image,video
def update_feature(feature_id,name,template,token):
    print('Updating Feature : '+name)
    headers = {'authorization': 'Bearer '+token}
    html = generate_feature_html(template)
    data = {
        "ID" : feature_id,
        "Html" : html,
        "Name" : name
    }
    r = requests.post('https://api.themap.net/api/Tour2/UpdateFeature', data = data, headers = headers)
    return r.json()
