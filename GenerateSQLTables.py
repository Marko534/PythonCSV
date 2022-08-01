import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship


engine = create_engine(
    'mssql://@MARKO-ILIOSKI/CSVData?driver=SQL Server Native Client 11.0', echo=True, future=True)
Base = declarative_base()


class Gender(Base):
    __tablename__ = "Gender"
    GengerId = Column(Integer, primary_key=True)
    Gender = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates='gender')


class Age(Base):
    __tablename__ = "Age"
    AgeId = Column(Integer, primary_key=True)
    Age = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates='age')


class Occupation(Base):
    __tablename__ = "Occupation"
    OccupationId = Column(Integer, primary_key=True)
    Occupation = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates='Occupation')


class CityCategory(Base):
    __tablename__ = "CityCategory"
    CityCategoryId = Column(Integer, primary_key=True)
    CityCategory = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates='cityCategory')


class StayInCurrentCityYears(Base):
    __tablename__ = "StayInCurrentCityYears"
    StayInCurrentCityYearsId = Column(Integer, primary_key=True)
    StayInCurrentCityYears = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates='stayInCurrentCityYears')


class MaritalStatus(Base):
    __tablename__ = "MaritalStatus"
    MaritalStatusId = Column(Integer, primary_key=True)
    MaritalStatus = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates='maritalStatus')


class User(Base):
    __tablename__ = "User"
    UserId = Column(Integer, primary_key=True)
    Id = Column(Integer)
    GenderId = Column(Integer, ForeignKey('Gender.GengerId'))
    AgeId = Column(Integer, ForeignKey('Age.AgeId'))
    OccupationId = Column(Integer, ForeignKey('Occupation.OccupationId'))
    CityCategoryId = Column(Integer, ForeignKey('CityCategory.CityCategoryId'))
    StayInCurrentCityYearsId = Column(Integer, ForeignKey(
        'StayInCurrentCityYears.StayInCurrentCityYearsId'))
    MaritalStatusId = Column(Integer, ForeignKey(
        'MaritalStatus.MaritalStatusId'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    gender = relationship('Gender', back_populates='user')
    age = relationship('Age', back_populates='user')
    Occupation = relationship('Occupation', back_populates='user')
    cityCategory = relationship('CityCategory', back_populates='user')
    stayInCurrentCityYears = relationship(
        'StayInCurrentCityYears', back_populates='user')
    maritalStatus = relationship('MaritalStatus', back_populates='user')

    receipt = relationship('Receipt', back_populates='user')


class ProductCategory1(Base):
    __tablename__ = "ProductCategory1"
    ProductCategory1Id = Column(Integer, primary_key=True)
    ProductCategory1 = Column(Integer())
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    product = relationship('Product', back_populates='productCategory1')


class ProductCategory2(Base):
    __tablename__ = "ProductCategory2"
    ProductCategory2Id = Column(Integer, primary_key=True)
    ProductCategory2 = Column(Integer())
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    product = relationship('Product', back_populates='productCategory2')


class ProductCategory3(Base):
    __tablename__ = "ProductCategory3"
    ProductCategory3Id = Column(Integer, primary_key=True)
    ProductCategory3 = Column(Integer())
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    product = relationship('Product', back_populates='productCategory3')


class Product (Base):
    __tablename__ = "Product"
    ProductId = Column(Integer, primary_key=True)
    ProductCategory1Id = Column(Integer, ForeignKey(
        'ProductCategory1.ProductCategory1Id'))
    ProductCategory2Id = Column(Integer, ForeignKey(
        'ProductCategory2.ProductCategory2Id'))
    ProductCategory3Id = Column(Integer, ForeignKey(
        'ProductCategory3.ProductCategory3Id'))
    Price = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    productCategory1 = relationship(
        'ProductCategory1', back_populates='product')
    productCategory2 = relationship(
        'ProductCategory2', back_populates='product')
    productCategory3 = relationship(
        'ProductCategory3', back_populates='product')

    receipt = relationship('Receipt', back_populates='product')


class Receipt(Base):
    __tablename__ = "Receipt"
    ReceiptId = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey('User.UserId'))
    ProductId = Column(Integer, ForeignKey('Product.ProductId'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship('User', back_populates='receipt')
    product = relationship('Product', back_populates='receipt')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    import BasicTables 
