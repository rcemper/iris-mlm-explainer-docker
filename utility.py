import intersystems_iris.dbapi._DBAPI as iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import config

#Connect to IS Cloud SQL
def get_db_connection():
    host = config.HOST
    port = config.PORT
    namespace = config.NAMESPACE
    username = config.IRIS_USERNAME
    password = config.IRIS_PASSWORD

    conn = iris.connect(host, port, namespace, username, password)
    return conn

#Get columns list
def get_cols(description):
    ds_cols = []
    for item in description:
        ds_cols.append(item[0])
    return ds_cols

#Split train and test data 
def get_model_train_test(model_type,model_query,perdict_col):
    connection = get_db_connection()
    cur = connection.cursor()
    cur.execute(model_query)
    data = cur.fetchall()
    df = pd.DataFrame (data = data, columns = get_cols(cur.description))
    #convert categorical variable to numeric in case of model_type is classification
    if model_type == "classification":
        ord_enc = OrdinalEncoder()
        df[perdict_col] = ord_enc.fit_transform(df[[perdict_col]])        

    X = df.drop(columns=[perdict_col])
    y = df[perdict_col]  
    # using the train test split function
    X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.20)
    #close cursor and connection 
    if cur:
        cur.close()
    if connection:
        connection.close()
    return X_train, y_train, X_test, y_test

#Get validation metrics from IS SQL Cloud
def get_validation_metrics(model_name,validation_runname):
    connection = get_db_connection()
    cur = connection.cursor()
    #get MSE
    stat = "SELECT METRIC_VALUE FROM INFORMATION_SCHEMA.ML_VALIDATION_METRICS where MODEL_NAME = '"+ model_name +"' AND VALIDATION_RUN_NAME = '"+ validation_runname +"' AND METRIC_NAME = 'MSE'"
    cur.execute(stat)
    data = cur.fetchall()
    mse = str(data[0][0])
    #get RMSE
    stat = "SELECT METRIC_VALUE FROM INFORMATION_SCHEMA.ML_VALIDATION_METRICS where MODEL_NAME = '"+ model_name +"' AND VALIDATION_RUN_NAME = '"+ validation_runname +"' AND METRIC_NAME = 'RMSE'"
    cur.execute(stat)
    data = cur.fetchall()
    rmse = str(data[0][0])
    #get Variance
    stat = "SELECT METRIC_VALUE FROM INFORMATION_SCHEMA.ML_VALIDATION_METRICS where MODEL_NAME = '"+ model_name +"' AND VALIDATION_RUN_NAME = '"+ validation_runname +"' AND METRIC_NAME = 'Variance'"
    cur.execute(stat)
    data = cur.fetchall()
    var = str(data[0][0])
    #get R2
    stat = "SELECT METRIC_VALUE FROM INFORMATION_SCHEMA.ML_VALIDATION_METRICS where MODEL_NAME = '"+ model_name +"' AND VALIDATION_RUN_NAME = '"+ validation_runname +"' AND METRIC_NAME = 'R2'"
    cur.execute(stat)
    data = cur.fetchall()
    r2 = str(data[0][0])
    #close cursor and connection 
    if cur:
        cur.close()
    if connection:
        connection.close()
    return mse,rmse,var,r2
