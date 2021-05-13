import requests

def import_file(filename,name_prop,map_id,layer_id,token):
    file = filename
    files = {'tileJSON': open(file,'rb')}
    values = {'tourmapID': map_id, 'nameProp': name_prop, 'layerID': layer_id}
    print('Uploading File : '+file)
    headers = {'authorization': 'Bearer '+token}
    r = requests.post('https://api.themap.net/api/Tour2/UploadFile', files=files, data=values, headers = headers)
    return r.json()
