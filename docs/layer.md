# Layer functions

All the layer functions are packed inside layer modole. e.g. `themap.layer.create_layer`

## create_layer

It creates new layer inside a map.

## get_default_style

It provides default style defination for layer. Ideally after creating new layer, if you intend to style it further, you should acquire defualt style object and change that object further. e.g.

    layer = themap.layer.create_layer(layer,token)
    style = themap.layer.get_default_style()
        #...
        #You might want to manipulate style object here...
        #...
    layer["GLStyle"] = json.dumps(style)
        #...
        # You might pass this style defination to other funtions to apply further styling
        # e.g. themap.layer.apply_category_colors(layer,'<<categofy_field>>',token)
        # Style is now assigned in layer, let's update layer
    layer = themap.layer.update_layer(layer,token)