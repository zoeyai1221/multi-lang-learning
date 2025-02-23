# Healthcare Analytics: Diabetes Risk Prediction Model

## Overview
An end-to-end machine learning project that predicts diabetes risk using patient health indicators. The model achieves 98.4% accuracy using Random Forest Classifier, potentially enabling early diagnosis and intervention.

## Dataset
- Source: National Institute of Diabetes, Digestive and Kidney Diseases (via Kaggle)
- Size: 2,768 patient records
- Features: 8 health-related numerical attributes
- Target: Binary classification (0: Healthy, 1: Diabetic)

## Project Structure
```
├── EDA
│   ├── EDA (Exploratory data analysis).ipynb
│   └── Healthcare-Diabetes.csv
└── Native Bayes and Random Forest
    ├── Healthcare-Diabetes.csv
    └── models.ipynb
```

## Methodology
1. **Data Preprocessing**
   - Outlier detection and removal
   - Feature selection based on correlation analysis
   - No missing values or duplicates found

2. **Exploratory Data Analysis**
   - Distribution analysis of health indicators
   - Correlation analysis between variables
   - Feature importance evaluation

3. **Model Development**
   - Implemented Bernoulli Naive Bayes and Random Forest classifiers
   - Model comparison and evaluation using confusion matrices
   - Random Forest achieved superior performance

## Technologies Used
- Python (Pandas, NumPy)
- Scikit-learn
- Seaborn/Matplotlib

## Results
- Random Forest Classifier: 98.4% accuracy
- Successfully identified key health indicators for diabetes prediction
- Created visualization tools for healthcare provider decision support