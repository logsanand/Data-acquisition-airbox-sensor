from sys import argv
from os.path import exists
import simplejson as json
import requests
import os

dataDirectory=r''
os.chdir(dataDirectory)                             # change the directory path
url = 'http://data.aireas.com/api/v2/locations'     # get the location of airbox url
response = requests.request('GET', url)
jsonObj2 = json.loads(response.text)                # convert text response into a dictionary
with open('loc.json', 'w') as jsonfile:             #store to JSON file
    json.dump(jsonObj2, jsonfile)
file=open('loc.json', 'r')                          # open the file
data = json.loads(file.read())
# convert to GEOJSON file
geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [d["gps"]["lon"], d["gps"]["lat"]],              # Separate the coordinates
            },
        "properties" :
            {
                "city":d["city"],"oid":d["_id"]["$oid"],"lon":d["gps"]["lon"],"lat":d["gps"]["lat"],"id2":d["_id"]      # sort the attributes
            }
     } for d in data]
}

print(json.dumps(geojson))
with open('loc1.json', 'w') as outfile:             # store into JSON file
    json.dump(geojson,outfile,indent=4, sort_keys=True)
