# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:50:15 2019

To check the powerof Pandas tool

@author: wflop
"""



import pandas as pd
print("Starting the Pandas testing\n")
print("The installed pandas versions is: " + str(pd.__version__))

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 10157865, 485199])

cities = pd.DataFrame({'City name':city_names,'Population':population})

print("Obtained DataFrame: ")
print(cities)

print('\n'*2)
#Accessing Data:

#Get a single column
print(type(cities['City name'][0]))
print(cities['City name'][0])

print(type(cities[0:2]))

#Read the data from a CSV
california_housing_df = pd.read_csv("california_housing_train.csv", sep=",")

