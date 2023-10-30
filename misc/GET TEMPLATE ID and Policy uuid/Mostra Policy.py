import requests
import json
from requests.exceptions import SSLError

url = "https://172.25.196.32:8834/policies"
access_key = "9d507eb6b90e1288ff7a9de6ebc54ccc7c339a813d55597c6bcbccd44409fc89"
secret_key = "5e04b96e748e6f6b5c1c2b8df5231f7b67d9f323fadec19beebcef9897f2cd88"

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.get(url, headers=headers, verify=False)

json_data = json.loads(response.text)
formatted_response = json.dumps(json_data, indent=4, sort_keys=True)

print(formatted_response)
