#This code imports the modules

import re
import requests

#This code retrieves a blob of text from the remote target

page = requests.get("http://www.thomasparksolutions.com").text

#This code makes a list of the substrings sought
#Replace the string Python with your desired regex
results = re.findall('(Thomas)',page)

#This code prints the result(s)

for i in results:
    print (i)

