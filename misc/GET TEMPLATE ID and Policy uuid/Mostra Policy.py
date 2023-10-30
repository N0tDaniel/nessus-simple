import requests
import json
from requests.exceptions import SSLError

url = "https://ip:8834/policies"
access_key = ""
secret_key = ""

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.get(url, headers=headers, verify=False)

json_data = json.loads(response.text)
formatted_response = json.dumps(json_data, indent=4, sort_keys=True)

print(formatted_response)
