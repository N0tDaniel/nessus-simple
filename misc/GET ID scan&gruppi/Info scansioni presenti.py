import requests
import json
from requests.exceptions import SSLError

url = "https://192.168.1.37:8834/scans/"
access_key = "a884f7c0459ff6d9aa883002895172ecf64661b4d2ab30abbbf4c3ba5a5132ef"
secret_key = "99b83d7d206cf4afa3fc6d9f8b4024b0542810099253cda5e939323ece814619"

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.get(url, headers=headers, verify=False)


data = json.loads(response.text)

# ordine in base al nome dello scan
sorted_output = {
    "folders": sorted(data["folders"], key=lambda x: x["name"]),
    "scans": sorted(data["scans"], key=lambda x: x["name"]),
    "timestamp": data["timestamp"]
}

# print output ordinato
print(json.dumps(sorted_output, indent=4))