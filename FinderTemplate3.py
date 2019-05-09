import re
import requests

page = requests.get("http://www.thomasparksolutions.com").text

# Replace the string Python with your desired regex

found = []

m = re.findall('http(.+?)com', page)
if m:
    found.append(m)

print(found)
