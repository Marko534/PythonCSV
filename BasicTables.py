import GenerateSQLTables as DB
import pandas as pd
import numpy as np
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, Session

engine = create_engine(
    'mssql://@MARKO-ILIOSKI/CSVData?driver=SQL Server Native Client 11.0', echo=True, future=True)

session = Session(engine)

Train = pd.read_csv('train.csv')
Train.drop_duplicates(inplace=True)

for gender in Train['Gender']:
    session.add(DB.Gender(Gender = gender))
    
session.commit()
    