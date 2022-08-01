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

for gender in Train['Gender'].unique():
    session.add(DB.Gender(Gender = gender))
    
for age in Train['Age'].unique():
    session.add(DB.Age(Age = age))
    
for occupation in Train['Occupation'].unique():
    session.add(DB.Occupation(Occupation = int (occupation)))
    
for cityCategory in Train['City_Category'].unique():
    session.add(DB.CityCategory(CityCategory = cityCategory))

for stayInCurrentCityYears in Train['Stay_In_Current_City_Years'].unique():
    session.add(DB.StayInCurrentCityYears(StayInCurrentCityYears = stayInCurrentCityYears))
    
for maritalStatus in Train['Marital_Status'].unique():
    session.add(DB.MaritalStatus(MaritalStatus = str( maritalStatus)))  

session.commit()
    