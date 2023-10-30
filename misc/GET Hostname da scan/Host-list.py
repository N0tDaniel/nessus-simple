import requests
import csv
from requests.exceptions import SSLError

scan_number = input("Inserisci il numero della scansione: ")
url = f"https://192.168.1.37:8834/scans/{scan_number}"
access_key = "a884f7c0459ff6d9aa883002895172ecf64661b4d2ab30abbbf4c3ba5a5132ef"
secret_key = "99b83d7d206cf4afa3fc6d9f8b4024b0542810099253cda5e939323ece814619"

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}


try:
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()

    data = response.json()

   
    if response.status_code == 200:
        asset_list = data["hosts"]

        # Salvataggio come file CSV
        file_path = "asset_list.csv"
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Hostname"])  
            for asset in asset_list:
                hostname = asset["hostname"]
                writer.writerow([hostname])

        print(f"File CSV salvato correttamente: {file_path}")
    else:
        print("Errore durante la richiesta degli hostname.")
except requests.exceptions.RequestException as e:
    print(f"Errore durante la richiesta: {e}")
except SSLError as e:
    print(f"Errore SSL: {e}")
