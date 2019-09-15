![phData Logo](img/phData_color_rgb.jpg "phData Logo")

# phData MLE Challenge Project
*An application that will predict whether a candidate should be given loan based on credit risk factors.*

### Objective
Objective of this proejct is to demonstrate deploying a machine learning model into production using a REST API after building a ml model. 
phData MLE-Challenge has given a dataset, pre-built model and other environemnt set up to run pre-built model.

### Tasks:
* Task 1: Explore and run pre-built model with given data and deploy the model into a REST API that allows users to POST data and obtain predictions.
* Task 2:Improve given model (I tried a different model) and deploy into a REST API where multiple users can use API resources without service interruption.

### My Approach
##### Task 1:
The model provided in in the challege was deployed locally using Flask REST API in an Anaconda virtual environment. A web template with a form was used, so that a user can enter values, which are model features into the form
and get prediections as output. Flask application uses a predict function, which uses the pickled model from local folder that gives predictions for "POST" method. These are done within the virtual envrinment itself.
