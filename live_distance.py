import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)
str = " "

for i in data:
    if (i == 'city' or i == 'region' or i == 'country' or i == 'loc'):
        str = str+' '+data[i]
print(str)
