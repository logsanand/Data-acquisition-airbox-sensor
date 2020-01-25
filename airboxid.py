import requests
import cbsodata
import json
import csv
url = 'http://data.aireas.com/api/v2/airboxes'          # Get the airbox data url
response = requests.request('GET', url)
jsonObj1 = json.loads(response.text)                     # convert text response into a dictionary
with open('airboxid.json', 'w') as jsonfile:                #store it as json file
    json.dump(jsonObj1, jsonfile)
file=open('airboxid.json', 'r')                         # read the json file
data = json.loads(file.read())
# Convert the JSON to Geojson file
# separate the coordinates and the attributes needed
geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["last_measurement"]["calibrated"]["readings"]["GPS"]["lat"], d["last_measurement"]["calibrated"]["readings"]["GPS"]["lon"]],
            },
        "properties" :
            {
                "date":d["last_measurement"]["calibrated"]["when"]["$date"],"AmbHum":d["last_measurement"]["calibrated"]["readings"]["AmbHum"],
             "PM1":d["last_measurement"]["calibrated"]["readings"]["PM1"],"WBGT":d.get(("last_measurement","WBGT"),'null'),"UFP":d.get(("last_measurement","UFP"),'null'),
             "PM25":d["last_measurement"]["calibrated"]["readings"]["PM25"],
             "Ozon": d["last_measurement"]["calibrated"]["readings"]["Ozon"],"PM10":d["last_measurement"]["calibrated"]["readings"]["PM10"],
             "Temp": d["last_measurement"]["calibrated"]["readings"]["Temp"],"RelHum":d["last_measurement"]["calibrated"]["readings"]["RelHum"],
             "AmbTemp": d["last_measurement"]["calibrated"]["readings"]["AmbTemp"],"NO2":d["last_measurement"]["calibrated"]["readings"]["NO2"],
             "ID": d["_id"],"location":d.get(("location"),'null')
            }
     } for d in data]      # Run over the json file and store it into separate values
}

print(json.dumps(geojson))
with open('airid_1.json', 'w') as outfile:                  # store as a json file
    json.dump(geojson,outfile,indent=4, sort_keys=True)
