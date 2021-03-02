import re
import json
from urllib.request import urlopen
import time

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

start = time.time()

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('Your IP detail\n ')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))


key = ""
while(key != "q"):
    key = input("Thanks for visiting. Press q when you are done.")

end = time.time()
duration = end-start
print("You were in our city for " + str(round(duration, 1)) + " seconds")
