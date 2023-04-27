# Car Price Prediction

## Context du projet

Ce projet a été réalisé lors de la formation "Développeur Data IA" à l'ecole Microsoft by Simplon. On nous a fourni un fichier CSV contenant des données sur les voitures, et notre objectif était de créer un modèle d'apprentissage automatique capable d'estimer le prix d'une voiture en se basant sur ces données.



## Description du projet 

**"Votre client, un revendeur de voiture, souhaite la création d'une application pouvant estimer le prix d'une voiture."**

Le projet consistait à analyser et à nettoyer les données, à construire un modèle d'apprentissage automatique à l'aide d'un algorithme  de regression lineaire, et à déployer le modèle sur une application Streamlit.

##### BONUS :

Rendre l'application accesible via une api(FastAPI)

## Fichiers présent dans le depot: 

#### Fichiers Jupyter Notebooks :

1. data_cleaning.ipynb : Ce fichier contient le code utilisé pour nettoyer les données.
2. data_analyse.ipynb : Ce fichier contient les données d'analyse et les graphiques pour comprendre les données.
3. modelisation.ipynb : Ce fichier contient le model d'apprentissage automaique.

#### Fichiers CSV :

1. cars.csv : la fichier de base contenant les informations nécessaire
2. cleaned_data.csv : le fichier cars.csv nettoyer

#### Autres fichiers :

- streamlit.py contenant le modéle dépolyé sur une app streamlit pret  à être utilisé
- model_predict_car.pkl le modele d'apprentissage automatique términé
- creation_bdd.py : script python pour crée et implanter les données dans une bdd sqlite
- cars.bdd : la base de donnée qui sera crée(étape précèdante) regroupant les données 
- main.py : le script pour la création de l'API




## Installation

1. Clonez [ce dépôt.](https://github.com/ForskyOnly/car_price_prediction)
2. Installez les dépendances avec `pip install`.


## Bibliothèque utilisées

- Scikit-learn (sklearn)
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Streamlit
- Pickle
- FastAPI
- Uvicorn
- Pydantic
- Sqlite3


## Utilisation

- Exécutez tout les notebooks `.ipynb` pour récupérer les informations
- Exécutez `streamlit run streamlit.py` pour lancer l'interface Web Streamlit
- Exécutez `creation_bdd.py` pour crée la base de donnée
- Exécutez `main.py` pour lancer l'API ou `uvicorn main:app --reload` dans un terminal
- Entrez http://127.0.0.1:8000/docs#/ dans votre navigateur pour acceder à l'interface de l'API

**Vous pouvez désormer estimé le prix d'une voiture , ajouter, supprimer ou modifier les voiture dans votre base de données**


## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
