import requests
import json

#url = "http://127.0.0.1:800/cube?n=5"

url = "http://20.0.207.104:8000/cube?n=5"

res = requests.get(url)

print(res.content.decode("utf-8"))