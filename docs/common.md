# Common functions

All the common functions are packed inside common modole. e.g. `themap.common.get_token`

## get_token

It take credentials of user and generate the API token using which further API communication can be authorized

**Signature**: `get_token(username=None,password=None)`

**Params**

- `username` **{string}**: TheMap username
- `password` **{string}**: TheMap password

**Returns**: `token` **{string}** API token

## generate_screenshot

It generates the screenshot of the map and update the map image with the screenshot.

**Signature**: `generate_screenshot(map,token)`

**Params**

- `map` **{dict}**: [Map](concepts/map_definition.md)
- `token` **{string}**: TheMap token

**Returns**: `map` **{dict}** Updated map dict


## upload_image

It takes the local image file and upload it to themap server so that uploaded image can be used in different APIs.

**Signature**: `upload_image(local_path,token)`

**Params**

- `local_path` **{string}**: Image file path
- `token` **{string}**: TheMap token

**Returns**: `url` **{string}** Uploaded image url

## get_cities

It retrives all locations TheMap has support for

**Signature**: `get_cities()`

**Returns**: `cities` **{array}** Array containing all the cities

## filter_outliers

It take data and perform outlier analysis on it. After analysis it will return new data excluding outliers.

**Signature**: `filter_outliers(data,value_fn,threshold=1.5)`

**Params**

- `data` **{array}**: Array of data to be filtered
- `value_fn` **{lamda function}**: Lamda function which will be called for each item in data and returns the value on which numerical analysis should be performed.
- `threshold` **{number}**: Threshold number which can later the range to make outlier more stricter/looser.

**Returns**: `filtered_data` **{array}** Filtered data excluding outliers

## color_fader

It interpolate the color scale and provide the color representing given value.

**Signature**: `color_fader(c1,c2,mix=0)`

**Params**

- `c1` **{string}**: Color1 hex which is set as start of scale i.e. `0`
- `c2` **{string}**: Color2 hex which is set as end of color scale i.e. `1`
- `mix` **{number}**: value based on which color will be returned from generated scale. Value must be between `0` and `1`.

**Returns**: `color` **{string}** Hex color represeting given `mix` value
