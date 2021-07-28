# Link map

    themap.common.init_session()
    map_options = {
                'Title' : 'Sample Link Map',
                'Description' : 'This is an example map',
                'Handle' : 'example-link-map'
            }
    my_map = themap.map.create_map(map_options)
    my_layer = map.add_link_layer({
                'IsVisible' : True,
                'Name' : 'Layer Name Here'
            })
    with open('data/links.csv') as csv_file:
        # Define which columns you want to add to properties
        properties = ["Name","Prop1","Prop2"]
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        # Now reading CSV file line by line
        for row in csv_reader:
            link = {
                'Url' : row['URL'],
                'Latitude' : row['Latitude'],
                'Longitude' : row['Longitude']
            }
            links = my_layer.add_links([link])
            # It's optional to add properties, but let's take a look at how you do it...
            for prop in properties:
                my_layer.add_link_property(links[0],prop,row[prop],token)
    print('Map generated : /'+my_map.Handle)

For complete reference to all possible map options and layer options, Refer [Link Layer definition](../concepts/link_layer_options.md) and [Map options](../concepts/map_options.md)