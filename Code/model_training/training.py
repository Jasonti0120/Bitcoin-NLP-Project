#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:48:16 2021

@author: jasonti
"""

from utils import *
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier, plot_tree

#Replace both paths with the one on your machine 
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"
output_pickle_score_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/scores/"

dummy = DummyClassifier()
svc = SVC()
gnb = GaussianNB()
rf = RandomForestClassifier(random_state=123)
dt = DecisionTreeClassifier()
lr = LogisticRegression()
knn = KNeighborsClassifier()


df = open_pickle(output_pickle_path, "merge_15_vol5.pkl")

labels = np.array(df.label.astype('int'))
features= df.drop('label', axis = 1)
features = np.array(features)

result3 = model_score([svc, gnb, lr], features, labels)

result5 = model_score([svc, gnb, rf, lr, knn], features, labels)

result7 = model_score([dummy, svc, gnb, rf, dt, lr, knn], features, labels)

# write_pickle(output_pickle_score_path, "zscore_3models_sr.pkl", result3)
# write_pickle(output_pickle_score_path, "zscore_5models_sr.pkl", result5)
# write_pickle(output_pickle_score_path, "zscore_7models_sr.pkl", result7)





# X_train, X_test, y_train, y_test = split_data(features, labels)

# Random Forest
# cur = []
# for i in range(10):
#     rf_model = my_rf(X_train, y_train, output_pickle_path)
#     rf_metrix = perf_metrics(rf_model, X_test, y_test)
#     cur.append(rf_metrix[0]) 
# print(cur)




    
    
# print(f"RandomForestClassifier test score: {np.mean(cv_rf['test_score'])}")
# # Decision Trees
# dtrees_model = my_dtrees(X_train, y_train, output_pickle_path)
# dtrees_metrix = perf_metrics(dtrees_model, X_test, y_test)

# # Naive Bayes
# nb_model = my_nb(X_train, y_train, output_pickle_path)
# nb_metrix = perf_metrics(nb_model, X_test, y_test)

