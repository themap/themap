# Map defination

Map object is container object representing one map on TheMap platform.

## Object Schema
    {
        "Title": "Sample Map",
        "Description": "This is cool!",
        "Logo": "https"://url.to/imge.jpg",
        "Handle": "sample-map-handle",
        "Is3D": false,
        "IsListed": true,
        "LayerHasContent": false,
        "MapStyle": null,
        "NE": [33.0133900, -96.056056],
        "SW": [32.4554055, -97.432789],
        "Tags": null,
        "WebsiteUrl": null
        "EditPermissionType": 0,
        "ViewPermissionType": 2,
    }

## Explanation

* `Title` - Title of the map
* `Description` - Description of the map
* `Logo` - Logo of the map
* `Handle` - Every map must have unique handle. This handle is something provides unique url to map as well. e.g. `https://themap.net/maps/view/your-handle-here`
* `Is3D` - Boolean deciding whether TheMap should be rendered as 3D or 2D.
* `IsListed` - If True, map will be listed on TheMap publically and also visible in search
* `LayerHasContent` - If True, layers will switch to presentation mode while rendering and thus will appear one by one based on input directions.
* `MapStyle` - Base layer style of the map. Possible values : `basic`,`streets`,`outdoors`,`light`,`dark` or `satellite-streets`
* `NE` - latitude/longitude pair representing North East point of map bounds. It's optional to provide this. If not provided. TheMap will calculate the bounds and decide right dispaly view automatically. Use this along with `SW` only if you want to override the map view.
* `SW` - latitude/longitude pair representing South West point of map bounds
* `Tags` - Comma seprated tags to assign for the map
* `WebsiteUrl` - In case you want to provide link to the source of data for reference/credits
* `EditPermissionType` - Flag controlling who can edit the map. Possible values : 
    * `0` - Only creator can edit
    * `2` - Anyone having link can edit
    * `3` = Everyone can edit
* `ViewPermissionType` - Flag controlling who can edit the map. Possible values : 
    * `0` - Only creator can view,
    * `2` - Anyone having link can view, 
    * `3` - Everyone can view