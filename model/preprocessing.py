import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Chargement des données
data = pd.read_csv('data/jeu_donnees_budgetaires_simule.csv')

# Encodage des variables catégorielles
data_encoded = pd.get_dummies(data, columns=['Entité', 'Poste budgétaire', 'Contexte économique'], drop_first=True)

# Colonnes explicatives et cible
X = data_encoded.drop(['Bonne décision'], axis=1)
y = data_encoded['Bonne décision']

# Division en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Sauvegarde du modèle
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modèle entraîné et sauvegardé avec succès.")
