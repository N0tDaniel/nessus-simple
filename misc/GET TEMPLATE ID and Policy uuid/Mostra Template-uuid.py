import requests
import json
from requests.exceptions import SSLError

url = "https://172.25.196.32:8834/editor/scan/templates"  # Modifica "scan" con "policy" per visionare le policy
access_key = "9d507eb6b90e1288ff7a9de6ebc54ccc7c339a813d55597c6bcbccd44409fc89"
secret_key = "5e04b96e748e6f6b5c1c2b8df5231f7b67d9f323fadec19beebcef9897f2cd88"

headers = {
    "accept": "application/json",
    "X-ApiKeys": f"accessKey={access_key};secretKey={secret_key}"
}
response = requests.get(url, headers=headers, verify=False)

# Carica la risposta come oggetto JSON
json_data = json.loads(response.text)

# Rimuovi 'icon' dalla struttura dati JSON
def remove_icon(template):
    if 'icon' in template:
        del template['icon']

# Rimuovi 'icon' da ogni template nella lista 'templates'
if 'templates' in json_data and isinstance(json_data['templates'], list):
    for template in json_data['templates']:
        remove_icon(template)

# Converti la risposta ordinata come stringa JSON con indentazione
sorted_response = json.dumps(json_data, indent=4, sort_keys=True)

print(sorted_response)

# Opzione di ricerca
search_term = input("Inserisci il termine di ricerca: ")
search_results = []

# Effettua la ricerca nell'output
if search_term:
    for template in json_data['templates']:
        if search_term.lower() in json.dumps(template).lower():
            search_results.append(template)

    # Stampa i risultati della ricerca
    if search_results:
        print(f"\nRisultati della ricerca per '{search_term}':")
        for result in search_results:
            print(json.dumps(result, indent=4))
    else:
        print(f"\nNessun risultato trovato per '{search_term}'.")

