# Map functions

All the map level functions/classes are packed inside map module. e.g. `themap.map.create_map`

## create_map

It creates new map on TheMap platform.

**Signature**: `create_map(map_options)`

**Params**

- `map_options` [**{dict}**](concepts/map_options.md#object-schema) : Options to create map

**Returns**: `map` [**{object}**](objects/map.md)

## get_map

It retrives existing map using its handle.

**Signature**: `get_map(handle)`

**Params**

- `handle` **{string}**: Handle of the map to be retrived

**Returns**: `map` [**{object}**](objects/map.md)

## search_map

It searches TheMap platform and provides list of maps matching search criteria.

**Signature**: `search_map(search_key,take = 20,skip = 0)`

**Params**

- `search_key` **{string}**: Search keyword
- `take` **{number}**: Specifies how many maps to retrive
- `skip` **{number}**: Specifies how may maps to skip before retriving (helps with pagination).

**Returns**: `maps` **{array}** of [map](objects/map.md)