
import requests

def get_cities():
    print('Retriving cities...')
    r = requests.get('https://api.themap.net/api/Features/GetCities')
    return r.json()
