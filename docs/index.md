### Exemple d'utilisation

En utilisant le fichier `data.tkv` comme dans l'exemple précédent :

```python
# Lire les données avec read_tkv
data = read_tkv("data/data.tkv")

# Convertir en DataFrame
df = to_dataframe(data)
print(df)
```

### Sortie attendue

```
                           temperature  humidity  pressure
timestamp                                                
2024-11-12 14:32:45+01:00         22.5      45.0    1013.0
2024-11-12 14:33:00+01:00         22.4      44.8    1012.0
```

### Explications

- **`pd.DataFrame(data)`** : Crée un DataFrame à partir de la liste de dictionnaires renvoyée par `read_tkv`.
- **`df.set_index("timestamp", inplace=True)`** : Utilise la colonne `timestamp` comme index du DataFrame. Cela permet de traiter chaque entrée comme une observation temporelle, utile pour les analyses de séries temporelles.

Ce DataFrame est maintenant prêt pour des analyses supplémentaires et permet une manipulation facile des données dans un format tabulaire avec `pandas`.