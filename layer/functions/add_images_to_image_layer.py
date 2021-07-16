import requests

def add_images_to_image_layer(layerID,images,token):
    headers = {'authorization': 'Bearer '+token}
    print("Uploading "+str(len(images))+" image(s)...")
    r = requests.post('https://api.themap.net/api/Tour2/AddImagesToImageLayer?layerID='+str(layerID), json = images, headers = headers)
    return r.json()
