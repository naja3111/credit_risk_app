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
and get prediections as output. Flask application uses a predict function, which uses the pickled model from local folder that gives predictions for "POST" method. These are done within the virtual environment itself.

##### Task 2:
The purpose of the following steps are to improve exisitng randomforest classification model and deploy it to the REST API. After a quick data exploration, since the data seemed little imbalanced with more of the positive outcome variables and less of negative 
outcome variables. However, given trainig and test datset was combined together, shuffled and divided into 80:20 train and test sets althouugh this approcah did not make a big difference. Accuracy is not a good measure 
as data is imbalanced and ROC-AUC curve was slight more than 50% which always would positive results (0 in our case) for a randomly selected sample (i.e test/unseen data).
to improve the model, hyperparameter of the model was tuned (n_estimators were increased from default 10 up to 100. This time the AUC went higher from 0.380 to 0.504. This model was re-deployed into the production.

In order to deploy the model that can be used by many users, a PaaS (platform as a service) style architecture was used. This serves the model into the world wide web using python flask application. Since Heroku works connecting to 
github updates of the models can be re-deployed by committing model changes since Flask will continue to use the saves model. It will be much nicer, if this model can be deployed into AWS or Azure with docker (different versions containerrized)
into the cloud as IaaS (infrastrucure as service), which will enable many users to access the REST API without stopping the service.
