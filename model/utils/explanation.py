import lime
import lime.lime_tabular
import pandas as pd
import pickle

# Chargement du modèle et des données
model = pickle.load(open('model/model.pkl', 'rb'))
data = pd.read_csv('data/jeu_donnees_budgetaires_simule.csv')
data_encoded = pd.get_dummies(data, columns=['Entité', 'Poste budgétaire', 'Contexte économique'], drop_first=True)
feature_names = data_encoded.drop(['Bonne décision'], axis=1).columns

explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=data_encoded.drop(['Bonne décision'], axis=1).values,
    feature_names=feature_names,
    class_names=['Mauvaise Décision', 'Bonne Décision'],
    mode='classification'
)

def expliquer_decision(instance):
    exp = explainer.explain_instance(instance, model.predict_proba, num_features=5)
    return exp.as_list()
