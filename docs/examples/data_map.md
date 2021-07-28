# Data map

    themap.common.init_session()
    map_options = {
            'Title' : 'Sample Data Map',
            'Description' : 'Example explaining how to create data map',
            'Handle' : 'data-map-handle'
    }
    my_map = themap.map.create_map(map_options)
    my_layer = my_map.add_layer({
        'Name' : 'Data Layer'
    })
    my_layer.import_file('data.geojson',"name_property")
    # In case you want to update layer information.
    my_layer.Name = 'Change layer name'
    my_layer.HoverField = 'Specify field to show on mouse over'
    my_layer.update()
    print('Map generated : https://themap.net/maps/view/'+my_map.Handle)

For complete reference to all possible map options and layer options, Refer [Layer definition](../concepts/layer_options.md) and [Map options](../concepts/map_options.md)