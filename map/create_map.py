import requests

def create_map(tourmap,token):
    print('Creating Map : '+ tourmap['Title'])
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/AddTourMap', data = tourmap, headers = headers)
    return r.json()
