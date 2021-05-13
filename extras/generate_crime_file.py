import requests
import json

def generate_crime_file(start,end,path):
    query = "reporteddate>='"+str(start)+"' AND reporteddate<'"+str(end)+"'"
    print(query)
    payload = {
        "$where" : query
    }
    r = requests.get('https://www.dallasopendata.com/resource/qv6i-rri7.json',params=payload)
    data = r.json()
    geojson = {
        "type": "FeatureCollection",
        "features" : []
    }
    for item in data:
        if("latitude" in item["geocoded_column"]):
            feature = {
                "type" : "Feature",
                "properties" : {
                    "division" : item["division"] if "division" in item else None,
                    "date1" : item["date1"] if "date1" in item else None,
                    "time1" : item["time1"] if "time1" in item else None,
                    "day1" : item["day1"] if "day1" in item else None,
                    "premise" : item["premise"] if "premise" in item else None,
                    "offincident" : item["offincident"] if "offincident" in item else None,
                    "signal" : item["signal"] if "signal" in item else None,
                    "incident_address" : item["incident_address"],
                    "ro1name" : item["ro1name"] if "ro1name" in item else None,
                    "nibrs_crime_category" : item["nibrs_crime_category"],
                    "nibrs_crime" : item["nibrs_crime"] if "nibrs_crime" in item else None,
                    "zip_code" : item["zip_code"] if "zip_code" in item else None,
                    "mo" : item["mo"] if "mo" in item else None,
                    "hatecrimedescriptn" : item["hatecrimedescriptn"],
                    "drug" : item["drug"] if "drug" in item else None,
                    "victimtype" : item["victimtype"] if "victimtype" in item else None,
                    "compname" : item["compname"] if "compname" in item else None,
                },
                "geometry" : {
                    "type" : "Point",
                    "coordinates" : [float(item["geocoded_column"]["longitude"]),float(item["geocoded_column"]["latitude"])]
                }
            }
            geojson["features"].append(feature)
    with open(path, 'w') as json_file:
        json.dump(geojson, json_file)
