# Data map

    themap.common.init_session()
    options = {
            'Title' : 'Sample Data Map',
            'Description' : 'Example explaining how to create data map',
            'Handle' : 'data-map-handle'
    }
    map = themap.map.create_map(options)
    layer = map.add_layer({
        'Name' : 'Data Layer'
    })
    layer.import_file('data.geojson',"name_property")
    # In case you want to update layer information.
    layer.Name = 'Change layer name'
    layer.HoverField = 'Specify field to show on mouse over'
    layer.update()
    print('Map generated : https://themap.net/maps/view/'+map.Handle)

For complete reference to all possible map options and layer options, Refer [Layer definition](../concepts/layer_options.md) and [Map options](../concepts/map_options.md)