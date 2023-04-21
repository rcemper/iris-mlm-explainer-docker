from explainerdashboard.datasets import titanic_survive, titanic_fare
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from explainerdashboard import ClassifierExplainer, ExplainerDashboard, ExplainerHub, RegressionExplainer
import dash_bootstrap_components as dbc
import utility

#Establish connection with InterSystems IRIS Cloud
connection = utility.get_db_connection()
#Create cursor 
cur = connection.cursor()
#Execute the cursor to retrieve all the models
cur.execute('SELECT MODEL_NAME,DESCRIPTION,DEFAULT_TRAINING_QUERY,PREDICTING_COLUMN_NAME FROM INFORMATION_SCHEMA.ML_MODELS')
#Fetch all the records in data
data = cur.fetchall()
dblst=[]
#Iterate all the records and check if model is trained
for i in range(len(data)):
    #check if model is trained
    cur.execute("select lower(max(model_type)) from information_schema.ML_TRAINED_MODELS where model_name = '"+data[i][0]+"'")
    data2 = cur.fetchall()
    #if Model type is regression
    if data2[0][0] == 'regression':
        #get splitted train and test data 
        X_train, y_train, X_test, y_test = utility.get_model_train_test(data2[0][0],data[i][2],data[i][3])
        # Select only numerical columns
        numerical_cols = [cname for cname in X_train.columns if X_train[cname].dtype in ['int64', 'float64']]
        X_train = X_train[numerical_cols].copy()
        X_test = X_test[numerical_cols].copy()
        try:
            #Generate model     
            model = RandomForestRegressor(n_estimators=50, max_depth=10).fit(X_train, y_train)
            #Initiate explainer 
            explainer = RegressionExplainer(model, X_test, y_test)
            try:
                #Append exlpaner to the list, so can be added to ExplainerHub
                dblst.append(ExplainerDashboard(explainer,title="Model : "+data[i][0], name="db"+ str(i+1),description=data[i][1]+", Training Query : "+data[i][2]))
            except:
                print("An exception occurred while appending explainer HUB")    
        except:
            print("An exception occurred while generating RandomForestRegressor")    
        

    #If Model type is classification
    elif data2[0][0] == 'classification':
        #get splitted train and test data 
        X_train, y_train, X_test, y_test = utility.get_model_train_test(data2[0][0],data[i][2],data[i][3]) 
        try:
            #Generate model           
            model = RandomForestClassifier().fit(X_train, y_train)
            #Initiate explainer 
            explainer = ClassifierExplainer(model, X_test, y_test)
            try:
                 #Append exlpaner to the list, so can be added to ExplainerHub
                 dblst.append(ExplainerDashboard(explainer,title="Model : "+data[i][0], name="db"+ str(i+1),description=data[i][1]+", Training Query : "+data[i][2]))
            except:
                print("An exception occurred while appending explainer HUB")   
        except:
            print("An exception occurred while generating ClassifierExplainer")   
    
    else:
        pass
    
#close cursor and connection
if cur:
    cur.close() 
if connection:
    connection.close()
#initate ExplanerHub by passing all the explaners
hub = ExplainerHub(dblst, bootstrap=dbc.themes.MORPH, title="InterSystems IRIS Cloud Integrated ML explorer",description="Give your applications direct access to the advanced relational database capabilities of InterSystems IRIS® Data Platform without the burden of provisioning, configuring, and maintaining cloud infrastructure. The IRIS Cloud IntegratedML option lets you define and execute predictive models by applying automated functions directly from SQL, without requiring extensive machine learning expertise.")
#Run application
hub.run()
