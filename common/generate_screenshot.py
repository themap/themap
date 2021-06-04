import requests
from ..map import update_map

def generate_screenshot(map,token): 
    url = "https://themap.net/maps/view/"+map["Handle"]+"?screenshot=1&hasPageReady=1"
    print("Generating screenshot...")
    params = {'url': url}
    r = requests.get('https://themap.net/screen-shot',params = params)
    print(r.text)
    map["Logo"] = r.text
    return update_map(map,token)