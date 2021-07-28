# Data layer options

Data layer is very generic layer type in TheMap which faciliates any geojson rendering on map. Typical layer object looks like this.

## Object Schema
    {
        'IsVisible' : True,
        'Name' : 'Layer Name Here',
        'Content' : None,
        'GLStyle' : None,
        'HoverField' : None,
        'SourceUrl' : None,
        'IsShowProperties' : True,
        'VisibleProperties' : "prop1,prop2,prop3"
    }

## Explanation

* `IsVisible` - If True, layer will be rendered by default when map is viewed.
* `Name` - Name of the layer to display
* `Content` - When layer is presentation layer, HTML content which should be displayed when this layer is on
* `GLStyle` - Style definition of layer. See [Style definition](layer_style_definition.md) for more details.
* `HoverField` - Field which should be displayed along with shape name when use mouse over the shape.
* `SourceUrl` - In case you want to provide link to the source of data for reference/credits
* `IsShowProperties` - If True, clicking on shape would display shape properties instead of shape HTML content
* `VisibleProperties` - if IsShowProperties is set to True then this field decides which properties to show. It will have comma seprated list of property names. If you set it to None, it will show all the properties.