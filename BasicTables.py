import GenerateSQLTables as DB
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    'mssql://@MARKO-ILIOSKI/CSVData?driver=SQL Server Native Client 11.0', echo=True, future=True)

session = Session(engine)

Train = pd.read_csv('train.csv')
Train.drop_duplicates(inplace=True)

for gender in Train['Gender'].unique():
    session.add(DB.Gender(Gender=gender))

for age in Train['Age'].unique():
    session.add(DB.Age(Age=age))

for occupation in Train['Occupation'].unique():
    session.add(DB.Occupation(Occupation=int(occupation)))

for cityCategory in Train['City_Category'].unique():
    session.add(DB.CityCategory(CityCategory=cityCategory))

for stayInCurrentCityYears in Train['Stay_In_Current_City_Years'].unique():
    session.add(DB.StayInCurrentCityYears(
        StayInCurrentCityYears=stayInCurrentCityYears))

for maritalStatus in Train['Marital_Status'].unique():
    session.add(DB.MaritalStatus(MaritalStatus=str(maritalStatus)))

for productCategory1 in Train['Product_Category_1'].unique():
    if not np.isnan(productCategory1):
        session.add(DB.ProductCategory1(
            ProductCategory1=int(productCategory1)))

for productCategory2 in Train['Product_Category_2'].unique():
    if not np.isnan(productCategory2):
        session.add(DB.ProductCategory2(
            ProductCategory2=int(productCategory2)))

for productCategory3 in Train['Product_Category_3'].unique():
    if not np.isnan(productCategory3):
        session.add(DB.ProductCategory3(
            ProductCategory3=int(productCategory3)))

session.commit()
