import requests
from . import update_map

def generate_screenshot(map_object,token): 
    url = "https://themap.net/maps/view/"+map_object.Handle+"?screenshot=1&hasPageReady=1"
    print("Generating screenshot...")
    params = {'url': url}
    r = requests.get('https://themap.net/screen-shot',params = params)
    print(r.text)
    map_object.Logo = r.text
    return update_map(map_object.to_dict(),token)