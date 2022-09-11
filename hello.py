from tkinter import Y
import requests
import json
from datetime import date

response = requests.get("http://www.energiatodistusrekisteri.fi/api/public/laatijat")
laatijat = response.json()

# Serializing json
json_object = json.dumps(laatijat, indent=4)
 
# Writing to laatijat-date.json
today = date.today()
with open(f'laatijat-{today}.json', "w") as file:
    file.write(json_object)


# Construct lists of emails
json1 = "laatijat-2022-09-10.json"
json2 = "laatijat-2022-09-11.json"

with open(json1) as jsonFile:
    data = json.load(jsonFile)
    for email in data:
        print(email)
    # print(data[0]["email"])

