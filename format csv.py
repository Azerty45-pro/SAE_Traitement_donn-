import csv

etudiants = [
    {"ID": 1, "Nom": "Schmitt", "Prenom": "Albert", "Note": 9},
    {"ID": 2, "Nom": "Al-Hakim", "Prenom": "Yasmine", "Note": 17},
    {"ID": 3, "Nom": "Tran", "Prenom": "Sebastien", "Note": 12},
    {"ID": 4, "Nom": "Meyer", "Prenom": "Claire", "Note": 16},
    {"ID": 5, "Nom": "Kobayashi", "Prenom": "Kaito", "Note": 11}
]
with open('fichier.csv', mode='w', encoding='utf-8', newline='') as file:
    champs = ["ID","Nom", "Prenom", "Note"]
    fichier = csv.DictWriter(file, fieldnames=champs)
    fichier.writeheader()
    fichier.writerows(etudiants)

resultatetudiants = [
    {"ID": 1, "Nom": "Schmitt", "Prenom": "Albert", "Resultat": "Refusé"},
    {"ID": 2, "Nom": "Al-Hakim", "Prenom": "Yasmine", "Resultat": "Admis"},
    {"ID": 3, "Nom": "Tran", "Prenom": "Sebastien",  "Resultat": "Admis"},
    {"ID": 4, "Nom": "Meyer", "Prenom": "Claire",  "Resultat": "Admis"},
    {"ID": 5, "Nom": "Kobayashi", "Prenom": "Kaito",  "Resultat": "Admis"}
]

with open('resultat.csv', mode='w', encoding='utf-8', newline='') as file:
    champs = ["ID","Nom", "Prenom", "Resultat"]
    resultat= csv.DictWriter(file, fieldnames=champs)
    resultat.writeheader()
    resultat.writerows(resultatetudiants)