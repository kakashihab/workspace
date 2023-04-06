import requests
import shutil
import random

# get 10 pictures of kittens
for i in range(10):
    # generate a random size for the picture
    x = random.randint(300, 800)
    y = random.randint(300, 800)
    print(x, y)

    # call the service with the random size
    url = f"http://placekitten.com/{x}/{y}"
    res = requests.get(url, stream=True)
    print(res.status_code)

    # save the "file-like object" in memory to disk using the shutil library
    outfile = open(f"kitten{i}.png", "wb")
    shutil.copyfileobj(res.raw, outfile)
    outfile.close()


# more info about saving binary data from services...
# https://docs.python-requests.org/en/latest/user/quickstart/#binary-response-content
# https://docs.python-requests.org/en/latest/user/quickstart/#raw-response-content