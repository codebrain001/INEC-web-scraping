### MESH MEDIA LAB
### PROGRAMMER: CODE_BRAIN
### PROJECT: INEC WEB SCRAPING

### Imorting important Packages
import html.parser
import requests
from bs4 import BeautifulSoup

payload = {"data[Voter][state_id]": "your state", "data[Voter][last_name]": "your last name",
           "data[Voter][vin]": "your VIN number"}
### Payload is our required input needed for authentication on the INEC site

### Development of the required inputs
state = int(input("enter state: "))
payload["data[Voter][state_id]"] = state
### The state are arranged in alphabetical order and number (e.g ABIA = 1)

name = input("enter last name: ")
payload["data[Voter][last_name]"] = name

Vin = input("Enter you Voter Identifiacation Number: ")
payload["data[Voter][vin]"] = Vin
payload["data[Voter][search_mode]"] = "vin"
r = requests.post("https://voters.inecnigeria.org/#statusViaVin", data=payload)
# print(r.text)


### Intitializing the Web Scrapping tool
soup = BeautifulSoup(r.text, "html.parser")

# print(soup.table)
# print(soup.table.find_all("td"))


### Looping through the desired output
for info in soup.table.find_all("td"):
    print(info.string)

### JSON Session
import json

json_string = json.dumps(info.string)
print(json_string)
json_string = json
