#This code retrieves the modules

import re
import requests

#This code fetches a blob of text from the web target

page = requests.get("http://www.thomasparksolutions.com").text

#This code finds all substrings starting with the first snippet, and ending with the second
#Replace the string with your desired regex, and prints the result(s)

found = []

m = re.search('Th(.+?)mas', page)
if m:
    found.append(m)

print(found)
