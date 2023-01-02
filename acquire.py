## IMPORTS

import os

import pandas as pd

from pydataset import data

from env import host, username, password, sql_connexion





## FUNCTION TO CONNECT TO THE MYSQL SERVER

def sql_connexion(db, user = username, host = host, password = password):
    
    '''
    This function connects to the SQL database,
    allowing for the retrieval of remote data.
    '''
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
    
    
    
    
## TELCO FUNCTION TO ACQUIRE THE DATASET FROM SQL
    

def get_telco_data(df):
    
    '''
    This function retrieves Telco data either from a .csv, 
    if the .csv is held locally, or pulls it from SQL 
    in the case that it's held remotely.
    '''
    
    if os.path.isfile('file.csv'):
        
        return pd.read_csv('file.csv')
    
    else:
        
        url = df('telco_churn')
    
        query = '''
        SELECT * 
        FROM customers
        JOIN contract_types 
            USING (contract_type_id)
        JOIN internet_service_types
            USING (internet_service_type_id)
        JOIN payment_types
            USING (payment_type_id)
                '''
        telco_df = pd.read_sql(query, url)
        
        telco_df.to_csv('telco_churn.csv')
        
    return telco_df
    