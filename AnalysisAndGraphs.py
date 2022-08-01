import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


Train = pd.read_csv('train.csv')
Train.drop_duplicates(inplace=True)

TrainWithoutNull = Train
Product_Category_1 = TrainWithoutNull['Product_Category_1'].unique()

for i in Product_Category_1:
    Product_Category_1Mean = TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] == i].mean(
    )
    TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] ==
                                               i] = TrainWithoutNull['Product_Category_2'].loc[TrainWithoutNull['Product_Category_1'] == i].fillna(value=Product_Category_1Mean)

TrainWithoutNull['Product_Category_2'] = TrainWithoutNull['Product_Category_2'].round(
    0)
TrainWithoutNull['Product_Category_2'] = TrainWithoutNull['Product_Category_2'].fillna(
    value=0)

Product_Category_2 = TrainWithoutNull['Product_Category_2'].unique()


for i in Product_Category_1:
    for j in Product_Category_2:
        Product_Category_2Mean = TrainWithoutNull['Product_Category_3'].loc[(
            TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)].mean()
        TrainWithoutNull['Product_Category_3'].loc[(TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)] = TrainWithoutNull['Product_Category_3'].loc[(
            TrainWithoutNull['Product_Category_1'] == i) & (TrainWithoutNull['Product_Category_2'] == j)].fillna(value=Product_Category_2Mean)

TrainWithoutNull['Product_Category_3'] = TrainWithoutNull['Product_Category_3'].round(
    0)
TrainWithoutNull['Product_Category_3'] = TrainWithoutNull['Product_Category_3'].fillna(
    value=0)

#Sreduvanje Outliers
Q1_Purchase = TrainWithoutNull['Purchase'].quantile(0.25)
Q3_Purchase = TrainWithoutNull['Purchase'].quantile(0.75)

IQR_Purchase = Q3_Purchase - Q1_Purchase

OutlierFilter = np.logical_or(TrainWithoutNull['Purchase'] < (Q1_Purchase - 1.5 * IQR_Purchase),
                              TrainWithoutNull['Purchase'] > (Q3_Purchase + 1.5 * IQR_Purchase))
Outliers = TrainWithoutNull[OutlierFilter]
TrainWithoutOutliers = TrainWithoutNull[~OutlierFilter]


def histogramPrice():
    Bins = range(0, 21400, 1000)
    plt.hist(TrainWithoutOutliers['Purchase'], bins=Bins, color='#3495eb')
    plt.xticks(Bins[::3])
    plt.title("Histogram for Purchase")
    plt.xlabel('Amount spent')
    plt.ylabel('Number of people')
    plt.show()


def boxPlotGender():
    plt.boxplot(TrainWithoutOutliers['Purchase'].loc[TrainWithoutOutliers['Gender'] == 'M'], positions=[
                1], labels=['Men'])
    plt.boxplot(TrainWithoutOutliers['Purchase'].loc[TrainWithoutOutliers['Gender'] == 'F'], positions=[
                2], labels=['Women'])
    plt.xlabel('Sex')
    plt.ylabel('Total Spent')
    plt.show()


def boxPlotAge():
    Ages = TrainWithoutOutliers['Age'].unique()
    Ages.sort()
    print(Ages)
    i = 0
    for AgeGroup in Ages:
        plt.boxplot(TrainWithoutOutliers['Purchase'].loc[TrainWithoutOutliers['Age'] == AgeGroup], positions=[
                    i], labels=[AgeGroup])
        i = i + 1
    plt.xlabel('Age Group')
    plt.ylabel('Total Spent')
    plt.show()


def pieGender():
    fig1, ax1 = plt.subplots()
    Sizes = [TrainWithoutOutliers['Gender'].loc[TrainWithoutOutliers['Gender'] == 'M'].count(),
             TrainWithoutOutliers['Gender'].loc[TrainWithoutOutliers['Gender'] == 'F'].count()]
    ax1.pie(Sizes, explode=[0, 0.1], labels=[
            'Male', 'Female'], autopct='%1.1f%%',  shadow=True)
    ax1.axis('equal')
    plt.title('Gender Pie chart')
    plt.show()


def histogramMaritalStatus():
    plt.hist(TrainWithoutOutliers['Marital_Status'], bins=[0, .45,  .55, 1])
    plt.xticks([0, 1])
    plt.title("Histogram for Marital Status")
    plt.xlabel(' Marital Status')
    plt.ylabel('Number of people')
    plt.show()


def pieCityCategory():
    fig1, ax1 = plt.subplots()
    Sizes = [TrainWithoutOutliers['City_Category'].loc[TrainWithoutOutliers['City_Category'] == 'A'].count(),
             TrainWithoutOutliers['City_Category'].loc[TrainWithoutOutliers['City_Category'] == 'B'].count(
    ),
        TrainWithoutOutliers['City_Category'].loc[TrainWithoutOutliers['City_Category'] == 'C'].count()]
    ax1.pie(Sizes, labels=['A', 'B', 'C'], autopct='%1.1f%%',  shadow=True)
    ax1.axis('equal')
    plt.title('City  category Pie Chart')
    plt.show()


def scaterPlot():
    Gender = []
    for IsGender in TrainWithoutOutliers['Gender']:
        if IsGender == 'M':
            Gender.append(0)
        elif IsGender == 'F':
            Gender.append(1)
    Ages = TrainWithoutOutliers['Age'].unique()
    Ages.sort()
    plt.scatter(TrainWithoutOutliers['Occupation'],
                TrainWithoutOutliers['Purchase'],  c=Gender)
    plt.show()


def CorrelationMatrix():
    import seaborn as sn
    NewMatrix = TrainWithoutOutliers.corr()
    sn.heatmap(NewMatrix, annot=True)
    plt.show()


CorrelationMatrix()
