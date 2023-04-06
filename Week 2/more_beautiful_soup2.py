import requests
from bs4 import BeautifulSoup
import os
 
url = "http://35.178.198.206/bigpictures.html"

def imagedown(url, folder):
    try: 
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass

    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    html = r.content.decode("utf-8")
    soup = BeautifulSoup(html, features="html.parser")
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('writing: ', name)

imagedown('http://35.178.198.206/bigpictures.html')




