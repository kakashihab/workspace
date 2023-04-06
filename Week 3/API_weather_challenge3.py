import requests
import json

# create a url
url = "https://api.openweathermap.org/data/2.5/weather?lat=25.2048&lon=55.2708&appid=4ae259d943afdda4f1b4fe60fa63a676"

# call the api
res = requests.get(url)
print(res.status_code)

# extract the contents from the response
s = res.content.decode("utf-8")
print(s)
print("----------")

# jsonify the returned contents
j = json.loads(s)
print(j)
print("----------")

# extract the temperature from the response
temp = j["main"]["temp"]
print(temp)
temp_c = float(temp) - 273.15
print(f"Temperature in Dubai is {temp_c} Celsius")