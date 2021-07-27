#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:38:06 2021

@author: jasonti
"""

# sentiment score   
def s_score(df,target,output):
    """

    Parameters
    ----------
    df : target dataframe.
    target : A string: column name for text
    output : A string: column name for sentiment score

    Returns
    -------
    None.

    """
    s_score = []
    for text in df[target]:
        score = sentiment_scores(text)
        s_score.append(score)
    df[output] = s_score
    print('complete')
    
    
def sentiment_scores(sentence):
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    return sentiment_dict

            

def merge_and_csv(var1, var2, temp, path, name, out_path):
    import pandas as pd
    m = pd.merge(left=var1, right=var2, on=temp)
    write_pickle(path, name+"pkl", m)
    m.to_csv(out_path+"/"+name+".csv")
    return m
    
#Vector count & td-idf
def create_tf_idf(df_in, min_n, max_n):
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pandas as pd
    my_tf_idf = TfidfVectorizer(ngram_range=(min_n, max_n))
    my_tf_idf_text = pd.DataFrame(my_tf_idf.fit_transform(df_in).toarray())
    my_tf_idf_text.columns = my_tf_idf.get_feature_names()
    return my_tf_idf_text

def create_vec(df_in, min_n, max_n):
    from sklearn.feature_extraction.text import CountVectorizer
    import pandas as pd
    my_vec = CountVectorizer(ngram_range=(min_n, max_n))
    my_vec_text = pd.DataFrame(my_vec.fit_transform(df_in).toarray())
    my_vec_text.columns = my_vec.get_feature_names()
    return my_vec_text


#cleeaning the text
def dictionary_check(var_in):
    import enchant
    d = enchant.Dict("en_US")
    tmp = var_in.split()
    tmp = [word for word in tmp if d.check(word)]
    tmp = ' '.join(tmp)
    return tmp
 
def rem_sw(var_in):
    from nltk.corpus import stopwords
    sw = stopwords.words('english')    
    clean_text = [word for word in var_in.split() if word not in sw]
    clean_text = ' '.join(clean_text)
    return clean_text

def unique_words(var_in):
    tmp = len(set(var_in.split()))
    return tmp



#write and open pickle 
def open_pickle(path_in, file_name):
    import pickle
    tmp = pickle.load(open(path_in + file_name, "rb"))
    return tmp

def write_pickle(path_in, file_name, var_in):
    import pickle
    pickle.dump(var_in, open(path_in + file_name, "wb"))

def find_row(rowname, head):
    for i in head:
        if i == rowname:
            return True
    return False

#clean the specific row in a file
def seek_and_clean(path_in,filename, rowname, columnname):
    import pandas as pd
    df = pd.read_csv(path_in + filename)
    if find_row(rowname, df.head()):
        df[columnname] = df[rowname].apply(clean_text)
    return df
        

#Clean the text
def clean_text(var_in):
    import re
    tmp = re.sub("[^A-z]+", " ", var_in.lower())
    return tmp

