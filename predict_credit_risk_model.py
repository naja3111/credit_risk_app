# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:18:33 2019

@author: NajaMohamed
"""

# Import Libraries
import numpy as np
import pandas as pd
# Model libraries
from sklearn.ensemble import RandomForestClassifier
# from xgboost import XGBClassifier # Use XGBClassifier as we have binary classification problem

# Preprocessing and Pipeline libraries
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder
import pickle

## model accuracy, score and cross validation libraries
from sklearn.metrics import accuracy_score

# Start here to predict models
data_path = r'data\combined_data.csv'  # Check with your folder path coreect them as needed

print("\nLoading data...")
# load data
data = pd.read_csv(data_path, engine='python', header=0)
print("\nThere are ", len(data), "records in dataset")

# Separate out X and y
X = data.loc[:, data.columns != 'is_late']
y = data.iloc[:,-1:]

## From Sklearn train_test_split function
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Assign numeric features from dataset and impute with median for missing data.
numeric_features = ['loan_amnt', 
                    'int_rate', 'annual_inc', 'revol_util', 
                    'dti', 'delinq_2yrs'
                   ]

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ])
# Assign values from dataset
categorical_features = ['purpose','grade', 'emp_length', 'home_ownership']

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

## Main pre-preprocess variable
preprocess = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
        ]
    )


## create a pipeline
model = make_pipeline(preprocess, RandomForestClassifier(n_estimators = 100, random_state=42))

### Train the model
print("\nTraining model ...")
model.fit(X_train, y_train)

print("Accuracy:\n%s" % accuracy_score(y_test, model.predict(X_test)))


print("\nSaving model ...")
file = open('models/credit_risk_model.pkl', 'wb')
pickle.dump(model, file)
file.close()


# load the pickled model
print("\nLoading saved model to make example predictions...")
pickledModel = pickle.load(open('models/credit_risk_model.pkl','rb'))



# Make a prediction for a likely on time payer
payOnTimePrediction = {
    'loan_amnt': [100],
    'int_rate': [0.02039],
    'purpose': ['credit_card'],
    'grade': ['A'],
    'annual_inc': [80000.00],
    'revol_util': [0.05],
    'emp_length': ['10+ years'],
    'dti': [1.46],
    'delinq_2yrs': [0],
    'home_ownership': ['RENT']
    }
payOnTimePredictionDf = pd.DataFrame.from_dict(payOnTimePrediction)

print("\nPredicting class probabilities for likely on-time payer:")
print(pickledModel.predict_proba(payOnTimePredictionDf))

# Prediction for a likely late payer
payLatePrediction = {
    'loan_amnt': [10000],
    'int_rate': [0.6],
    'purpose': ['credit_card'],
    'grade': ['D'],
    'annual_inc': [20000.00],
    'revol_util': [0.85],
    'emp_length': ['1 year'],
    'dti': [42.00],
    'delinq_2yrs': [4],
    'home_ownership': ['RENT']
    }
payLatePredictionDf = pd.DataFrame.from_dict(payLatePrediction)

print("\nPredicting class probabilities for a likely late payer:")
print(pickledModel.predict_proba(payLatePredictionDf))

# Predict class probabilities for a set of records using the test set
print("\nPredicting class probabilities for the test data set:")
print(pickledModel.predict_proba(X_test))

# Check Model Accuracy
# print("Accuracy of pickled model :\n%s" % accuracy_score(y_test, pickledModel.predict(X_test)))
