
# Kobi - Assistant Budgétaire Intelligent

##  Projet
**Kobi** est un modèle d'IA génératif explicatif conçu pour accompagner les décideurs publics québécois dans la prise de décisions budgétaires. Il propose des recommandations optimisées et produit des explications claires pour chaque décision, contribuant à une meilleure transparence et à une gestion efficace des ressources publiques.

---

##  Fonctionnalités
- Analyse des décisions budgétaires.
- Évaluation de la qualité des allocations budgétaires.
- Génération d'explications automatiques via LIME (XAI).
- Interface utilisateur interactive développée avec Streamlit.
- Déploiement containerisé avec Docker.

---

## Technologies utilisées
- Python 3.9
- Scikit-learn
- LIME (Local Interpretable Model-agnostic Explanations)
- Streamlit
- Docker

---

## 🗂️ Structure du projet
```
kobi-assistant/
├── Dockerfile
├── requirements.txt
├── streamlit_app.py
├── jeu_donnees_budgetaires_simule.csv
└── README.md
```

---

## ⚙️ Installation et exécution avec Docker


### 1. Construire l’image Docker
```bash
docker build -t kobi-app .
```

### 2. Lancer le conteneur Docker
```bash
docker run -p 8501:8501 kobi-app
```

### 3. Accéder à l’application
Ouvrez votre navigateur à l’adresse :  
[http://localhost:8501](http://localhost:8501)

---

## 📊 Jeu de données
Le jeu de données contient les colonnes suivantes :
- **Entité** : Organisation publique (ex : Ville, CIUSSS, etc.)
- **Année** : Année budgétaire
- **Poste budgétaire** : Secteur d’affectation des fonds (ex : Sécurité, Recherche)
- **Montant alloué ($)** : Montant attribué
- **Contexte économique** : Croissance, Récession ou Stable
- **Justification** : Motif de l’allocation budgétaire
- **Bonne décision** : Label généré (0 : Mauvaise décision, 1 : Bonne décision)

---

## 🔍 Exemple d’utilisation
- L’utilisateur entre une nouvelle décision budgétaire.
- Le modèle prédit si c’est une bonne ou une mauvaise décision.
- LIME explique les critères les plus influents dans la décision.

---

## 📈 Objectifs futurs
- Enrichir le jeu de données avec des sources réelles.
- Intégrer SHAP comme alternative à LIME.
- Déployer le projet sur une plateforme Cloud (AWS, Azure).
- Ajouter une fonctionnalité d’historique des décisions.

---

## 👤 Auteur
**Kobenan Kouman Dua**  
 Futur Devops and Cloud Engineer |Étudiant en Science des Données|Passionée de MLOPS

[LinkedIn](www.linkedin.com/in/kobenan-kouman-dua-2904531b7) 

---

## 📬 Contact
Pour toute question ou collaboration : **duakobe12@gmail.com**
