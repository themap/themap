import requests

def update_map(tourmap,token):
    print('Updating Map : '+tourmap["Title"])
    headers = {'authorization': 'Bearer '+token}
    if tourmap["Layers"] == None:
        tourmap["Layers"] = []
    if tourmap["DynaLayers"] == None:
        tourmap["DynaLayers"] = []
    if tourmap["TileLayers"] == None:
        tourmap["TileLayers"] = []
    r = requests.post('https://api.themap.net/api/Tour2/UpdateTourMap', json = tourmap, headers = headers)
    return r.json()