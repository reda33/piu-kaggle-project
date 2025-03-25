# piu-kaggle-project
# **PIU Kaggle Project - Predictive Modeling for Problematic Internet Use**

## **Description**
Ce projet a pour objectif de prédire l'usage problématique d'Internet chez les enfants et adolescents à partir de données issues de questionnaires cliniques et de mesures physiques.

Le modèle utilise des algorithmes de **Machine Learning** pour classer les individus en fonction de leur niveau de sévérité (`sii`) dans 4 classes :
- **0** : Aucun problème
- **1** : Problème léger
- **2** : Problème modéré
- **3** : Problème sévère

Le modèle a été testé et optimisé avec **LightGBM** et **XGBoost**, deux algorithmes populaires pour les compétitions Kaggle.

## **Table of Contents**
- [Installation](#installation)
- [Data](#data)
- [Features](#features)
- [Modeling](#modeling)
- [Hyperparameter Optimization](#hyperparameter-optimization)
- [Results](#results)
- [Conclusion](#conclusion)

## **Installation**
1. Clonez ce repository :
    ```bash
    git clone https://github.com/ton-utilisateur/piu-kaggle-project.git
    cd piu-kaggle-project
    ```

2. Installez les dépendances nécessaires :
    ```bash
    pip install -r requirements.txt
    ```

## **Data**
Les données proviennent de la compétition Kaggle "Child Mind Institute – Problematic Internet Use". 
Vous pouvez télécharger les données directement depuis la page de la compétition. Les fichiers sont au format `.csv` :
- `train.csv` : Ensemble d'entraînement contenant les caractéristiques des individus et la cible `sii`.
- `test.csv` : Ensemble de test sans la colonne `sii`.

## **Features**
Les principales caractéristiques utilisées dans le modèle sont :
- **Numériques** :
  - `Basic_Demos-Age`, `Physical-BMI`, `PreInt_EduHx-computerinternet_hoursday`, `SDS-SDS_Total_T`
- **Catégorielles** :
  - `Basic_Demos-Sex`, `Basic_Demos-Enroll_Season`, `Physical-Season`

## **Modeling**
Le modèle de base utilise **LightGBM**, un algorithme de boosting populaire. Après une première évaluation, un **XGBoost** a également été testé.

1. **LightGBM** :
   - Hyperparamètres de base :
     - `learning_rate = 0.05`
     - `max_depth = 3`
     - `n_estimators = 100`
     - `num_leaves = 15`
   - **QWK score** : 0.3499 après optimisation.

2. **XGBoost** :
   - Hyperparamètres optimisés :
     - `learning_rate = 0.1`
     - `max_depth = 3`
     - `n_estimators = 100`
     - `subsample = 0.7`
   - **QWK score** : 0.3355.

## **Hyperparameter Optimization**
L'optimisation des hyperparamètres a été réalisée à l'aide de **GridSearchCV**, avec les paramètres suivants :
- **Learning rate**
- **Max depth**
- **Number of estimators**
- **Subsample ratio**

## **Results**
- Après optimisation, **LightGBM** a donné le meilleur résultat avec un **QWK score de 0.3499**.
- Les prédictions ont été générées pour la compétition Kaggle.

Les résultats des prédictions sont disponibles dans le fichier `outputs/submission_baseline.csv`.

## **Conclusion**
Ce projet montre comment des modèles puissants comme **LightGBM** et **XGBoost** peuvent être utilisés pour prédire des problèmes de dépendance à Internet chez les jeunes à partir de données cliniques et de comportement.

- **LightGBM** a donné les meilleurs résultats.
- Le modèle peut encore être amélioré par l'ajout de nouvelles features, un meilleur tuning des hyperparamètres, ou l'intégration de données externes.

## **Future Work**
- Test de modèles supplémentaires (comme **CatBoost**)
- Exploration de techniques avancées pour le **rééquilibrage des classes**
- Amélioration des performances avec **features additionnelles**.

