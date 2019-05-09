import re
import requests

page = requests.get("http://www.thomasparksolutions.com").text

# Replace the string Python with your desired regex

found = []
final = []

m = re.findall('http(.+?)com', page)
if m:
    result = tuple(m[x:x+1] for x in range(0, len(m), 1))
    for elem in result:
        elem2 = str(elem)
        elem3 = elem2[2:-2]
        elem4 = "http" + elem3 + "com"
        final.append(elem4)

print(final)
