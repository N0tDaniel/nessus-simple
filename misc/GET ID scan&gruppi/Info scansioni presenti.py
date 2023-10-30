import requests
import json
from requests.exceptions import SSLError

url = "https://192.168.1.37:8834/scans/"
access_key = ""
secret_key = ""

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
