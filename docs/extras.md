# Extras functions

All the miscellaneous functions are packed inside extras modole. e.g. `themap.extras.generate_crime_file`

## generate_crime_file

It fetches [crime data](https://www.dallasopendata.com/resource/qv6i-rri7.json) from Dallas Open Data portal and generate geoJSON file from it.

**Signature**: `generate_crime_file(start,end,path)`

**Params**

- `start` **{date}**: Start date to filter the data
- `end` **{date}**: End date to filter the data
- `path` **{string}**: Path of the geoJSON file to be generated
