import json
import requests

def main():
    # Lese die Daten aus der Datei allmakes.json
    with open('allmakes.json', 'r') as file:
        data = json.load(file)
    
    # Liste für alle Responses
    all_responses = []

    # Iteriere über alle Make_IDs
    for make in data['Results']:
        make_id = make['Make_ID']
        make_name = make['Make_Name']
        url = f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/{make_id}?format=json"
        
        # HTTP-GET-Anfrage an die API senden
        response = requests.get(url)
        
        # Überprüfe den Statuscode der Antwort
        if response.status_code == 200:
            try:
                # Versuche, die Antwort als JSON zu parsen
                response_json = response.json()
            except json.JSONDecodeError:
                print(f"Invalid JSON response for Make_ID: {make_id}")
                continue

            # Füge die Response zur Liste hinzu
            all_responses.append({
                "Make_ID": make_id,
                "Make_Name": make_name,
                "Response": response_json
            })

            # Drucke den Make_Name bei Erfolg
            print(f"Successfully fetched data for Make_ID: {make_id}, Make_Name: {make_name}")
        else:
            print(f"Failed to fetch data for Make_ID: {make_id}")

    # Schreibe alle Responses in eine neue JSON-Datei
    with open('all_responses.json', 'w') as outfile:
        json.dump(all_responses, outfile, indent=4)

if __name__ == "__main__":
    main()
