#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:55:14 2021

@author: jasonti
"""

def split_data(x_in, y_in, split_fraction):
    #training test split
    from sklearn.model_selection import train_test_split
    X_train_t, X_test_t, y_train_t, y_test_t = train_test_split(
        x_in, y_in, test_size=split_fraction, random_state=42)
    return X_train_t, X_test_t, y_train_t, y_test_t


def split_data(x_in, y_in, split_fraction):
    #training test split
    from sklearn.model_selection import train_test_split
    X_train_t, X_test_t, y_train_t, y_test_t = train_test_split(
        x_in, y_in, test_size=split_fraction, random_state=42)
    return X_train_t, X_test_t, y_train_t, y_test_t


def stem_fun(var):
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    processed_text = [stemmer.stem(word) for word in var.split()]
    processed_text = ' '.join(processed_text)
    return processed_text

def perf_metrics(model_in, x_in, y_true):
    #How well did this model perform?
    from sklearn.metrics import precision_recall_fscore_support
    y_pred = model_in.predict(x_in)
    metrics = precision_recall_fscore_support(
        y_true, y_pred, average='weighted')
    return metrics

def my_rf(x_in, y_in, out_in):
    from sklearn.ensemble import RandomForestClassifier
    my_rf = RandomForestClassifier(random_state=123)
    my_rf.fit(x_in, y_in) #model is trained
    write_pickle(out_in, "rf.pkl", my_rf)
    return my_rf

def split_data(x_in, y_in):
    #training test split
    from sklearn.model_selection import train_test_split
    X_train_t, X_test_t, y_train_t, y_test_t = train_test_split(
        x_in, y_in, test_size=0.20, random_state=42)
    return X_train_t, X_test_t, y_train_t, y_test_t


def open_pickle(path_in, file_name):
    import pickle
    tmp = pickle.load(open(path_in + file_name, "rb"))
    return tmp

def write_pickle(path_in, file_name, var_in):
    import pickle
    pickle.dump(var_in, open(path_in + file_name, "wb"))
