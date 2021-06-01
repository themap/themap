# Layer functions

All the layer functions are packed inside layer modole. e.g. `themap.layer.create_layer`

## create_layer

It creates new layer inside a map.

**Signature**: `create_layer(layer,token)`

**Params**

- `layer` **{dict}**: [layer dict](concepts/layer_defination.md#object-schema) with `TourMapID` as required field
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server layer dict


## get_default_style

It provides default style defination for layer. Ideally after creating new layer, if you intend to style it further, you should acquire defualt style dict and change that dict further. e.g.

    layer = themap.layer.create_layer(layer,token)
    style = themap.layer.get_default_style()
        #...
        #You might want to manipulate style dict here...
        #...
    layer["GLStyle"] = json.dumps(style)
        #...
        # You might pass this style defination to other funtions to apply further styling
        # e.g. themap.layer.apply_category_colors(layer,'<<categofy_field>>',token)
        # Style is now assigned in layer, let's update layer
    layer = themap.layer.update_layer(layer,token)


**Signature**: `get_default_style()`

**Returns**: `style` **{dict}** default [style dict](concepts/layer_style_defination.md#style-object-schema)

## apply_category_colors

It will apply category based colors to layer and update the style information on themap server.

**Signature**: `apply_category_colors(layer, field, token, colors = {})`

**Params**

- `layer` **{dict}**: layer dict on which category colors should be applied
- `field` **{string}**: field which should be used as a category
- `token` **{string}**: auth token
- `colors` **{dict}**: color dict to specify color for particular category. If not specified, it will pick random colors

**Returns**: `layer` **{dict}** updated layer dict

## apply_bucket_colors

It will apply quartile bucket colors to layer and update the style information on themap server.

**Signature**: `apply_bucket_colors(layer, field, colors, token)`

**Params**

- `layer` **{dict}**: layer dict on which quartile colors should be applied
- `field` **{string}**: field which should be used create quartile
- `colors` **{string}**: `-` separated color codes for quartile. e.g. `"#0000ff-#00ff00-#ffff00-#0000ff"`
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** updated layer dict

## apply_gradient_colors

It will apply gradient colors to layer and update the style information on themap server.

**Signature**: `apply_gradient_colors(layer, field, colors, token)`

**Params**

- `layer` **{dict}**: layer dict on which gradient colors should be applied
- `field` **{string}**: field which should be used generate gradient
- `colors` **{string}**: `-` separated color codes for min and max. e.g. `"#0000ff-#00ff00"`
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** updated layer dict

## apply_gradient_sizes

It will apply gradient sizes to layer and update the style information on themap server.

**Signature**: `apply_gradient_sizes(layer, field, sizes, token)`

- `layer` **{dict}**: layer dict on which gradient sizes should be applied
- `field` **{string}**: field which should be used generate gradient
- `colors` **{string}**: `-` separated min (`0.1`) and max (`2.0`) sizes. e.g. `"0.5-1.5"`
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** updated layer dict