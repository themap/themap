# Map functions

All the map functions are packed inside map modole. e.g. `themap.map.create_map`

## create_map

It creates new map on TheMap platform.

**Signature**: `create_map(tourmap,token)`

**Params**

- `tourmap` **{dict}**: [map dict](concepts/map_definition.md#object-schema)
- `token` **{string}**: auth token

**Returns**: `map` **{dict}** server map dict

## get_map

It retrives existing map using its handle.

**Signature**: `get_map(handle,token)`

**Params**

- `handle` **{string}**: Handle of the map to be retrived
- `token` **{string}**: auth token

**Returns**: `map` **{dict}** server [map dict](concepts/map_definition.md#object-schema)

## search_map

It searches TheMap platform and provides list of maps matching search criteria.

**Signature**: `search_map(search_key,token,take = 20,skip = 0)`

**Params**

- `search_key` **{string}**: Search keyword
- `token` **{string}**: auth token
- `take` **{number}**: Specifies how many maps to retrive
- `skip` **{number}**: Specifies how may maps to skip before retriving (helps with pagination).

**Returns**: `maps` **{array}** list of maps

## create_layer

It updates existing map with provided fields

**Signature**: `update_map(tourmap,token)`

**Params**

- `tourmap` **{dict}**: [map dict](concepts/map_definition.md#object-schema) with `ID` as required field
- `token` **{string}**: auth token

**Returns**: `map` **{dict}** updated server map dict

## get_all_features

It retrives all the features of specific map.

**Signature**: `get_all_features(map_id,token)`

**Params**

- `map_id` **{number}**: ID of the map
- `token` **{string}**: auth token

**Returns**: `features` **{array}** list of all the features

## delete_map

It deletes the map.

**Signature**: `delete_map(id,token)`

**Params**

- `id` **{number}**: id of the map to be deleted
- `token` **{string}**: auth token