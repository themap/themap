# Image map

    themap.common.init_session()
    map_options = {
                'Title' : 'Sample Image Map',
                'Description' : 'Example image map',
                'Handle' : 'example-image-map'
            }
    my_map = themap.map.create_map(map_options) 
    my_layer = my_map.add_image_layer({
                'IsVisible' : True,
                'Name' : 'Layer Name Here'
            })
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
            image['Url'] = themap.common.upload_image(row['ImageFile'])
        my_layer.add_images(images)
    # In case you want to take snapshot of map and set it as display image of map.    
    my_map.generate_screenshot()
    print('Map generated : /'+my_map.Handle)

For complete reference to all possible map options and layer options, Refer [Image Layer definition](../concepts/image_layer_options.md) and [Map options](../concepts/map_options.md)