# Link layer

Data layer is specific layer type which can contain point type geometries. It's meant to represent any web link as geographic point on the map. Typical link layer object looks like this.

## Fields

* `IsVisible` - If True, layer will be rendered by default when map is viewed. e.g. `True`
* `Name` - Name of the layer to display. e.g. `'Layer Name Here'`
* `Content` - When layer is presentation layer, HTML content which should be displayed when this layer is on. e.g. `'<p>Rich html content</p>'`
* `HoverField` - Field which should be displayed along with shape name when use mouse over the shape. e.g. `'population'`
* `SourceUrl` - In case you want to provide link to the source of data for reference/credits. e.g. `https://mysite.com`

## Methods

### add_links

It adds set of links to the link layer. 

**Signature**: `add_links(links)`

**Params**

- `links` **{array}**: An array of dict. Each dict should contain 3 keys: `Url`,`Latitude` and `Longitude`. Themap API would parse metadata from the link automatically.

**Returns**: `links` **{array}**


### add_link_property

It will add property to link object.

**Signature**: `add_link_property(link,name,value)`

**Params**

- `link` **{dict}**: link dict containing linkID. When link layer is retreived from API, it will have `Links` property containing all the links.
- `name` **{string}**: Name of the property to add
- `value` **{string}**: Value of the property to add

**Returns**: **{void}**
