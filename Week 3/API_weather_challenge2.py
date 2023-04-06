import requests
import json

url = "https://api.openweathermap.org/data/2.5/weather?lat=35.6762&lon=139.6503&appid=4ae259d943afdda4f1b4fe60fa63a676"

countries = {
    "Dubai" : {
        "lat" : 25.2048,
        "long" : 55.2708
    },
    "Riyadh" : {
        "lat" : 24.7136,
        "long" : 46.6753
    },
    "Lusaka" : {
        "lat" : -15.3875,
        "long" : 28.3228
    },
    "Tokyo" : {
        "lat" : 35.6762,
        "long" : 139.6503
    },
    "Melbourne" : {
        "lat" : -37.8136,
        "long" : 144.9631
    },
    "Seattle" : {
        "lat" : 47.6062,
        "long" : -122.3321
    },
    "Buenos_Aires" : {
        "lat" : -34.6037,
        "long" : -58.3816
    }
}



for temps in countries:
    temp_country = j["main"]["temp"]
    print(temp_tokyo)
    temp_ct = float(temp_tokyo) - 273.15
    print(f"Temperature in Tokyo is {temp_ct} Celsius")