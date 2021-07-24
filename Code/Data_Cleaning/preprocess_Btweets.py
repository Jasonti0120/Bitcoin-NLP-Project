#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 07:36:06 2021

@author: jasonti
"""


from utils import *
import pandas as pd

#Replace both paths with the one on your machine 
tweet_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/tweets/"
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

data = pd.read_csv(tweet_path + 'Bitcoin_tweets.csv')

data["date"]=pd.to_datetime(data["date"], errors='coerce')

data["date"]=data["date"].round('min')

data["text"] = data["text"].astype(str)

data["new_tweet"] = data["text"].apply(clean_text)

data['rem_sw']=data["new_tweet"].apply(rem_sw)
data["sw_dictionary"]=data.rem_sw.apply(dictionary_check)



write_pickle(output_pickle_path, "BTweets.pkl", data)