import re
import requests

page = requests.get("http://www.thomasparksolutions.com").text

# Replace the string Python with your desired regex
results = re.findall('(Thomas)',page)

for i in results:
    print (i)

