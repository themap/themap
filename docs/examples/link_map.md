# Link map

    token = themap.common.get_token()
    options = {
                'Title' : 'Sample Link Map',
                'Description' : 'This is an example map',
                'Handle' : 'example-link-map'
            }
    map = themap.map.create_map(options,token)
    options = {
                'IsVisible' : True,
                'Name' : 'Layer Name Here',
                'TourMapID' : map["ID"]
            }
    layer = themap.layer.create_link_layer(options,token)
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
            links = themap.layer.add_links_to_link_layer(layer,[link],token)
            # It's optional to add properties, but let's take a look at how you do it...
            for prop in properties:
                themap.layer.add_link_property(links[0],prop,row[prop],token)
    print('Map generated : /'+tourmap['Handle'])

For complete reference to all possible map options and layer options, Refer [Link Layer defination](../concepts/link_layer_defination.md) and [Map defination](../concepts/map_defination.md)