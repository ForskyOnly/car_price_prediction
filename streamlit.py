import random
import streamlit as st
import pandas as pd
import pickle


st.set_page_config(page_title="Your Car Estimator", page_icon="🚘", layout="wide")

html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Estimez le prix de votre voiture
    </h2></div>
    
    """
st.markdown(html_temp, unsafe_allow_html=True)



# Charger le modèle prédit
with open('model_predict_car.pkl', 'rb') as file:
    model = pickle.load(file)
    
df = pd.read_csv('cleaned_data.csv')



# Dictionnaire de traduction des colonnes en français
colonnes_fr = {
    'CarName': 'Marque',
    'carbody': 'Type de carrosserie',
    'drivewheel': 'Type de transmission',
    'enginetype': 'Type de moteur',
    'fuelsystem': 'Carburant',
    'wheelbase': 'Empattement',
    'carlength': 'Longueur de la voiture',
    'carwidth': 'Largeur de la voiture',
    'curbweight': 'Poids de la voiture',
    'cylindernumber': 'Nombre de cylindres',
    'enginesize': 'Taille du moteur',
    'boreratio': "Rapport d'alésage",
    'horsepower': 'Puissance (chevaux)',
    'citympg': 'Consommation en ville (mpg)',
    'highwaympg': 'Consommation sur autoroute (mpg)'
}
col1, col2, col3 = st.columns(3)

def get_user_input():
    user_input = {}
    user_input_list = []
    compteur = 0
    for colonne in colonnes_fr:
        if compteur % 3 == 0:
            col = col1
        elif compteur % 3 == 1:
            col = col2
        else:
            col = col3
        user_input[colonne] = col.selectbox(colonnes_fr[colonne], sorted(df[colonne].unique().tolist()), key='selectbox_' + str(compteur))
        compteur += 1
        user_input_list.append(user_input[colonne])

    return pd.DataFrame([user_input_list], columns=colonnes_fr.keys()) 




user_input = get_user_input()

with st.container():
    st.write("<h5 style='text-align: center;'>D'aprés les caractéristiques ci-dessous :</h5>", unsafe_allow_html=True)
    st.write('<div style="display: flex; justify-content: center;"><style>.dataframe .dvn-scroller.glideDataEditor {max-width: 100%;}</style>' + user_input.to_html(classes=["dataframe", "dvn-scroller", "glideDataEditor"], index=False) + '</div>', unsafe_allow_html=True)


st.write("""
    <style>
        p {
            font-size: 1.2em;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)


prediction = model.predict(user_input)
st.write('<h4 style="text-align: center;">La voiture est estimée à :</h4>', unsafe_allow_html=True)
st.write('<h4 style="text-align: center;">' + str(prediction[0].round(2)) + '$'+'</h4>', unsafe_allow_html=True)

