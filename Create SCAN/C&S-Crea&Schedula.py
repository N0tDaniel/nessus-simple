import requests
import csv
import json
from requests.exceptions import SSLError

url = "https://172.25.196.32:8834/#/scans"
access_key = "9d507eb6b90e1288ff7a9de6ebc54ccc7c339a813d55597c6bcbccd44409fc89"
secret_key = "5e04b96e748e6f6b5c1c2b8df5231f7b67d9f323fadec19beebcef9897f2cd88"

# Leggi i target dal file CSV
targets = []
with open('file.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        targets.append(row[0])

text_targets = ",".join(targets)


payload = {
    "settings": {
        "enabled": True,
        "name": "Network Scan",
        "description": "First Network Scan",
        "policy_id": 21,
        "folder_id": 1236,
        "launch": "ON_DEMAND",
        "starttime": "20230628T152500",
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

# Carica la risposta come oggetto JSON
json_data = json.loads(response.text)
formatted_response = json.dumps(json_data, indent=4, sort_keys=True)
print(formatted_response)