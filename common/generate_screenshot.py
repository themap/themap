import requests

def generate_screenshot(tourmap,token): 
    url = "https://themap.net/maps/view/"+tourmap["Handle"]+"?screenshot=1"
    print("Generating screnshot...")
    params = {'url': url}
    r = requests.get('https://themap.net/screen-shot',params = params)
    print(r.text)
    tourmap.Logo = r.text
    print('Updating Map : '+ tourmap['Title'])
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/UpdateTourMap', data = tourmap, headers = headers)