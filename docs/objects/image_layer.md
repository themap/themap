# Image layer

Image layer is specific layer type which can contain point type geometries. It's meant to represent any image as geographic point on the map. Typical image layer object looks like this.

## Fields

* `IsVisible` - If True, layer will be rendered by default when map is viewed. e.g. `True`
* `Name` - Name of the layer to display. e.g. `'Layer Name Here'`
* `Content` - When layer is presentation layer, HTML content which should be displayed when this layer is on. e.g. `<p>rich html content</p>`
* `HoverField` - Field which should be displayed along with shape name when use mouse over the shape. e.g. `'population'`
* `SourceUrl` - In case you want to provide link to the source of data for reference/credits. e.g. `'https://mysite.com'`

## Methods

### add_images

It adds set of images to the image layer inside a map. 

**Signature**: `add_images(images)`

**Params**

- `images` **{array}**: An array of dict. Each dict should contain 4 keys: `Title`,`Url`,`Latitude` and `Longitude`. 

**Returns**: `images` **{array}**
