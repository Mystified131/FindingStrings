#This code imports the necessary modules

import re
import requests

#This code gets a blob of text from the webpage target

page = requests.get("http://www.thomasparksolutions.com").text

#This code finds substrings that begin and end as mentioned, and prints them

found = []

m = re.findall('http(.+?)com', page)
if m:
    found.append(m)

print(found)
