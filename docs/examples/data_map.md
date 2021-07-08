# Data map

    token = themap.common.get_token()
    options = {
            'Title' : 'Sample Data Map',
            'Description' : 'Example explaining how to create data map',
            'Handle' : 'data-map-handle'
    }
    map = themap.map.create_map(options)
    layer = themap.layer.import_file('data.geojson',"name_property",map["ID"],token)
    # In case you want to update layer information.
    layer['Name'] = 'Change layer name'
    layer['HoverField'] = 'Specify field to show on mouse over'
    themap.layer.update_layer(layer,token)
    print('Map generated : https://themap.net/maps/view/'+tourmap['Handle'])

For complete reference to all possible map options and layer options, Refer [Layer definition](../concepts/layer_definition.md) and [Map definition](../concepts/map_definition.md)