# tkv-format TKV Time Key Value

## Description

**TKV Time Key Value** est un format de données simplifié pour stocker des séries temporelles de capteurs avec des valeurs associées. Chaque ligne représente un enregistrement de timestamp avec fuseau horaire, suivi de paires `clé:valeur` pour chaque capteur. Ce format est facile à lire, compact, et adapté pour des applications qui nécessitent des enregistrements de capteurs structurés et datés.

## Format des données

Chaque enregistrement est constitué d'un timestamp avec fuseau horaire suivi de paires `clé:valeur` pour chaque capteur. Le format général est le suivant :

```
timestamp ; capteur1:valeur1 ; capteur2:valeur2 ; ...
```

Le format de timestamp recommandé est conforme à la norme **ISO 8601**, incluant le fuseau horaire, comme suit :

```
YYYY-MM-DDTHH:MM:SS±HH:MM
```

### Exemple

```
2024-11-12T14:32:45+01:00 ; temperature:22.5 ; humidity:45.0 ; pressure:1013
```

Dans cet exemple :
- `timestamp` est l'heure de l'enregistrement avec fuseau horaire (ici, `+01:00`).
- `temperature`, `humidity`, et `pressure` sont des clés représentant différents capteurs.
- `22.5`, `45.0`, et `1013` sont les valeurs associées à chaque capteur au moment de cet enregistrement.

## Structure du Projet

```
- TKV/
    - data/               # Dossier pour les fichiers de données au format TKV
    - src/                # Code source du projet
        - parser.py       # Script pour lire et analyser les fichiers TKV
        - writer.py       # Script pour générer et écrire des fichiers TKV
    - README.md           # Documentation du projet
    - requirements.txt    # Dépendances Python
```

## Installation

Assurez-vous d’avoir **Python 3.8** ou une version ultérieure. Pour installer les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

### Parsing d’un fichier TKV

Le script `parser.py` permet de lire un fichier TKV et de charger les données dans une structure Python.

Exemple d'utilisation :

```python
from src.parser import parse_tkv

data = parse_tkv("data/fichier.tkv")
print(data)
```

### Création d’un fichier TKV

Le script `writer.py` permet de créer un nouveau fichier TKV à partir de données sous forme de dictionnaire.

Exemple d'utilisation :

```python
from src.writer import write_tkv

data = [
    {"timestamp": "2024-11-12T14:32:45+01:00", "temperature": 22.5, "humidity": 45.0, "pressure": 1013},
    {"timestamp": "2024-11-12T14:33:00+01:00", "temperature": 22.4, "humidity": 44.8, "pressure": 1012},
]

write_tkv("data/nouveau_fichier.tkv", data)
```

## Contribution

1. Fork le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Committez vos modifications (`git commit -m 'Ajouter ma fonctionnalité'`).
4. Pushez vers la branche (`git push origin feature/ma-fonctionnalité`).
5. Créez une Pull Request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

## Auteurs

- **Votre Nom** - Créateur du projet

--- 

Ce fichier est structuré en Markdown pour une meilleure lisibilité sur GitHub et autres plateformes.