import requests

def add_links_to_link_layer(layer,links,token):
    headers = {'authorization': 'Bearer '+token}
    print("Uploading "+str(len(links))+" link(s)...")
    r = requests.post('https://api.themap.net/api/Tour2/AddLinksToLinkLayer?layerID='+str(layer['ID']), json = links, headers = headers)
    return r.json()
