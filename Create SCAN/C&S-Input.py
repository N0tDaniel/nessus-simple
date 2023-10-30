import requests
import csv
import json
from datetime import datetime
from requests.exceptions import SSLError

url = "https://192.168.1.37:8834/scans"
access_key = "a884f7c0459ff6d9aa883002895172ecf64661b4d2ab30abbbf4c3ba5a5132ef"
secret_key = "99b83d7d206cf4afa3fc6d9f8b4024b0542810099253cda5e939323ece814619"


targets = []
with open('file.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        targets.append(row[0])

text_targets = ",".join(targets)


name = input("Inserisci il nome: ")
description = input("Inserisci la descrizione: ")
policy_id = input("Inserisci la policy ID: ")
folder_id = input("Inserisci il folder ID: ")

starttime_input = input("Inserisci lo starttime (formato: yyyy-mm-dd HH:MM:SS): ")
starttime = datetime.strptime(starttime_input, "%Y-%m-%d %H:%M:%S").strftime("%Y%m%dT%H%M%S")

payload = {
    "settings": {
        "enabled": True,
        "name": name,
        "description": description,
        "policy_id": int(policy_id),
        "folder_id": int(folder_id),
        "launch": "ON_DEMAND",
        "starttime": starttime,
        "timezone": "Europe/Berlin",
        "text_targets": text_targets,
        "rrules": "1"
    },
    "uuid": "ab4bacd2-05f6-425c-9d79-3ba3940ad1c24e51e1f403febe40"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.post(url, json=payload, headers=headers, verify=False)


json_data = json.loads(response.text)
formatted_response = json.dumps(json_data, indent=4, sort_keys=True)
print(formatted_response)
