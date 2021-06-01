# Link layer defination

Data layer is specific layer type which can contain point type geometries. It's meant to represent any web link as geographic point on the map. Typical link layer object looks like this.

## Object Schema
    {
        'IsVisible' : True,
        'Name' : 'Layer Name Here',
        'TourMapID' : 123,
        'Content' : None,
        'Description' : None,
        'HoverField' : None,
        'SourceUrl' : None
    }

## Explanation

* `IsVisible` - If True, layer will be rendered by default when map is viewed.
* `Name` - Name of the layer to display
* `TourMapID` - ID of map this layer belongs to
* `Content` - When layer is presentation layer, HTML content which should be displayed when this layer is on
* `HoverField` - Field which should be displayed along with shape name when use mouse over the shape.
* `SourceUrl` - In case you want to provide link to the source of data for reference/credits