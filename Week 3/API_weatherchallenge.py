import requests
import json

temps_recorded = {"Dubai":"temp", "Riyadh":"temp2", "Lusaka":"temp3"}

url_dubai = "https://api.openweathermap.org/data/2.5/weather?lat=25.2048&lon=55.2708&appid=80c930c817f54a033a6aedfac1aaa0fa"
url_riyadh = "https://api.openweathermap.org/data/2.5/weather?lat=24.7136&lon=46.6753&appid=80c930c817f54a033a6aedfac1aaa0fa"
url_lusaka = "https://api.openweathermap.org/data/2.5/weather?lat=15.3875&lon=28.3228&appid=80c930c817f54a033a6aedfac1aaa0fa"
url_tokyo = "https://api.openweathermap.org/data/2.5/weather?lat=35.6762&lon=139.6503&appid=80c930c817f54a033a6aedfac1aaa0fa"
url_melbourne = "https://api.openweathermap.org/data/2.5/weather?lat=37.8136&lon=144.9631&appid=80c930c817f54a033a6aedfac1aaa0fa"

res = requests.get(url_dubai)
res2 = requests.get(url_riyadh)
res3 = requests.get(url_lusaka)
res4 = requests.get(url_tokyo)
res5 = requests.get(url_melbourne)

rs = res.content.decode("utf-8")
rs2 = res2.content.decode("utf-8")
rs3 = res3.content.decode("utf-8")
rs4 = res4.content.decode("utf-8")
rs5 = res5.content.decode("utf-8")

jd = json.loads(rs)
jr = json.loads(rs2)
jl = json.loads(rs3)
jt = json.loads(rs4)
jm = json.loads(rs5)


#dubai temp
temp_dubai = jd["main"]["temp"]
temp_cd = float(temp_dubai) - 273.15
print(f"Temperature in Dubai is {temp_cd} Celsius")

#Riyadh temp
temp_riyadh = jr["main"]["temp"]
temp_cr = float(temp_riyadh) - 273.15
print(f"Temperature in Riyadh is {temp_cr} Celsius")

#Lusaka temp
temp_lusaka = jl["main"]["temp"]
temp_cl = float(temp_lusaka) - 273.15
print(f"Temperature in Lusaka is {temp_cl} Celsius")

#Tokyo temp
temp_tokyo = jt["main"]["temp"]
temp_ct = float(temp_tokyo) - 273.15
print(f"Temperature in Tokyo is {temp_ct} Celsius")

#Melbourne
temp_melbourne = jm["main"]["temp"]
temp_cm = float(temp_melbourne) - 273.15
print(f"Temperature in Melbourne is {temp_cm} Celsius")

