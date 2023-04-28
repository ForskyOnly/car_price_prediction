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



with open('/car_prediction/model_predict_car.pkl', 'rb') as file:
    model = pickle.load(file)
    
df = pd.read_csv('cleaned_data.csv')




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

def donnes_pour_prediction() -> pd.DataFrame :
    """
    Cette fonction permet de créer une interface utilisateur pour saisir les caractéristiques d'une voiture pour laquelle
    on veut prédire le prix. Elle retourne un DataFrame Pandas contenant les caractéristiques saisies par l'utilisateur ainsi que le prix prédis.
    Returns:
        pd.DataFrame: Un DataFrame Pandas contenant les caractéristiques d'une voiture entré par l'utilisateur et le prix de la prédiction en format'float'
    """
    carac_voiture = {}
    carac_voiture_list = []
    compteur = 0
    for colonne in colonnes_fr:
        if compteur % 3 == 0:
            col = col1
        elif compteur % 3 == 1:
            col = col2
        else:
            col = col3
        carac_voiture[colonne] = col.selectbox(colonnes_fr[colonne], sorted(df[colonne].unique().tolist()), key='selectbox_' + str(compteur))
        compteur += 1
        carac_voiture_list.append(carac_voiture[colonne])

    return pd.DataFrame([carac_voiture_list], columns=colonnes_fr.keys()) 




carac_voiture = donnes_pour_prediction()

with st.container():
    st.write("<h5 style='text-align: center;color : #FFF8DC;'>D'aprés les caractéristiques ci-dessous :</h5>", unsafe_allow_html=True)
    st.write('<div style="display: flex; justify-content: center;"><style>.dataframe .dvn-scroller.glideDataEditor {max-width: 100%;}</style>' + carac_voiture.to_html(classes=["dataframe", "dvn-scroller", "glideDataEditor"], index=False) + '</div>', unsafe_allow_html=True)


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
        .css-8ojfln.e1wqxbhn1{
            background-color : #1E2A3A ;
            color : #FFC300;
        }
        .css-bn3168.e1wbw4rs0.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bf.st-bg.st-dm.st-bt.st-dn.st-cg.st-do.st-b1.st-bs.st-as.st-dp.st-dq.st-ao.st-aq.st-dl{
            background-color : #1E2A3A;
        }
        div{
            background-color:#1E2A3A;
        }
        td{
            color : #FFC300;
        }
    </style>
""", unsafe_allow_html=True)


prediction = model.predict(carac_voiture)
st.write('<h4 style="text-align: center;color : #FFF8DC;">La voiture est estimée à :</h4>', unsafe_allow_html=True)
st.write('<h1 style="text-align: center; color : green; font-weight: bold;" >' + str(prediction[0].round(2)) + ' 💲 '+'</h4>', unsafe_allow_html=True)

