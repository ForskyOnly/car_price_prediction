import random
import streamlit as st
import pandas as pd
import pickle


st.set_page_config(page_title="Car Price Estimator", page_icon="🚘", layout="wide")

html_temp = """
    <div style="background: #1E2A3A ;padding:10px; margin-bottom : 20px">
    <h2 style="color:#FFF8DC;text-align:center;"> Estimez le prix de votre voiture
    </h2></div>
    
    """
st.markdown(html_temp, unsafe_allow_html=True)



with open('model_predict_car.pkl', 'rb') as file:
    model = pickle.load(file)
    
df = pd.read_csv('cleaned_data.csv')



# Dictionnaire de traduction des colonnes en français
colonnes_fr = {
    'CarName': 'Marque',
    'carbody': 'Type de carrosserie',
    'drivewheel': 'Motricité',
    'enginetype': 'Type de moteur',
    'fuelsystem': 'Systéme de carburant',
    'wheelbase': 'Empattement',
    'carlength': 'Longueur de la voiture (cm)',
    'carwidth': 'Largeur de la voiture (cm)',
    'curbweight': 'Poids de la voiture (kg)',
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
    st.write("<h5 style='text-align: center;color : #FFF8DC;'>D'aprés les caractéristiques ci-dessous :</h5>", unsafe_allow_html=True)
    st.write('<div style="display: flex; justify-content: center;"><style>.dataframe .dvn-scroller.glideDataEditor {max-width: 100%;}</style>' + user_input.to_html(classes=["dataframe", "dvn-scroller", "glideDataEditor"], index=False) + '</div>', unsafe_allow_html=True)


st.write("""
    <style>
        p {
            font-size: 1.2em;
            font-weight: bold;
            background-color :  #1E2A3A;
            color : #FF5733;
        }
        th {
            font-size: 1.2em;
            font-weight: bold;
            text-align: center;
            background-color :  #1E2A3A;
            color : #FF5733;
        }
        .css-81oif8.effi0qh3{
            background-color :  #1E2A3A;
        }
        .css-18ni7ap.e8zbici2{
            background-color:  #1E2A3A;
        }
        .block-container.css-z5fcl4.egzxvld4{
            background-color :  #1E2A3A;
        }
        .st-c8.st-bf.st-c9.st-ca.st-cb.st-bh.st-cc.st-cd.st-ce{
            color: #FFC300;
            background-color:  #1E2A3A;
            font-weight: bold;
        }
        .st-bf.st-bg.st-bz.st-c0.st-c1.st-b3.st-c2.st-c3.st-bh.st-c4.st-c5.st-c6.st-c7{
            background-color:  #1E2A3A;
        }
        path{
            color: #FFC300;
            background-color:  #1E2A3A;
        }
        footer{
            background-color:  #1E2A3A;
        }
        .st-bf.st-bg.st-b3.st-d1.st-c2.st-d2.st-c7{
            background-color:  #1E2A3A;
        }
        
        td{
            color : #FFC300;
        }
    </style>
""", unsafe_allow_html=True)


prediction = model.predict(user_input)
st.write('<h4 style="text-align: center;color : #FFF8DC;">La voiture est estimée à :</h4>', unsafe_allow_html=True)
st.write('<h2 style="text-align: center; color : green; font-weight: bold;" >' + str(prediction[0].round(2)) + ' 💲 '+'</h4>', unsafe_allow_html=True)

