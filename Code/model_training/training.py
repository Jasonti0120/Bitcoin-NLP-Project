#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:48:16 2021

@author: jasonti
"""

from utils import *
import pandas as pd
import numpy as np
#Replace both paths with the one on your machine 
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

df = open_pickle(output_pickle_path, "merge1.pkl")
df = df.drop(columns=['Vol'])
labels = np.array(df.label)
features= df.drop('label', axis = 1)
features = np.array(features)
X_train, X_test, y_train, y_test = split_data(features, labels)


rf_model = my_rf(X_train, y_train, output_pickle_path)

model_metrics = perf_metrics(rf_model, X_test, y_test)