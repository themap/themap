# Layer

Data layer is very generic layer type in TheMap which faciliates any geojson rendering on map.

## Fields

* `IsVisible` - If True, layer will be rendered by default when map is viewed. e.g. `True`
* `Name` - Name of the layer to display. e.g. `'Layer Name Here'`
* `Content` - When layer is presentation layer, HTML content which should be displayed when this layer is on. e.g. `<p>Rich content here</p>`
* `GLStyle` - Style definition of layer as json string. See [Style definition](layer_style_definition.md) for more details.
* `HoverField` - Field which should be displayed along with shape name when use mouse over the shape. e.g. `'population'`
* `SourceUrl` - In case you want to provide link to the source of data for reference/credits. e.g. `'https://mysite.com'`
* `IsShowProperties` - If True, clicking on shape would display shape properties instead of shape HTML content. e.g. `False`
* `VisibleProperties` - if IsShowProperties is set to True then this field decides which properties to show. It will have comma seprated list of property names. e.g. `"prop1,prop2,prop3"`

## Methods


### update

It updates the layer.

**Signature**: `update(layer_options)`

**Params**

- `layer_options` **{dict}**: [options dict](../concepts/layer_options.md#object-schema)

**Returns**: `layer` [**{object}**](layer.md)

---

### color_by

It will apply provided color scheme to the layer and update the style information on themap server.

**Signature**: `color_by(field, scheme, colors = {})`

**Params**

- `field` **{string}**: field which should be used to apply color scheme.
- `scheme` **{string}**: color scheme to apply. Possible values : `category`,`bucket` or `gradient`
- `colors` **{dict}** or **{string}**: For category scheme, this will dict to specify colors for particular category. If not specified, it will pick random colors. For bucket scheme, it will be `-` separated color codes for quartile. e.g. `"#0000ff-#00ff00-#ffff00-#0000ff"`. For gradient scheme, it will be `-` separated color codes for min and max. e.g. `"#0000ff-#00ff00"`

**Returns**: `layer` [**{object}**](layer.md)

---

### outline_color_by

It will apply specified color scheme to layer outline and update the style information on themap server.

**Signature**: `outline_color_by(field, scheme, colors = {})`

**Params**

- `field` **{string}**: field which should be used as a category
- `scheme` **{string}**: color scheme to apply. Possible values : `category`
- `colors` **{dict}**: color dict to specify color for particular category. If not specified, it will pick random colors

**Returns**: `layer` [**{object}**](layer.md)

---

### opacity_by

It will apply specifie opacity scheme to layer and update the style information on themap server.

**Signature**: `opacity_by(field, opacities = {})`

**Params**

- `field` **{string}**: field which should be used as a category
- `scheme` **{string}**: color scheme to apply. Possible values : `category`
- `opacities` **{dict}**: opacity dict to specify opacity for particular category. If not specified, it will pick random value

**Returns**: `layer` [**{object}**](layer.md)

---

### size_by

It will apply gradient sizes to layer and update the style information on themap server.

**Signature**: `size_by(field, scheme, sizes)`

**Params**

- `field` **{string}**: field which should be used generate gradient
- `scheme` **{string}**: size scheme to apply. Possible values : `gradient`
- `sizes` **{string}**: `-` separated min (`0.1`) and max (`2.0`) sizes. e.g. `"0.5-1.5"`

**Returns**: `layer` [**{object}**](layer.md)

---

### delete

It will delete particular data layer from map.

**Signature**: `delete()`

---

### download

It will download complete layer data along with geometry as geoJSON file.

**Signature**: `download(as_file = None)`

**Params**

- `as_file` **{string}**: It will be path of the geoJSON file to be genrated from layer

**Returns**: `geoJSON/path` **{dict/string}** if `as_file` is not provided, it will return geoJSON dict object otherwise filepath of downloaded geoJSON file.

---

### import_file

It will take geoJSON file and upload it to layer as geometry + data.

**Signature**: `import_file(filepath,name_prop)`

**Params**

- `filepath` **{string}**: Path of the geoJSON file to be uploaded
- `name_prop` **{string}**: GeoJSON property name which should be used as name of each shape

**Returns**: `layer` [**{object}**](layer.md)
