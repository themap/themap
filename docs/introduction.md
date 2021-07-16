# Introduction

[TheMap python](https://github.com/themap/themap) package is developed to expose various themap APIs as python package. This helps to build various python scripting automation for python community.

## Installation


This package is open source and available [here on github](https://github.com/themap/themap). You can install it directly from git via following pip command.

    pip install git+https://github.com/themap/themap.git#egg=themap


## Authorization

Since this python package is wrapper around the TheMap APIs. TheMap APIs are secure APIs and it needs authorization to interact with. If you don't have TheMap account, you can signup [here](https://themap.net/auth/signup) and set your credentials. Once you have you credentials you can generate your token using following function.

    themap.common.init_session()

Ideally this would be first line of your script and it will persist your token until script is running. After you initialize the session, you need not to woory about authorization until your script is complete.

## Modules

Overall package is divided into 4 modules.

* `map` - Map level functions.
* `layer` - Layer level functions.
* `common` - Common functions accoss the package

## Package layout

    ...    # Root level files
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    map    # map module
        create_map.py # Create Map
        ...           # Other map level stuffs
    layer  # layer module
        create_layer.py # Create Layer
        ...             # Other layer level stuffs
    common  # common module
        generate_screenshot.py # Generates the screenshot of the map
        ...                    # Other common stuffs