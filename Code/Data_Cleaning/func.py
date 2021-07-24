#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:38:33 2021

@author: nan
"""

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

def create_tf_idf(df_in, out_in, min_n, max_n):
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pandas as pd
    my_tf_idf = TfidfVectorizer(ngram_range=(min_n, max_n))
    my_tf_idf_text = pd.DataFrame(my_tf_idf.fit_transform(df_in).toarray())
    my_tf_idf_text.columns = my_tf_idf.get_feature_names()
    write_pickle(out_in, "tf_idf.pkl", my_tf_idf)
    return my_tf_idf_text

def create_vec(df_in, out_in, min_n, max_n):
    from sklearn.feature_extraction.text import CountVectorizer
    import pandas as pd
    my_vec = CountVectorizer(ngram_range=(min_n, max_n))
    my_vec_text = pd.DataFrame(my_vec.fit_transform(df_in).toarray())
    my_vec_text.columns = my_vec.get_feature_names()
    write_pickle(out_in, "vec.pkl", my_vec)
    return my_vec_text

def dictionary_check(var_in):
    import enchant
    d = enchant.Dict("en_US")
    tmp = var_in.split()
    tmp = [word for word in tmp if d.check(word)]
    tmp = ' '.join(tmp)
    return tmp

def rem_sw(var_in):
    import nltk
    from nltk.corpus import stopwords
    sw = stopwords.words('english')    
    clean_text = [word for word in var_in.split() if word not in sw]
    clean_text = ' '.join(clean_text)
    return clean_text

def unique_words(var_in):
    tmp = len(set(var_in.split()))
    return tmp

def open_pickle(path_in, file_name):
    import pickle
    tmp = pickle.load(open(path_in + file_name, "rb"))
    return tmp

def write_pickle(path_in, file_name, var_in):
    import pickle
    pickle.dump(var_in, open(path_in + file_name, "wb"))

def clean_text(var_in):
    import re
    tmp = re.sub("[^A-z]+", " ", var_in.lower())
    return tmp

def seek_and_clean(path_in, path_out):
    import pandas as pd
    import os
    the_data = pd.DataFrame()
    for root, dirs, files in os.walk(path_in, topdown=False):
        tmp = root.split("/")[-1]
        for word in files:
            try:
                f = open(root + "/" + word, "r", encoding="utf8")
                tmp_txt = clean_text(f.read())
                if len(tmp_txt) > 0:
                    the_data = the_data.append(
                        {"body": tmp_txt, "label": tmp}, ignore_index=True)
                f .close()
            except:
                print ("ERROR WITH FILE: ", word)
                pass
    write_pickle(path_out, "data.pkl", the_data)
    return the_data