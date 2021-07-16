# Layer functions

All the layer functions are packed inside layer modole. e.g. `themap.layer.create_layer`

## get_default_style

It provides default style definition for layer. Ideally after creating new layer, if you intend to style it further, you should acquire defualt style dict and change that dict further. e.g.

    layer = map.create_layer(layer_options)
    style = themap.layer.get_default_style()
        #...
        #You might want to manipulate style dict here...
        #...
    layer.GLStyle = json.dumps(style)
        #...
        # Now you can apply diffrent styles
        # e.g. layer.color_by('<<categofy_field>>','category')


**Signature**: `get_default_style()`

**Returns**: `style` **{dict}** default [style dict](concepts/layer_style_definition.md#style-object-schema)

## update_feature

It updates the feature of the layer for it's content which is being displayed when featureis selected.

**Signature**: `update_feature(feature_id,name,template,token)`

**Params**

- `feature_id` **{number}**: ID of the feature to be updated.
- `name` **{string}**: updated name for the feature
- `template` **{array}**: [template](concepts/feature_content_template.md) of the feature content.
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server data layer dict