import shutil
import requests
import json

# call the apod api
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
ret = requests.get(url)
# print(ret.status_code)
# print(ret.content)
jsondata = json.loads(ret.content.decode("utf-8"))
# print(jsondata)

# print some of the text data from the response
print(jsondata["title"])
print(jsondata["explanation"])

# get the url of the picture
picurl = jsondata["url"]
print(picurl)

# get the picture
ret = requests.get(picurl, stream=True)
outfile = open(f"apod.jpg", "wb")
shutil.copyfileobj(ret.raw, outfile)
outfile.close()