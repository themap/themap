# Image map

    token = themap.common.get_token()
    options = {
                'Title' : 'Sample Image Map',
                'Description' : 'Example image map',
                'Handle' : 'example-image-map'
            }
    map = themap.map.create_map(options,token)
    options = {
                'IsVisible' : True,
                'Name' : 'Layer Name Here',
                'TourMapID' : map["ID"]
            }
    layer = themap.layer.create_image_layer(options,token)
    with open('data/image_map.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        images = []
        # Now reading CSV file line by line
        for row in csv_reader:
            image = {
                'Title' : row['Title'],
                'Html' : row['Content'],
                'Latitude' : row['Latitude'],
                'Longitude' : row['Longitude']
            }
            images.append(image)
            image['Url'] = themap.common.upload_image(row['ImageFile'],token)
        themap.layer.add_images_to_image_layer(layer,images,token)
    # In case you want to take snapshot of map and set it as display image of map.    
    themap.common.generate_screenshot(map,token)
    print('Map generated : /'+tourmap['Handle'])

For complete reference to all possible map options and layer options, Refer [Image Layer definition](../concepts/image_layer_definition.md) and [Map definition](../concepts/map_definition.md)