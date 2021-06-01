
import requests
import urllib.request
import json

def download_layer(id,token,as_file = None):
    print('Downloading layer : '+str(id))
    payload = {
        "layerID" : id
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/GenerateGeoJsonFromLayer',params=payload, headers = headers)
    url = 'https://api.themap.net/api/Tour2/DownloadGeoJsonFile?fileName='+r.text.replace('"','')
    if as_file != None:
        urllib.request.urlretrieve(url, as_file)
        print('File downloaded : '+as_file)
        return as_file
    else:
        f = urllib.request.urlopen(url)
        myfile = f.read()
        return json.loads(myfile)