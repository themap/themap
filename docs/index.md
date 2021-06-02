# Getting started

Using [TheMap python](https://github.com/themap/themap) package, creating map on TheMap platform using python is as simple as following code snippet.

    token = themap.common.get_token()
    options = {
            'Title' : 'Some cool title!',
            'Description' : 'This is awesome!',
            'Handle' : 'my-map-handle'
    }
    map = themap.map.create_map(options)
    layer = themap.layer.import_file('data.geojson',"name_property",map["ID"],token)
    print('Map generated : https://themap.net/maps/view/'+tourmap['Handle'])