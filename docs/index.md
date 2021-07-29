# Getting started

Using [TheMap python](https://github.com/themap/themap) package, creating map on TheMap platform using python is as simple as following code snippet.

    token = themap.common.init_session()
    my_map = themap.map.create_map({
            'Title' : 'Some cool title!',
            'Description' : 'This is awesome!',
            'Handle' : 'my-map-handle'
    })
    my_layer = my_map.add_layer({
            'Name' : 'My First Layer'
    })
    my_layer.import_file('data.geojson',"name_property")
    print('Map generated : https://themap.net/maps/view/'+my_map.Handle)