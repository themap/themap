def get_default_style():
    style = {
        'common' : {
            'common-color': '#074223',
            'common-stroke-color': '#ffffff',
            'common-stroke-opacity': 0.7,
            'common-opacity': 0.7,
            'common-width': 3,
            'common-size': 0.5,
            'common-image': "marker",
            'common-height': 1000,
            'image-marker' : None,
            'extrusion' : False,
            'outline' : False,
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
            "outlineColor": {
                "type": "uniform",
                "color": "#074223",
                "field": None,
                "min": {},
                "max": {},
                "categories": [],
                "ranges": []
            },
            "opacity": {
                "type": "uniform",
                "opacity": 1,
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
    return style
