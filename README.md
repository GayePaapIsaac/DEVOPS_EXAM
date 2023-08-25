# Mon Programme  Exam

## Description

Mon Programme Exam est un utilitaire en ligne de commande qui crée une structure d'arborescence spécifique et télécharge un fichier CSV à partir d'une URL.

## Fonctionnalités

- Crée une structure d'arborescence organisée en utilisant le script `arborescence_script.py`.
- Télécharge un fichier CSV à partir de l'URL spécifiée.
- Effectue des commits pour chaque étape majeure du développement.

## Conception

Le programme est écrit en Python et suit une approche modulaire pour améliorer la lisibilité et la maintenance. Il est composé de plusieurs modules :

- `main.py` : Le point d'entrée du programme.
- `arborescence_script.py` : Contient la fonction `mon_arbre` pour créer la structure d'arborescence.
- `requests` : Utilisé pour télécharger le fichier CSV à partir d'une URL.

## Utilisation

1. Assurez-vous d'avoir Python installé.
2. Clonez ce dépôt sur votre machine.
3. Ouvrez un terminal et accédez au répertoire du programme.

Exécutez le programme avec la commande suivante :

```bash
python main.py



## Exemples d'arborescence créée
├── data               #  repertoire contenant des données (brutes, propres)
│   ├── cleaned
│   └── raw
├── docs               #  repertoire contenant toute documentation utile
├── LICENSE
├── Makefile           #  fichier permettant d'automatiser des taches
├── models             #  repertoire contenant tous les modèles construits
├── notebooks          #  repertoire contenant tous les notebooks rédigés
│   └── main.ipynb
├── README.md
├── reports            #  repertoire contenant tous les rapports générés
├── requirements.txt   #  fichier contenant la liste des dépendances du projets
└── src                #  repertoire contenant tout code python utile
    └── utils.py