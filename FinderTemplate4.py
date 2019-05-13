#This code fetches the necessary modules

import re
import requests

#This code gets a blob of text from the target website

page = requests.get("https://www.thomasparksolutions.com").text

#This code fetches strings that begin and end as requested, and rebuilds them into a list, and prints it

found = []
final = []

m = re.findall('http(.+?)mp3', page)
if m:
    result = tuple(m[x:x+1] for x in range(0, len(m), 1))
    for elem in result:
        elem2 = str(elem)
        elem3 = elem2[2:-2]
        elem4 = "http" + elem3 + "mp3"
        final.append(elem4)

print(final)
