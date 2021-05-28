# Layer style defination

TheMap data layers are split into geometry and non-geometry data when layer is created. This is essential to speed up the viewing expeirience specially when size is larger. That also means that style data is decouped from geometry data. This style object provides defination about how geometry should be styled. A typical style object looks like this.

## Style object schema

    {
        'common' : {
            'common-color': '#074223',
            'common-stroke-color': '#ffffff',
            'common-opacity': 0.7,
            'common-width': 3,
            'common-size': 0.5,
            'common-image': "marker",
            'common-height': 1000,
            'extrusion' : False
        },
        "colorType": 'uniform',
        "legend": {
            "showLegend": True,
            "format" : False,
            "extrude" :{
                "type": "gradient",
                "field": None,
                "min": {},
                "max": {},
            },
            "color": {
                "type": "uniform",
                "color": "#074223",
                "field": None,
                "min": {},
                "max": {},
                "categories": [],
                "ranges": []
            },
            "size": {
                "type": "uniform",
                "size": 0.5,
                "field": None,
                "min": {},
                "max": {},
                "categories": [],
                "ranges": []
            }
        }
    }

The above object is the same object you receive from [layer.get_default_style](../layer.md#get_default_style) function. Following sections describes behavior driven by each field of style object.

## Common

This object contains styling definations regarding appearance of the layer.

    {
        'common-color': '#074223',
        'common-stroke-color': '#ffffff',
        'common-opacity': 0.7,
        'common-width': 3,
        'common-size': 0.5,
        'common-image': "marker",
        'common-height': 1000,
        'extrusion' : False
    }

### common-color

Defines the color of shapes. It should be hex color code always. If unspecified, shapes will go black. For shape types which have stroke and fill (e.g. Polygon, circle), this field acts as fill color.

### common-stroke-color

Certain shape types (e.g. Polygon, Circle) can have different shape color and also different stroke/outline color. For those shapes, this field provides stroke color value.

### common-opacity

Defines the opacity of the shapes. Value range `min : 0, max:1`

### common-width

Defines the stroke width of the shape. e.g. stroke width of circle, line width of line shape. Value range `min : 1, max:10`

### common-size

Defines the size of point type shapes. Point type shapes can be either markers or circles defined by [common-image](#common-image) field. Either the case, this field will provide size of marker/circle. Value range `min : 0.1, max:2`

### common-image

This field defines whether points should be rendered as marker or circle. By default it'se set to `'marker'`. If you want to turn points into circle, set this filed to `None` and it would render points as circles.

### common-height

When layer has [extrusion](#extrusion) enabled this field decides the height of extrusion. This field can accept any data driven style defination accepted by [mapbox extrusion height](https://docs.mapbox.com/mapbox-gl-js/style-spec/layers/#paint-fill-extrusion-fill-extrusion-height). 

### extrusion

Defines the color of shapes.

This field decides whether to enable extrusion for particular layer or not. Posiible values are `True` or `False`.

## colorType

This field defines the type of color scheme layer will adopt. There are 4 possible values :

* `'uniform'` - Layer has uniform color accross the shapes.
* `'gradient'` - Layer has gradient color accross the shapes.
* `'category'` - Layer has category based color for each shape.
* `'buckets'` - Layer has bucket based color for shapes grouped in particular bucket.