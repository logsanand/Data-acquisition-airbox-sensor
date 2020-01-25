import requests
import os
import json
import simplejson as json1
dataDirectory=r''
os.chdir(dataDirectory)
data=[]         # create an empty list
# use for loop to run over the air box data
for i in range(1,40):
    a=str(i)
    items = ["http://data.aireas.com/api/v2/airboxes/history/", a, '/1475280000/1477872000']
    url1 = "/".join([(u.strip("/") if index + 1 < len(items) else u.lstrip("/")) for index, u in enumerate(items)])
    response = requests.request('GET', url1)
    jsonObj1 = json.loads(response.text) # convert text response into a dictionary
    data.append(jsonObj1)               # add the data into a list
with open('airboxfull.json', 'w') as jsonfile:      #store as a json file
    json.dump(data, jsonfile)
file=open('airboxfull.json', 'r')
data1 = json1.loads(file.read())                    # open the json file and store it as GeoJson
# separate the coordinates and the required attributes
feas=[
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["readings_calibrated"]["GPS"]["lon"], d["readings_calibrated"]["GPS"]["lat"]],
            },
        "properties" :
            {"airbox_id":d["airbox_id"],"date1":d["when"]["measured"]["$date"],"AmbHum":d["readings_calibrated"]["AmbHum"],
             "PM1":d["readings_calibrated"]["PM1"],"UFP":d["readings_calibrated"]["UFP"],
             "PM25":d["readings_calibrated"]["PM25"],
             "Ozon": d["readings_calibrated"]["Ozon"],"PM10":d["readings_calibrated"]["PM10"],
             "Temp": d["readings_calibrated"]["Temp"],"RelHum":d["readings_calibrated"]["RelHum"],
             "AmbTemp": d["readings_calibrated"]["AmbTemp"],"NO2":d["readings_calibrated"]["NO2"],
             }
     }
    for c in data1
    for d in c                   # Run over the json file and store it into separate values
    ]
geojson = {
    "type": "FeatureCollection",
    "features": feas
}

with open('air_fin1.json', 'w') as outfile:                 # store into a new JSON file
    json1.dump(geojson,outfile,indent=4, sort_keys=True)
