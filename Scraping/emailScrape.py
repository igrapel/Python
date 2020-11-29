import re
import requests
page = requests.get('https://www.dlapiper.com/en/us/locations/los-angeles-century-city/?tab=lawyers')
html_contents = page.text
print(html_contents)
#Define the regular expression
regex = re.compile(r'[\w.-]+@[\w.-]+')

#Compile using the regular expression
email = re.findall(regex, html_contents)

#Display the email addresses in an list
print(email)

