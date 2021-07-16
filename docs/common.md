# Common functions

All the common functions are packed inside common modole. e.g. `themap.common.get_token`

## init_session

It take credentials of user and generate the API token using which further API communication can be authorized

**Signature**: `init_session(username=None,password=None)`

**Params**

- `username` **{string}**: TheMap username
- `password` **{string}**: TheMap password

**Returns**: `token` **{string}** API token

## upload_image

It takes the local image file and upload it to themap server so that uploaded image can be used in different APIs.

**Signature**: `upload_image(local_path)`

**Params**

- `local_path` **{string}**: Image file path

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

## generate_feature_html

It takes input template and generate html which can be used further as feature content.

**Signature**: `generate_feature_html(template)`

**Params**

- `template` **{array}**: [template](concepts/feature_content_template.md) of the feature content.

**Returns**: `html` **{string}** generated html content based on
