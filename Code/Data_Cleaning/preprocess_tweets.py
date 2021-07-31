#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 07:57:28 2021

@author: jasonti
"""

from utils import *
import pandas as pd

#Replace both paths with the one on your machine 
tweet_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/tweets/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

tweet = open_pickle(output_pickle_path, "tweets.pkl")


# tweet["dict"]=tweet["re_sw"].apply(dictionary_check)
# tweet["clean_text"] = tweet["text"].apply(clean_text)

# tweet["re_sw"] = tweet["clean_text"].apply(rem_sw)




# write_pickle(output_pickle_path, "tweets.pkl", tweet)



# tweet = tweet.drop(columns=['index'])

# tweet["date"] = tweet['timestamp'].apply(
#     lambda x: str(x)[0:10]).apply(fix_data)

# dt = pd.to_datetime("2019-01-01")

# tweet=tweet[(tweet['date'] >= dt)].reset_index()






# translate_text=[]
# translator=Translator()
# for i in tweet['text']:
#     translator.raise_Exception = True
#     translate_text.append(translator.translate(i, dest='en'))
