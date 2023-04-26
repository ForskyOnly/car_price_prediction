import streamlit as st
import pandas as pd
import pickle

html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Estimez le prix d'une voitre
    </h2></div>
    
    """
st.markdown(html_temp, unsafe_allow_html=True)

# Charger le modèle prédit
with open('model_predict_car.pkl', 'rb') as file:
    model = pickle.load(file)

# Créer un dictionnaire avec les noms français des colonnes
column_names = {
    'CarName': 'Nom de la voiture',
    'carbody': 'Type de carrosserie',
    'drivewheel': 'Type de transmission',
    'wheelbase': 'Empattement',
    'carlength': 'Longueur',
    'carwidth': 'Largeur',
    'curbweight': 'Poids',
    'enginetype': 'Type de moteur',
    'cylindernumber': 'Nombre de cylindres',
    'enginesize': 'Taille du moteur',
    'fuelsystem': 'Système de carburant',
    'boreratio': 'Rapport d\'alésage',
    'horsepower': 'Puissance',
    'citympg': 'Consommation en ville',
    'highwaympg': 'Consommation sur autoroute'
}

# Créer une fonction pour traduire les noms des colonnes en français
def get_french_column_name(column_name):
    if column_name in column_names:
        return column_names[column_name]
    else:
        return column_name

# Créer une fonction pour charger les données utilisateur et les traduire en anglais
def get_user_input():
    user_input = {}
    for column_name in column_names.keys():
        french_name = get_french_column_name(column_name)
        if column_name in ['CarName', 'carbody']:
            user_input[column_name] = st.text_input(french_name)
        else:
            user_input[column_name] = st.number_input(french_name)
    return pd.DataFrame([user_input])


st.title('Prédiction de prix de voitures')
st.write('Entrez les caractéristiques de votre voiture pour obtenir une prédiction de prix.')
user_input = get_user_input()
st.write('Voici les caractéristiques de votre voiture :')
st.write(user_input)

prediction = model.predict(user_input)
st.write('Le prix de votre voiture est estimé à :')
st.write(prediction[0])
