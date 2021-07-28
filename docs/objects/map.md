# Map

Map object is container object representing one map on TheMap platform.

## Fields

* `Title` - Title of the map e.g. `"Sample Map"`
* `Description` - Description of the map e.g. `"This is cool!"`
* `Logo` - Logo of the map e.g. `"https"://url.to/imge.jpg"`
* `Handle` - Every map must have unique handle. This handle is something provides unique url to map as well. e.g. `"sample-map-handle"`
* `Layers` - List of data layers
* `LinkLayers` - List of link layers
* `ImageLayers` - List of image layers
* `Is3D` - Boolean deciding whether TheMap should be rendered as 3D or 2D. e.g. `false`
* `IsListed` - If True, map will be listed on TheMap publically and also visible in search. e.g. `true`
* `LayerHasContent` - If True, layers will switch to presentation mode while rendering and thus will appear one by one based on input directions. e.g. `false`
* `MapStyle` - Base layer style of the map. Possible values : `basic`,`streets`,`outdoors`,`light`,`dark` or `satellite-streets`
* `NE` - latitude/longitude pair representing North East point of map bounds. It's optional to provide this. If not provided. TheMap will calculate the bounds and decide right dispaly view automatically. Use this along with `SW` only if you want to override the map view. e.g. `[33.0133900, -96.056056]`
* `SW` - latitude/longitude pair representing South West point of map bounds. e.g. `[32.4554055, -97.432789]`
* `Tags` - Comma seprated tags to assign for the map. e.g. `Civic,Economy`
* `WebsiteUrl` - In case you want to provide link to the source of data for reference/credits. `https://mysite.com`
* `EditPermissionType` - Flag controlling who can edit the map. Possible values : 
    * `0` - Only creator can edit
    * `2` - Anyone having link can edit
    * `3` = Everyone can edit
* `ViewPermissionType` - Flag controlling who can edit the map. Possible values : 
    * `0` - Only creator can view,
    * `2` - Anyone having link can view, 
    * `3` - Everyone can view


## Methods


### update

It updates existing map with provided fields

**Signature**: `update(map_options)`

**Params**

- `map_options` **{dict}**: [map_options](../concepts/map_options.md#object-schema)

**Returns**: `map` **{object}** updated [map](map.md)

---

### features

It retrives all the features of specific map.

**Signature**: `features()`

**Returns**: `features` **{array}** list of all the features

---

### add_layer

It adds new data layer inside a map.

**Signature**: `add_layer(layer_options)`

**Params**

- `layer_options` **{dict}**: [layer dict](../concepts/layer_options.md#object-schema)

**Returns**: `layer` [**{object}**](layer.md)

---

### add_link_layer

It adds new link layer inside a map.

**Signature**: `add_link_layer(link_layer_options)`

**Params**

- `link_layer_options` **{dict}**: [layer dict](../concepts/link_layer_options.md#object-schema)

**Returns**: `link_layer` [**{object}**](link_layer.md)

---

### add_image_layer

It adds new image layer inside a map.

**Signature**: `add_image_layer(image_layer_options)`

**Params**

- `image_layer_options` **{dict}**: [layer dict](../concepts/image_layer_options.md#object-schema)

**Returns**: `image_layer` [**{object}**](image_layer.md)

---

### generate_screenshot

It generates the screenshot of the map and update the map image with the screenshot.

**Signature**: `generate_screenshot()`

**Returns**: `map` [**{object}**](map.md)

---

### delete

It deletes the map.

**Signature**: `delete()`