import json

fiche = {
    "Nom": "Weber",
    "Prenom": "Charlotte",
    "age": 32,
    "profession": "ingénieure",
    "langues": ["Français", "Anglais", "Japonais"]
}

with open('donnees.json', mode='w', encoding='utf-8') as file:
    json.dump(fiche, file, indent=4)