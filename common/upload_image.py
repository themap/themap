import requests
import base64

def upload_image(local_path,token):
    print('Uploading image : '+ local_path)
    headers = {'authorization': 'Bearer '+token}
    encoded = base64.b64encode(open(local_path, "rb").read())
    post_data ={
        "Data": 'data:img/jpeg;base64,'+encoded.decode('utf-8'),
        "Type": "image/jpeg",
        "DoNotResize": False
    }
    r = requests.post('https://api.themap.net/api/Tour2/AddImage', data = post_data, headers = headers)
    return r.json()['location']
