import requests
from requests.exceptions import SSLError
import time

scan_number = input("Inserisci il numero della scansione: ")
file_path = input("Inserisci il percorso completo di destinazione del file (es. /path/risultato.nessus): ")

url = f"https://192.168.1.37:8834/scans/{scan_number}/export"
access_key = ""
secret_key = ""

payload = {"format": "nessus"}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.post(url, json=payload, headers=headers, verify=False)
response_data = response.json()
file_id = response_data["file"]

print("Print del Token e dell'id del file, attendi acuni secondi per lo step di Check")
print(response.text)
print("File non anora pronto")

time.sleep(60)  # Pausa necessaria 60s

url = f"https://192.168.1.37:8834/scans/{scan_number}/export/{file_id}/status"

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.get(url, headers=headers, verify=False)

print(response.text)
print("in caso di errore (error) controlla lo spazio presente sulla macchina ")

time.sleep(60)  # Pausa necessaria 60s
url = f"https://192.168.1.37:8834/scans/{scan_number}/export/{file_id}/download"

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.get(url, headers=headers, verify=False)

# Salva la response come .nessus nel percorso specificato
with open(file_path, "wb") as file:
    file.write(response.content)

print(f"Scan salvato come {file_path}")
