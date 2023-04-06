import requests
import json

# set the date
d = "2023-02-06"

# call the api
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={d}&end_date={d}&api_key=DEMO_KEY"
ret = requests.get(url)
# print(ret.status_code)

# extract the json
retdata = ret.content.decode("utf-8")
print(retdata)
jsondata = json.loads(retdata)

# how many asteroids are near earth today?
elementcount = jsondata["element_count"]
print(f"{elementcount} asteroids near earth today...")

# check to see if any of the asteroids are hazardous
for object in jsondata["near_earth_objects"][d]:
    # print(object)
    name = object["name"]
    hazardous = object["is_potentially_hazardous_asteroid"]
    print(f"Object {name} : hazardous? {hazardous}")