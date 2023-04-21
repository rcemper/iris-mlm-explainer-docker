![image](https://user-images.githubusercontent.com/18219467/233314974-71c44cf3-8abd-4f92-b550-9f5f578ac331.png)
# iris-mlm-explainer
This web application connects to InterSystems Cloud SQL to create, train, validate, and predict ML models, make Predictions and display a dashboard of all the trained models with an explanation of the workings of a fitted machine learning model.
The dashboard provides interactive plots on model performance, feature importances, feature contributions to individual predictions, partial dependence plots, SHAP (interaction) values, visualization of individual decision trees, etc.

The Application includes the following:
- Jupyter Notebook to explore data, create, train, validate, and predict model
- Web Application to view the Prediction
- Web Application for explainer dashboard which includes the following:
  - SHAP values (i.e. what is the contribution of each feature to each individual prediction?)
  - Permutation importance (how much does the model metric deteriorate when you shuffle a feature?)
  - Partial dependence plots (how does the model prediction change when you vary a single feature?)
  - For Random Forests and xgboost models: visualization of individual trees in the ensemble.
  - Plus for classifiers: precision plots, confusion matrix, ROC AUC plot, PR AUC plot, etc
  - For regression models: goodness-of-fit plots, residual plots, etc.

![](https://github.com/mwaseem75/iris-mlm-explorer/blob/main/irisMLMExp.gif)

# Prerequisits
- You should have an account with [InterSystems Cloud SQL](https://portal.sql-contest.isccloud.io/cloudservices). 
- You should have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed locally.
- You should have [Python3](https://www.python.org/downloads/) installed locally. 

# Getting Started
We will follow the below steps to create and view the explainer dashboard of a model :
- Step 1 : Close/git Pull the repo
- Step 2 : Activate python virtual environment 
- Step 3 : Set InterSystems Cloud SQL connection parameters
- Step 4 : Running Jupyter notebook
  - Step 4.1 : Explore USA housing (for USA housing price Prediction)
  - Step 4.2 : Create table and import data
  - Step 4.3 : Create Model
  - Step 4.4 : Train Model
  - Step 4.5 : Validate Model
  - Step 4.6 : Predict Model
- Step 5 : Run Web Application for prediction   
- Step 6 : Explore the Explainer dashboard

## Step 1 : Close/git Pull the repo
So Let us start with first Step

Create folder and Clone/git pull the repo into any local directory
```
git clone https://github.com/mwaseem75/iris-mlm-explainer.git
```

## Step 2 : Activate python virtual environment 
Repository already contains python virtual environment folder (venv) along with all the required libraries.

All we need is to just activate the environment
On Unix or MacOS:
```
$ source venv/Scripts/activate
```
On Windows:
```
venv\scripts\activate
```
## Step 3 : Set InterSystems Cloud SQL connection parameters
Repo contains config.py file. Just open and set the parameters
![image](https://user-images.githubusercontent.com/18219467/232424168-3fd4ce14-2a78-44bc-a42b-c65909d9696a.png)

Put same values used in InterSystems Cloud SQL
![image](https://user-images.githubusercontent.com/18219467/232485432-4b100781-1127-45b0-b3d8-95570124d977.png)

## Step 4 : Running Jupyter notebook
Repo contains USA_Housing_train.csv and USA_Housing_validate.csv files under datasets folder, from which we will create tables and import data.

We will use USAHousingModelNotebook.ipynb notebook for next steps.

Repo also contains Jupyter notebook. In order to run it, just run runnotebook.bat under venv environment
```
runnotebook
```
![image](https://user-images.githubusercontent.com/18219467/232427181-21b2c7e3-3de8-40fb-8111-4b86a9042039.png)

Navigate to [http://localhost:8888/](http://localhost:8888/) to run the notebook
open USAHousingModelNotebook.ipynb notebook by clicking on it
![image](https://user-images.githubusercontent.com/18219467/232428806-89ba6cd3-8e49-4001-ae0d-f1f8e6873540.png)

It will open the notebook
![image](https://user-images.githubusercontent.com/18219467/233067990-cc24b4d2-3cce-4650-9f0e-d9e8f2418fee.png)

**NOTE : Make sure to select venv kernal by selecting main menu Kernal>Change kernal>venv**, so that notebook will use virtual environment libraries

![image](https://user-images.githubusercontent.com/18219467/232429659-cb4366e9-c14d-41fd-8408-e8447cea4710.png)

NOTE : Run the cells in sequence by just clicking the small arrow
![image](https://user-images.githubusercontent.com/18219467/232431439-8aaa7eac-900b-4cc8-9cca-ec6a44bb7920.png)

## Step 4.1 : Explore USA housing (for USA housing price Prediction)
![image](https://user-images.githubusercontent.com/18219467/233324394-ca5691b5-ef4e-4062-bb0e-612554d8e96c.png)

## Step 4.2 : Create table and import data
![image](https://user-images.githubusercontent.com/18219467/233068671-d5655948-a6df-4dd4-9c05-4832d0091de2.png)

## Step 4.3 : Create Model
![image](https://user-images.githubusercontent.com/18219467/233068824-6a257402-58e5-45e2-8f10-3b1b2588c758.png)


## Step 4.4 : Train Model
![image](https://user-images.githubusercontent.com/18219467/233068922-d5d5247e-5333-4393-a67d-17ffe3740577.png)


## Step 4.5 : Validate Model
![image](https://user-images.githubusercontent.com/18219467/233069090-99826b11-0a7f-48eb-b26c-d8f1df61cb82.png)
![image](https://user-images.githubusercontent.com/18219467/232436385-9df76a7c-fc0f-46d8-b5bf-3c062cc2b7e6.png)

## Step 4.6 : Do a Prediction
![image](https://user-images.githubusercontent.com/18219467/232437235-7ba99b14-3f72-47ab-b644-fd995c37cca8.png)

## Step 5 : Run Web Application for prediction   
Run the below command in virtual environment to start our main application
```
python app.py
```
![image](https://user-images.githubusercontent.com/18219467/233229144-4ecac12f-15b4-4318-a6ea-0ad6790038ae.png)

Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to run the application

![image](https://user-images.githubusercontent.com/18219467/233230031-63c27a25-910c-4b16-9a5a-9466f2e57354.png)

Enter Age of house, No of rooms, No of bedroom and Area population to get the prediction 


## Step 6 : Explore the Explainer dashboard
Finaly, run the below command in virtual environment to start our main application
```
python expdash.py
```
![image](https://user-images.githubusercontent.com/18219467/232438579-26fc0a30-9f95-4df1-81ef-7f24270316c5.png)
![image](https://user-images.githubusercontent.com/18219467/232478449-557091da-3a7d-4534-bd0f-13c12e682e4c.png)
![image](https://user-images.githubusercontent.com/18219467/232478562-70200f16-4161-4738-bf13-fd043a21d194.png)

Navigate to [http://localhost:8050/](http://localhost:8050/) to run the application

![image](https://user-images.githubusercontent.com/18219467/233049477-3c62aa02-952e-4ea1-8334-699f8c8eb215.png)


Application will list all the trained models along with our USAHousingPriceModel. Navigate to "go to dashboard" hyperlink to view model explainer

Feature Importances. Which features had the biggest impact?
![image](https://user-images.githubusercontent.com/18219467/232486985-1719d884-295c-4521-a5cd-85ac034eded9.png)

Quantitative metrics for model performance, How close is the predicted value to the observed?
![image](https://user-images.githubusercontent.com/18219467/232487163-cbaceee4-54c7-4b7e-a3c7-c775cb873419.png)

Prediction and How has each feature contributed to the prediction?
![image](https://user-images.githubusercontent.com/18219467/232487390-81a06116-ac72-495c-9b1d-be117f69ff08.png)

Adjust the feature values to change the prediction
![image](https://user-images.githubusercontent.com/18219467/232487500-0c772ce6-b665-40ab-8316-ee5cdf43f3c7.png)

Shap Summary, Ordering features by shap value
![image](https://user-images.githubusercontent.com/18219467/232487656-d2a5bf90-c09b-45b0-b05c-0a1f6570d2cb.png)

Interactions Summary,Ordering features by shap interaction value
![image](https://user-images.githubusercontent.com/18219467/232487941-c9f4b9a3-d727-4895-887a-68b825a2bb6b.png)

Decision Trees, Displaying individual decision trees inside Random Forest
![image](https://user-images.githubusercontent.com/18219467/232488582-99b93bb2-5017-4670-a85b-27d19860cc92.png)


## Credits
This application is derived from the [isc-cloud-sql-python-demo](https://openexchange.intersystems.com/package/isc-cloud-sql-python-demo) template by @Evgeny Shvarov

Thanks
