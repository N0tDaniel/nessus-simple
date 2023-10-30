import requests
from requests.exceptions import SSLError
import time

scan_number = input("Inserisci il numero della scansione: ")

# Specifica il percorso completo di destinazione del file
file_path = "C:\\Users\\dan\\Desktop\\Nessus Code\\Scarica Scan .nessus\\Step 1,2,3\\risultato.nessus"

url = f"https://192.168.1.37:8834/scans/{scan_number}/export"
access_key = "a884f7c0459ff6d9aa883002895172ecf64661b4d2ab30abbbf4c3ba5a5132ef"
secret_key = "99b83d7d206cf4afa3fc6d9f8b4024b0542810099253cda5e939323ece814619"

payload = {"format": "nessus"}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.post(url, json=payload, headers=headers, verify=False)
response_data = response.json()
file_id = response_data["file"]

print("Print del Token e dell'id del file, attendi alcuni secondi per lo step di Check")
print(response.text)
print("File non ancora pronto")

time.sleep(60)  # Pausa necessaria 60s

url = f"https://192.168.1.37:8834/scans/{scan_number}/export/{file_id}/status"

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}

response = requests.get(url, headers=headers, verify=False)

print(response.text)
print("In caso di errore (error) controlla lo spazio presente sulla macchina")

time.sleep(20)  # Pausa necessaria 20s
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
