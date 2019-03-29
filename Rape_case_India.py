# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:41:50 2019

@author: ROHAN
"""
# import the libraries 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate
from tabulate import tabulate
 
# configure matplotlib to output inline 
%matplotlib inline

#victim of rape in india 
rape_victim = pd.read_csv("C:/Users/ROHAN/Desktop/R PROJECT/New folder/20_Victims_of_rape.csv")

#The data is structured 
rape_victim.head()
print(rape_victim)


# drop the unwanted column  
rape_victim = rape_victim[rape_victim['Subgroup']!= 'Total Rape Victims']

#lets check if the all the rape cases are reported
rape_victim[rape_victim['Victims_of_Rape_Total']!=rape_victim['Rape_Cases_Reported']].head() 

rape_victim['Unreported_Cases'] = rape_victim['Victims_of_Rape_Total']- rape_victim['Rape_Cases_Reported']

#new dataframe

rape_victim[rape_victim['Unreported_Cases'] >0].head()

#ploting un reported rape cases sorted by state

unreported_victims_by_state = rape_victim.groupby('Area_Name').sum()
unreported_victims_by_state.drop('Year',axis = 1,inplace=True)
plt.subplots(figsize = (10, 5))
ct = unreported_victims_by_state[unreported_victims_by_state['Unreported_Cases'] 
                                 > 0]['Unreported_Cases'].sort_values(ascending = False)
# print

ax = ct.plot.bar()
ax.set_xlabel('Area Name')
ax.set_ylabel('Total Number of Unreported Rape Victims from 2001 to 2010')
ax.set_title('Statewise total Unreported Rape Victims throughout 2001 to 2010')
plt.show()

# let's take some general data and plot some simple charts
rape_victims_by_state = rape_victim.groupby('Area_Name').sum()
rape_victims_by_state.drop('Year', axis = 1, inplace = True)
print('Total Rape Victims = ' ,rape_victims_by_state['Rape_Cases_Reported'].sum())
rape_victims_by_state.sort_values(by = 'Rape_Cases_Reported', ascending = False).head()

# let's make a heatmap variable
rape_victims_heatmap = rape_victims_by_state.drop(['Rape_Cases_Reported', 
                                                   'Victims_of_Rape_Total', 
                                                   'Unreported_Cases'], axis = 1)
plt.subplots(figsize = (10, 10))
ax = sns.heatmap(rape_victims_heatmap, cmap="winter")
ax.set_xlabel('Age Group')
ax.set_ylabel('State Name')
ax.set_title('Statewise Victims of Rape Cases based on Age Group')
plt.show()

# let's first plot only the total number of rape cases reported in each state
plt.subplots(figsize = (15, 6))
ct = rape_victims_by_state['Rape_Cases_Reported'].sort_values(ascending = False)
#print(ct)
ax = ct.plot.bar()
#ax = sns.barplot(x = rape_victims_by_state.index, y = rape_victims_by_state['Rape_Cases_Reported'])
ax.set_xlabel('Area Name')
ax.set_ylabel('Total Number of Reported Rape Victims from 2001 to 2010')
ax.set_title('Statewise total Reported Rape Victims throught the Years 2001 to 2010')
plt.show()
print(ct)

ch_rape_victims = rape_victim[rape_victim['Area_Name'] == 'Chhattisgarh']

# let's have a look in the data
ch_rape_victims.head()

