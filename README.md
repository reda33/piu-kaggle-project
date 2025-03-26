# PIU Kaggle Project – Predictive Modeling for Problematic Internet Use

##  Description

Ce projet a été réalisé dans le cadre de la compétition Kaggle **"Problematic Internet Use"** organisée par le **Child Mind Institute**.  
L'objectif : **prédire le niveau de sévérité de l’usage problématique d’Internet (sii)** chez les enfants et adolescents, à partir de données cliniques, physiques et comportementales.

Les individus sont classés en 4 catégories :
- `0` : Aucun problème
- `1` : Problème léger
- `2` : Problème modéré
- `3` : Problème sévère

---

##  Table of Contents
- [Installation](#installation)
- [Data](#data)
- [Features](#features)
- [Modeling](#modeling)
- [Hyperparameter Optimization](#hyperparameter-optimization)
- [Results](#results)
- [Application Streamlit](#application-streamlit-interface-interactive)
- [Déploiement Cloud (AWS)](#déploiement-cloud-aws)
- [Conclusion](#conclusion)
- [Future Work](#future-work)

---

##  Installation

```bash
git clone https://github.com/reda33/piu-kaggle-project.git
cd piu-kaggle-project
pip install -r requirements.txt
```

---

##  Data

Les données utilisées proviennent de la compétition Kaggle :  
🔗 https://www.kaggle.com/competitions/child-mind-institute-problematic-internet-use/

- `train.csv` : données d’entraînement avec la cible `sii`
- `test.csv` : données de test sans la colonne `sii`

---

##  Features

###  Variables numériques
- `Basic_Demos-Age`
- `Physical-BMI`
- `PreInt_EduHx-computerinternet_hoursday`
- `SDS-SDS_Total_T`

###  Variables catégorielles
- `Basic_Demos-Sex`
- `Basic_Demos-Enroll_Season`
- `Physical-Season`

---

##  Modeling

###  Modèle principal : LightGBM
- `learning_rate = 0.05`
- `max_depth = 3`
- `n_estimators = 100`
- `num_leaves = 15`
-  QWK Score : **0.3499**

###  Comparatif : XGBoost
- `learning_rate = 0.1`
- `max_depth = 3`
- `n_estimators = 100`
- `subsample = 0.7`
-  QWK Score : **0.3355**

---

##  Hyperparameter Optimization

Optimisation réalisée avec `GridSearchCV` sur :
- `learning_rate`
- `max_depth`
- `n_estimators`
- `subsample`
- `num_leaves`

---

##  Results

-  **Meilleur modèle** : LightGBM  
-  **QWK Score** : 0.3499  
-  Prédictions disponibles dans : `outputs/submission_baseline.csv`

---

##  Application Streamlit (Interface interactive)

Une interface a été développée avec **Streamlit** pour simuler une prédiction dynamique.

###  Lancer l'application localement :
```bash
streamlit run app.py
```

L’utilisateur peut renseigner : âge, IMC, score de dépression, etc.  
→ Et obtenir une prédiction claire : **aucun problème / léger / modéré / sévère**

---

## ☁ Déploiement Cloud (AWS)

L'application a été **déployée sur un serveur EC2 Ubuntu via AWS**, avec :
- Création d’instance
- Environnement virtuel Python
- Installation des dépendances
- Ouverture du port `8501` (Streamlit)
- Lancement et accès via IP publique

🔗 Démo en ligne disponible ici (exemple) :
```
http://15.237.191.31:8501
```

---

##  Conclusion

Ce projet démontre la capacité à :
- Manipuler des données réelles issues d’un contexte clinique
- Appliquer des modèles de classification supervisés
- Optimiser les performances
- Créer une interface simple et intuitive
- Déployer une solution sur le cloud

---

##  Future Work

- Intégration de **SHAP** pour l’interprétabilité des prédictions
- Déploiement automatisé sur **Streamlit Cloud / Docker**
- Ajout de **features combinées** ou dérivées
- Rééquilibrage des classes avec **SMOTE**

---

 **Auteur** : Rida KHAYI  
🔗 [Mon GitHub](https://github.com/reda33)

