# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:43:44 2019

@author: wflop
"""


import pandas as pd
import numpy as np



#Get the dataset
california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

#Shuffle the data
california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0


