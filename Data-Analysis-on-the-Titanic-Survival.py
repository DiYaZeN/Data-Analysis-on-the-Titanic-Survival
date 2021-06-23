import numpy as np
import pandas as pd

df=pd.DataFrame(pd.read_csv('C:\Users\Minol Amarakoon\Desktop\New folder (2)\ train.csv'))

################################################_________Introduction_________################################################

shapedf=df.shape #stores the number of columns and number of rows in the dataframe
print(f"{shapedf}\n")

print("****Conclusion on data set****\n")
print(f"**These are the details about {shapedf[0]} passengers.") #Output the number of rows in the dataframe
print(f"**And there are {shapedf[1]} categorized data about each one of them.\n") #Output the number of columns in the dataframe

###############################################################################################################################
sumofnull=df.isnull().sum()

print(f"{sumofnull}\n")

drop_col= sumofnull[df.isnull().sum()>(df.shape[0]*35/100)]

print(f"{drop_col}\n")

print(f"****Conclusion on data set****\n \n**Data is unavailable for {drop_col[0]} rows in {drop_col.index[0]}.\n")

df.drop(drop_col.index, axis=1,inplace=True) #dropping the cabin column
print(f"****Rest of null values in DataFrame\n \n{df.isnull().sum()}\n") #updated dataframe
###############################################################################################################################

#other two columns which have null values are Age and Embarked
print(f"Data Type of Age is {df['Age'].dtype}\n")
print(f"Data Type of Embarked is {df['Embarked'].dtype}\n")

###############################################################################################################################

df.Age.fillna(df.Age.mean(), inplace=True)#update the null values in the Age Column with the mean of the values in the entire Age column
print(f"****Conclusion on age is,****\n**The Average age of the passengers is {round(df.Age.mean())}\n")
###############################################################################################################################


print(f"****Rest of null values in DataFrame\n \n{df.isnull().sum()}\n") #updated dataframe

print(f"{df.Embarked.describe()}\n")#describe the Embarked

hishestFreqInEmbark=df.Embarked.describe()
df.Embarked.fillna(hishestFreqInEmbark.top,inplace=True)#update the null values in the Embarked Column with the value of the highest frequency value in the entire Embarked column

print(f"****Rest of null values in DataFrame\n \n{df.isnull().sum()}\n") #updated dataframe

print("So there are no more null values\n\n")
###############################################################################################################################


df['FamilySize']= df['SibSp']+df['Parch']+1 #family size with the passenger

df.drop(['SibSp','Parch'], axis=1,inplace=True) #dropping the 'SibSp' and 'Parch' columns

print(f"{df.corr()}\n")#corelation with the families

print("****Conlcusion\n**So according to the corelation of the considered data,it indicates that survival wasn't depended on the Size of the Family\n")

###############################################################################################################################


df['Alone']=[1 if df['FamilySize'][i]==1 else 0 for i in df.index]# if the family size is equal to 1 that means he is there alone, and other value is he is not alone 
             
print(f"{df.head()}\n")

###############################################################################################################################

print(f"{df.groupby(['Alone'])['Survived'].mean()}\n")

print("****Conclusion\n**So according to that there are greater chance of surviving if the passenger is not alone\n\n")
###############################################################################################################################

print(f"{df[['Alone','Fare']].corr()}\n")
print("****Conclusion\n**So according to that the person is alone,the ticket price probably be higher\n\n")

###############################################################################################################################

df['Gender']=[1 if df['Sex'][i]=="male" else 0 for i in df.index  ]

GenderGrouped=df.groupby(["Gender"])['Survived'].mean()
print(f"{GenderGrouped}\n")

print("****Conclusion\n**So according to that if the person is a female,there is a higher chance of surviving \n\n")
###############################################################################################################################

GroupedEmbarked=df.groupby(['Embarked'])['Survived'].mean()
print(f"{GroupedEmbarked}\n")

print("****Conclusion\n**So according to that if the person is  embarked under the code 'C' ,there is the highest chance of surviving \n\n")
print("****Conclusion\n**So according to that if the person is  embarked under the code 'S' ,there is the Lowest chance of surviving \n\n")

##############################################__________End_________##########################################################
