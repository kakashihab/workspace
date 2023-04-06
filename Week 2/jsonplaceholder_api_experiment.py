import requests
import json

# set the url of the service
url = "https://jsonplaceholder.typicode.com/posts?userId=4"

# call the service
res = requests.get(url)
print(res.status_code)

# display the headers of the response
# all the headers
print(res.headers)
# or a single header
print(res.headers["Content-Type"])

# get the contents from the response
# this is returned as a string
s = res.content.decode("utf-8")

# turn the string into a list using json.loads
posts = json.loads(s)
print(posts)

# loop through the list, show the title of each post
for post in posts:
    print(post["title"])