# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 21:35:00 2019

@author: NajaMohamed
"""
## Import Nexessary Packages to Runt the Model
import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
import webbrowser

app = Flask(__name__)
model = pickle.load(open('models/credit_risk_model.pkl', 'rb'))

@app.route('/')
def home():
    ## use index.html to create an HTML page for our application
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    ::: Get input from users
    ::: Predict values using the pickled model
    
    In the following model, predict_proba takes in a Pandas DataFrame
    Map user input into its feature using a dictionary and create a pandas Data Frame
    
    '''
    ## Features or predictors for model is user input
    features = [x for x in request.form.values()]
    
    # Instantiate an empty dictionary
    # This dictionary saves user input as values for below keys
    payFeatures_dict = {}
    
    # Create keys for dictionary 
    keys = ['loan_amnt', 'int_rate', 'purpose', 'grade', 'annual_inc', 'revol_util', 
            'emp_length', 'dti', 'delinq_2yrs', 'home_ownership']
    
    # Iterate through each value in form and assign values to dictionary keys
    for k, val in zip(keys, features):
        payFeatures_dict[k] = val 
    
    pred_val_df = pd.DataFrame(payFeatures_dict, index=[0])
    
    prediction = model.predict_proba(pred_val_df)
    
    ## First value 0th index tells use the probability of 0 happening, which is no rsik associated
    ## Using 0th index for output value 0 print risk result, so users can see the result.
    if prediction[0][0] >= 0.9:
        risk = "No Risks associated with the profile entered"
    elif prediction[0][0] < 0.9:
        risk = "Risks associated with this profile entered"
    
    #return render_template('index.html', prediction_text='Credit Risk{}'.format(risk))
    return render_template('index.html', prediction_text="Result: {}".format(risk))


if __name__ == "__main__":
    webbrowser.open('http://localhost:5000')
    app.run(debug=True)