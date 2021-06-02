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

For complete reference to all possible map options and layer options, Refer [Layer defination](../concepts/layer_defination.md) and [Map defination](../concepts/map_defination.md)