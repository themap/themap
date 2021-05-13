
import requests
import urllib.request
import json

def download_layer(id,token,as_file):
    print('Downloading layer : '+str(id))
    payload = {
        "layerID" : id
    }
    headers = {'authorization': 'Bearer '+token}
    r = requests.get('https://api.themap.net/api/Tour2/GenerateGeoJsonFromLayer',params=payload, headers = headers)
    url = 'https://api.themap.net/api/Tour2/DownloadGeoJsonFile?fileName='+r.text.replace('"','')
    if as_file:
        file_path = 'data/'+str(id)+'.json'
        urllib.request.urlretrieve(url, file_path)
        print('File downloaded : '+file_path)
        return file_path
    else:
        f = urllib.request.urlopen(url)
        myfile = f.read()
        return json.loads(myfile)