import requests
import cbsodata
import json
import csv

# The url to get the road data using the bounding box coordinates of RD_new system
url = 'https://geodata.nationaalgeoregister.nl/nwbwegen/wfs?service=wfs&version=2.0.0&request=GetFeature&outputFormat=json&typeNames=nbwwegen:wegvakken&srsName=urn:ogc:def:crs:EPSG::28992&bbox=149684.148,391924.645,172544.197,371392.938'
response = requests.request('GET', url)
jsonObj = json.loads(response.text) # convert text response into a dictionary
with open('roads_eindoven.json', 'w') as jsonfile:      # store in a json file
    json.dump(jsonObj, jsonfile)
print("over")