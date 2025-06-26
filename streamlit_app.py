import pandas as pd
import streamlit as st

# Charger les données
data = pd.read_csv('data/jeu_donnees_budgetaires_simule.csv')

# Interface utilisateur
st.title('Kobi - Assistant Budgétaire Intelligent')

st.write('Aperçu du Jeu de Données')
st.write(data.head())

# Saisie utilisateur
st.write('### Simuler une décision budgétaire')
entite = st.text_input('Entité')
annee = st.selectbox('Année', data['Année'].unique())
poste = st.selectbox('Poste budgétaire', data['Poste budgétaire'].unique())
montant = st.number_input('Montant alloué ($)')
contexte = st.selectbox('Contexte économique', data['Contexte économique'].unique())

if st.button('Soumettre la décision'):
    st.write('Analyse en cours...')
    st.write(f"Entité : {entite}")
    st.write(f"Année : {annee}")
    st.write(f"Poste budgétaire : {poste}")
    st.write(f"Montant : {montant}")
    st.write(f"Contexte : {contexte}")
    st.success('Simulation terminée. (Modèle à intégrer)')

st.write('Prochaine étape : Intégration du modèle et des explications.')

st.write("Merci d'utiliser Kobi - Assistant Budgétaire Intelligent !")