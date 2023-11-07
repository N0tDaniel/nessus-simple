import requests
import csv
from requests.exceptions import SSLError

scan_number = input("Inserisci il numero della scansione: ")
url = f"https://nessusip:8834/scans/{scan_number}"
access_key = ""
secret_key = ""

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
