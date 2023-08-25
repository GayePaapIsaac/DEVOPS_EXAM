import os
import subprocess
from arborescence_script import mon_arbre
import requests

def commit_changes(message):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    
def download_file(url, destination):
    response = requests.get(url)
    with open(destination, "wb") as file:
        file.write(response.content)

def main():
    subprocess.run(["git", "init"])
    
    mon_arbre('Mon_dossier_parent')#je cree mon dossier parent contenant respectant mon arborescence
    commit_changes("Étape 1 : Création de l'arborescence de base")
    
    csv_url = "https://nskm.xyz/assets/dataset.txt"
    csv_destination = "Mon_dossier_parent/docs/exemple.csv"
    download_file(csv_url, csv_destination)
    commit_changes("Étape 2 : Téléchargement du fichier CSV")
    
    
    

if __name__ == "__main__":
    main()
    
    
    
    
    