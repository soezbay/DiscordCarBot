import json

def main():
    # Lese die Daten aus der Datei all_responses.json
    with open('all_responses.json', 'r') as file:
        all_responses = json.load(file)
    
    # Iteriere über alle Einträge in all_responses und ändere den Schlüssel "Response" zu "Models"
    for entry in all_responses:
        entry['Models'] = entry.pop('Response')

    # Schreibe die aktualisierten Daten in eine neue JSON-Datei namens allmodels.json
    with open('allmodels.json', 'w') as outfile:
        json.dump(all_responses, outfile, indent=4)

if __name__ == "__main__":
    main()