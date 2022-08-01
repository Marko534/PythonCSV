import GenerateSQLTables as DB
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    'mssql://@MARKO-ILIOSKI/CSVData?driver=SQL Server Native Client 11.0', echo=True, future=True)

session = Session(engine)

Train = pd.read_csv('train.csv')
Train.drop_duplicates(inplace=True)
Train['created_date'] = pd.to_datetime('today')

# print (Train[['Gender', 'created_date']])

# Train[['Gender', 'created_date']].to_sql(name = 'Gender', if_exists = 'append', con=engine, index = False )

    # Generates users 
print (Train['User_ID'].unique())
    
    #ZA PROIZVODI
session.commit()
