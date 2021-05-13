import requests

def search_map(search_key,token,take = 20,skip = 0):
    print('Searching Map : '+ search_key)
    headers = {'authorization': 'Bearer '+token}
    search = {
        'SearchKey' : search_key,
        'Take' : take,
        'Skip' : skip
    }
    r = requests.post('https://api.themap.net/api/Tour2/SearchTours', data = search, headers = headers)
    return r.json()
