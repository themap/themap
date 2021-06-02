import requests

def add_images_to_image_layer(layer,images,token):
    headers = {'authorization': 'Bearer '+token}
    print("Uploading "+str(len(images))+" image(s)...")
    r = requests.post('https://api.themap.net/api/Tour2/AddImagesToImageLayer?layerID='+str(layer['ID']), json = images, headers = headers)
    return r.json()
