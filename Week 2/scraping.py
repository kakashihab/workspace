#----------TASK 1 and 2 --------#

import requests
from bs4 import BeautifulSoup

f = open("Week 2\wats.txt")

url = "http://35.178.198.206/scarlet1.html"


res = requests.get(url)

html = res.content.decode("utf-8")
soup = BeautifulSoup(html, features="html.parser")

watsons = soup.find_all("span", {"class" : "watson"})
print(watsons)
for item in watsons:
    print(item.get_text())


#----------TASK 3--------------#

url1 = "http://35.178.198.206/bigpictures.html"

res = requests.get(url1)

links = soup.find_all("a")
#print(links)
for link in links:
    print(f"{link} : {link.get_text()} : {link.attrs['href']}")