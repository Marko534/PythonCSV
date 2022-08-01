SELECT * FROM Gender
SELECT * FROM Age
SELECT * FROM Occupation
SELECT * FROM CityCategory
SELECT * FROM StayInCurrentCityYears
SELECT * FROM MaritalStatus
SELECT * FROM ProductCategory1
SELECT * FROM ProductCategory2
SELECT * FROM ProductCategory3

DELETE FROM Gender
DELETE FROM Age
DELETE FROM Occupation
DELETE FROM CityCategory
DELETE FROM StayInCurrentCityYears
DELETE FROM MaritalStatus
DELETE FROM ProductCategory1
DELETE FROM ProductCategory2
DELETE FROM ProductCategory3

DBCC CHECKIDENT (Gender, RESEED, 0)
DBCC CHECKIDENT (Age, RESEED, 0)
DBCC CHECKIDENT (Occupation, RESEED, 0)
DBCC CHECKIDENT (CityCategory, RESEED, 0)
DBCC CHECKIDENT (StayInCurrentCityYears, RESEED, 0)
DBCC CHECKIDENT (MaritalStatus, RESEED, 0)
DBCC CHECKIDENT (ProductCategory1, RESEED, 0)
DBCC CHECKIDENT (ProductCategory2, RESEED, 0)
DBCC CHECKIDENT (ProductCategory3, RESEED, 0)