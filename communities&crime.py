# -*- coding: utf-8 -*-
"""Communities&Crime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1InF-g-3UhVdBCamnyiffN2C3yggto-tz

Analysing the dataset: Communities and Crime
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pylab
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from google.colab import drive
drive.mount("/content/gdrive")

pd.set_option('display.max_rows', 20)
text=pd.read_csv('/content/gdrive/My Drive/IDS Report/communitiesFINAL.csv')

text=text.replace('?',float("NAN"))
text

text.columns

text.head()

text.info()

text.shape

stat=pd.read_csv('/content/gdrive/My Drive/IDS Report/Summary_Stat.txt',header=None)
stat

df1 = text.iloc[:,0:20]
df2 = text.iloc[:,20:40]
df3 = text.iloc[:,40:60]
df4 = text.iloc[:,60:80]
df5 = text.iloc[:,80:100]
df6 = text.iloc[:,100:120]
df7 = text.iloc[:,120:]
sns.heatmap(df1.sample(250).isnull(),yticklabels=False)
plt.show()
sns.heatmap(df2.sample(250).isnull(),yticklabels=False)
plt.show()
sns.heatmap(df3.sample(250).isnull(),yticklabels=False)
plt.show()
sns.heatmap(df4.sample(250).isnull(),yticklabels=False)
plt.show()
sns.heatmap(df5.sample(250).isnull(),yticklabels=False)
plt.show()
sns.heatmap(df6.sample(250).isnull(),yticklabels=False)
plt.show()
sns.heatmap(df7.sample(250).isnull(),yticklabels=False)
plt.show()

pd.set_option('display.max_rows',None)
text.isnull().sum()

del text['LemasTotReqPerPop']
del text['county']
del text['community']
del text['LemasSwornFT']
del text['LemasSwFTPerPop']
del text['PolicReqPerOffic']
del text['OfficAssgnDrugUnits']
del text['PolicAveOTWorked']
del text['PolicOperBudg']
del text['PctPolicMinor']
del text['NumKindsDrugsSeiz']
del text['LemasPctPolicOnPatr']
del text['LemasGangUnitDeploy']
del text['LemasPctOfficDrugUn']
del text['PolicBudgPerPop']
del text['PolicCars']
del text['PolicPerPop']
del text['PctPolicBlack']
del text['RacialMatchCommPol']
del text['PctPolicHisp']
del text['PctPolicWhite']
del text['LemasSwFTFieldOps']
del text['LemasSwFTFieldPerPop']
del text['LemasTotalReq']
del text['PctPolicAsian']

text.isnull().sum()

text.shape

pd.set_option('display.max_rows',None)
text.mean()

#isko nhi krna hai!!!!!
#x=text['OtherPerCap'].mean()
#y=text['OtherPerCap'].mode()
#z=text['OtherPerCap'].median()
text["OtherPerCap"].median()

display(text.describe())

categorical=list(text.select_dtypes(include=['object']).columns.values)
categorical

text["OtherPerCap"] = text["OtherPerCap"].replace(np.nan, 'none', regex=True)

le=LabelEncoder()
for i in range(0,len(categorical)):
  text[categorical[i]]=le.fit_transform(text[categorical[i]])
  x=1
text.head()

pd.reset_option('display.max_rows', None)
com=text['communityname']
text.sort_values("communityname", inplace = True)
text.drop_duplicates(subset ="communityname", keep = False, inplace = True)
text

c=text.iloc[:,:]
features = list(c)
features.remove("ViolentCrimesPerPop")
X=text[features]
correlation = X.corr()
plt.figure(figsize=(50, 50))
sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")

del text['householdsize']
del text['fold']
del text['numbUrban']
del text['NumUnderPov']
del text['MalePctDivorce']
del text['FemalePctDiv']
del text['PctFam2Par']
del text['PctKids2Par']
del text['PctYoungKids2Par']
del text['PctTeen2Par']
del text['PctWorkMomYoungKids']
del text['PctWorkMom']
del text['NumIlleg']
del text['NumImmig']
del text['PctImmigRecent']
del text['PctImmigRec5']
del text['PctImmigRec8']
del text['PctImmigRec10']
del text['PctRecImmig5']
del text['PctRecImmig8']
del text['PctRecImmig10']
del text['PctLargHouseFam']

c=text.iloc[:,:]
features = list(c)
features.remove("ViolentCrimesPerPop")
X=text[features]
correlation = X.corr()
plt.figure(figsize=(50, 50))
sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")

text['HighCrime']=(text['ViolentCrimesPerPop']>0.1)
text.HighCrime.value_counts().plot(kind="bar")

x=text.HighCrime.value_counts()
x

text.sample(200).hist(column=['state' , 'population' , 'racepctblack' , 'racePctWhite' , 'racePctAsian' ,
'racePctHisp' , 'agePct12t21' , 'agePct12t29' , 'agePct16t24' , 'agePct65up' , 'pctUrban' , 'medIncome' ,
 'pctWWage' , 'pctWFarmSelf' , 'pctWInvInc' , 'pctWSocSec' , 'pctWPubAsst' , 'pctWRetire' ,
'medFamInc' , 'perCapInc' , 'whitePerCap' , 'blackPerCap' , 'indianPerCap' , 'AsianPerCap' , 'OtherPerCap' ,
 'HispPerCap' , 'PctPopUnderPov' , 'PctLess9thGrade' , 'PctNotHSGrad' , 'PctBSorMore' , 'PctUnemployed' ,
  'PctEmploy' , 'PctEmplManu' , 'PctEmplProfServ' , 'PctOccupManu' ,
'PctOccupMgmtProf' , 'MalePctNevMarr' , 'TotalPctDiv' , 'PersPerFam' , 'PctIlleg' , 'PctSpeakEnglOnly' ,
 'PctNotSpeakEnglWell' , 'PctLargHouseOccup' , 'PersPerOccupHous' , 'PersPerOwnOccHous' , 'PersPerRentOccHous' ,
  'PctPersOwnOccup' , 'PctPersDenseHous' , 'PctHousLess3BR' , 'MedNumBR' , 'HousVacant' , 'PctHousOccup' ,
   'PctHousOwnOcc' , 'PctVacantBoarded' , 'PctVacMore6Mos' , 'MedYrHousBuilt' , 'PctHousNoPhone' ,
    'PctWOFullPlumb' , 'OwnOccLowQuart' , 'OwnOccMedVal' , 'OwnOccHiQuart' , 'RentLowQ' , 'RentMedian' ,
     'RentHighQ' , 'MedRent' , 'MedRentPctHousInc' , 'MedOwnCostPctInc' , 'MedOwnCostPctIncNoMtg' ,
      'NumInShelters' , 'NumStreet' , 'PctForeignBorn' , 'PctBornSameState' , 'PctSameHouse85' ,
       'PctSameCity85' , 'PctSameState85' , 'LandArea' , 'PopDens' , 'PctUsePubTrans' ],figsize=(18,18))
pylab.suptitle("Analyzing distribution for the series", fontsize="xx-large")

c=text.iloc[:,:]
features = list(c)
features.remove("ViolentCrimesPerPop")
X=text[features]
correlation = X.corr()
plt.figure(figsize=(50, 50))
sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")

c=text.iloc[:,60:]
correlation = c.sample(100).corr()
plt.figure(figsize=(50, 50))
sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")

x=text['communityname']
x

y=text.sort_values('ViolentCrimesPerPop')
y

c=text.iloc[50:100,:]

plt.figure(figsize=(50, 50))
kx = sns.boxplot(x='ViolentCrimesPerPop', y="communityname", data = c)
kx.set(xlabel='ViolentCrimesPerPop', ylabel='communities', title='crime rate in different communities')

len(text.communityname.unique())

plt.scatter(text.perCapInc, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt per Capita Income")

plt.scatter(text.pctUrban, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt percentage of people living in urban areas")

plt.scatter(text.agePct12t21, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt percentage of population that is 12-21 in age")

plt.scatter(text.agePct12t29, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt percentage of population that is 12-29 in age")

plt.scatter(text.agePct16t24, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt percentage of population that is 16-24 in age")

plt.scatter(text.PctUsePubTrans, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt percent of people using public transit for commuting"
)

sns.barplot(x='communityname', y='ViolentCrimesPerPop', data=text)
plt.xticks(None,None,rotation=90)
t=plt.title('Crime Rate in different communities')

pieLabels = 'True', 'False'
boolean_value = [x[0],x[1]]
figureObject, axesObject = plt.subplots()
# Draw the pie chart
axesObject.pie(boolean_value,labels=pieLabels,autopct='%1.2f',startangle=90)
# Aspect ratio - equal means pie is a circle
axesObject.axis('equal')
plt.show()

sns.barplot(x='communityname', y='agePct16t24', hue='HighCrime',data=text)
plt.xticks(None,None,rotation=90)
t=plt.title('Crime Rate in different communities wrt percentage of population that is 16-24 in age')

plt.scatter(text.racepctblack, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt Race Pct Black")

plt.scatter(text.racePctWhite, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt Race Pct White")

plt.scatter(text.racePctAsian, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt Race Pct Asian")

plt.scatter(text.racePctHisp, text.ViolentCrimesPerPop, alpha=0.1)
plt.title("Violent Crimes Per population wrt Race Pct Hisp")

ax=sns.countplot(x="PctUnemployed" , hue="HighCrime" , data=text)

ax=sns.countplot(x="PctUnemployed" , hue="HighCrime" , data=text)

labels = 'S1', 'S2', 'S3'
sections = [56, 66, 24]
colors = ['c', 'g', 'y']

plt.pie(sections, labels=labels, colors=colors,
        startangle=90,
        explode = (0, 0.1, 0),
        autopct = '%1.2f%%')

plt.axis('equal') # Try commenting this out.
plt.title('Pie Chart Example')
plt.show()