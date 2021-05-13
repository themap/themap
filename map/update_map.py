import requests

def update_map(tourmap,token):
    print('Updating Map : '+tourmap["Title"])
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/UpdateTourMap', json = tourmap, headers = headers)
    return r.json()
