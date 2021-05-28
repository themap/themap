# Introduction

[TheMap python](https://github.com/themap/themap) package is developed to expose various themap APIs as python package. This helps to build various python scripting automation for python community.

## Modules

Overall package is divided into 4 modules.

* `map` - Map level functions.
* `layer` - Layer level functions.
* `common` - Common functions accoss the package
* `extras` - Not the core functions but something nice to have for more productivity

## Package layout

    ...    # Root level files
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    map    # map module
        create_map.py # Create Map
        ...           # Other map level functions
    layer  # layer module
        create_layer.py # Create Layer
        ...             # Other layer level functions
    common  # common module
        generate_screenshot.py # Generates the screenshot of the map
        ...                    # Other common functions
    extras  # extras module
        generate_crime_file.py # Generates geojson from dallas crime API
        ...                    # Other extra functions
