# Layer functions

All the layer functions are packed inside layer modole. e.g. `themap.layer.create_layer`

## create_layer

It creates new data layer inside a map.

**Signature**: `create_layer(layer,token)`

**Params**

- `layer` **{dict}**: [layer dict](concepts/layer_defination.md#object-schema) with `TourMapID` as required field
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server data layer dict

## update_layer

It updates the data layer inside a map.

**Signature**: `update_layer(layer,token)`

**Params**

- `layer` **{dict}**: [layer dict](concepts/layer_defination.md#object-schema) with `TourMapID` and `ID` as required fields
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server data layer dict


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

## apply_category_outline_colors

It will apply category based colors to layer outline and update the style information on themap server.

**Signature**: `apply_category_outline_colors(layer, field, token, colors = {})`

**Params**

- `layer` **{dict}**: layer dict on which category colors should be applied
- `field` **{string}**: field which should be used as a category
- `token` **{string}**: auth token
- `colors` **{dict}**: color dict to specify color for particular category. If not specified, it will pick random colors

**Returns**: `layer` **{dict}** updated layer dict



## apply_gradient_sizes

It will apply gradient sizes to layer and update the style information on themap server.

**Signature**: `apply_gradient_sizes(layer, field, sizes, token)`

**Params**

- `layer` **{dict}**: layer dict on which gradient sizes should be applied
- `field` **{string}**: field which should be used generate gradient
- `colors` **{string}**: `-` separated min (`0.1`) and max (`2.0`) sizes. e.g. `"0.5-1.5"`
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** updated layer dict


## delete_layer

It will delete particular data layer from map.

**Signature**: `delete_layer(id,source_file,token)`

**Params**

- `id` **{number}**: ID of the layer to be deleted
- `source` **{string}**: `GLSource` property of the layer to be deleted
- `token` **{string}**: auth token

## download_layer

It will download complete layer data along with geometry as geoJSON file.

**Signature**: `download_layer(id,token,as_file = None)`

**Params**

- `id` **{number}**: ID of the layer to be downloaded
- `token` **{string}**: auth token
- `as_file` **{string}**: It will be path of the geoJSON file to be genrated from layer

**Returns**: `geoJSON/path` **{dict/string}** if `as_file` is not provided, it will return geoJSON dict object otherwise filepath of downloaded geoJSON file.

## import_file

It will take geoJSON file and upload it to layer as geometry + data.

**Signature**: `import_file(filepath,name_prop,map_id,token,layer_id = None)`

**Params**

- `filepath` **{string}**: Path of the geoJSON file to be uploaded
- `name_prop` **{string}**: GeoJSON property name which should be used as name of each shape
- `map_id` **{number}**: ID of the map in which file should be imported
- `layer_id` **{number}**: Optional ID of the layer in which file should be imported
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server data layer dict

## update_feature

It updates the feature of the layer for it's content which is being displayed when featureis selected.

**Signature**: `update_feature(feature_id,name,template,token)`

**Params**

- `feature_id` **{number}**: ID of the feature to be updated.
- `name` **{string}**: updated name for the feature
- `template` **{array}**: [template](concepts/feature_content_template.md) of the feature content.
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server data layer dict


## generate_feature_html

It takes input template and generate html which can be used further as feature content.

**Signature**: `generate_feature_html(template)`

**Params**

- `template` **{array}**: [template](concepts/feature_content_template.md) of the feature content.

**Returns**: `html` **{string}** generated html content based on


## create_image_layer

It creates new image layer inside a map. Image layer is a layer type where each shape is assumed to be point representing any image.

**Signature**: `create_image_layer(layer,token)`

**Params**

- `layer` **{dict}**: [image layer dict](concepts/image_layer_defination.md#object-schema) with `TourMapID` as required field
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server image layer dict

## add_images_to_image_layer

It adds set of images to the image layer inside a map. 

**Signature**: `add_images_to_image_layer(layer,images,token)`

**Params**

- `layer` **{dict}**: [image layer dict](concepts/image_layer_defination.md#object-schema) with `TourMapID` as required field
- `images` **{array}**: An array of dict. Each dict should contain 4 keys: `Title`,`Url`,`Latitude` and `Longitude`. 
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server image layer dict


## create_link_layer

It creates new link layer inside a map. Link layer is a layer type where each shape is assumed to be point representing any url.

**Signature**: `create_link_layer(layer,token)`

**Params**

- `layer` **{dict}**: [link layer dict](concepts/link_layer_defination.md#object-schema) with `TourMapID` as required field
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server link layer dict

## add_links_to_link_layer

It adds set of links to the link layer inside a map. 

**Signature**: `add_links_to_link_layer(layer,links,token)`

**Params**

- `layer` **{dict}**: [link layer dict](concepts/link_layer_defination.md#object-schema) with `TourMapID` as required field
- `link` **{array}**: An array of dict. Each dict should contain 3 keys: `Url`,`Latitude` and `Longitude`. Themap API would parse metadata from the link automatically.
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server link layer dict


## add_link_property

It will add property to link object.

**Signature**: `add_link_property(link,name,value,token)`

**Params**

- `link` **{dict}**: link dict containing linkID. When link layer is retreived from API, it will have `Links` property containing all the links.
- `name` **{string}**: Name of the property to add
- `value` **{string}**: Value of the property to add
- `token` **{string}**: auth token

**Returns**: `layer` **{dict}** server link property dict
