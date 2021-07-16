# Getting started

Using [TheMap python](https://github.com/themap/themap) package, creating map on TheMap platform using python is as simple as following code snippet.

    token = themap.common.init_session()
    map = themap.map.create_map({
            'Title' : 'Some cool title!',
            'Description' : 'This is awesome!',
            'Handle' : 'my-map-handle'
    })
    layer = map.add_layer({
            'Name' : 'My First Layer'
    })
    layer.import_file('data.geojson',"name_property")
    print('Map generated : https://themap.net/maps/view/'+map.Handle)