import streamlit as st
import pandas as pd
import joblib

# Charger le modèle pré-entrainé LightGBM
model = joblib.load('models/model_lightgbm.pkl')

def predict_problem(age, bmi, hours_internet, depression_score, sex, season_enroll, physical_season):
    input_data = pd.DataFrame({
        'Basic_Demos-Age': [age],
        'Physical-BMI': [bmi],
        'PreInt_EduHx-computerinternet_hoursday': [hours_internet],
        'SDS-SDS_Total_T': [depression_score],
        'Basic_Demos-Sex': [sex],
        'Basic_Demos-Enroll_Season': [season_enroll],
        'Physical-Season': [physical_season]
    })

    st.write("🧪 Données envoyées au modèle :", input_data)

    prediction = model.predict(input_data)
    st.write("📊 Prédiction brute du modèle :", prediction)

    if prediction[0] == 0:
        return "Aucun problème d'Internet"
    elif prediction[0] == 1:
        return "Problème léger d'Internet"
    elif prediction[0] == 2:
        return "Problème modéré d'Internet"
    else:
        return "Problème sévère d'Internet"


# Interface utilisateur Streamlit
st.title('Prédiction de l\'utilisation problématique d\'Internet')

# Entrées utilisateur
age = st.number_input('Âge', min_value=0, max_value=100, value=18)
bmi = st.number_input('IMC (Indice de Masse Corporelle)', min_value=10.0, max_value=50.0, value=20.0)
hours_internet = st.number_input('Heures d\'Internet par jour', min_value=0, max_value=24, value=2)
depression_score = st.number_input('Score de dépression (SDS)', min_value=0, max_value=100, value=10)
sex = st.selectbox('Sexe', options=[0, 1])  # 0 = Garçon, 1 = Fille
season_enroll = st.selectbox('Saison d\'inscription', options=[0, 1, 2, 3])  # Exemple pour 4 saisons possibles
physical_season = st.selectbox('Saison physique', options=[0, 1, 2, 3])

# Bouton pour prédire
if st.button('Prédire'):
    result = predict_problem(age, bmi, hours_internet, depression_score, sex, season_enroll, physical_season)
    st.write(f"Résultat de la prédiction : {result}")

