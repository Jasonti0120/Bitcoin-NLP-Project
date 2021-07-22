#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:51:20 2021

@author: jasonti
"""

from utils import *
import pandas as pd

#Replace both paths with the one on your machine 
tweet_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/tweets/"
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

EM_tweet = open_pickle(output_pickle_path, "EM_tweet.pkl")
Doge = open_pickle(output_pickle_path, "doge.pkl")

#Unify the date
EM_tweet["date"]=pd.to_datetime(EM_tweet['date'])
Doge["date"]=pd.to_datetime(Doge['Date'])
Doge=Doge.drop(columns=['Date'])

#merge original EM(clean text) with Doge price
m1 = pd.merge(left=EM_tweet, right=Doge, on="date")
write_pickle(output_pickle_path, "MEmDogeOriginal.pkl", m1)


#merge tf_idf EM tweet with Doge price
temp = create_tf_idf(EM_tweet['sw_dictionary'], 1, 1)
temp["date"] = EM_tweet["date"]
m2 = pd.merge(left=temp, right=Doge, on="date")
write_pickle(output_pickle_path, "MEmDoge_tf_idf.pkl", m2)

#merge vector count EM tweet with Doge price
cur = create_vec(EM_tweet['sw_dictionary'], 1, 1)
cur["date"] = EM_tweet["date"]
m3 = pd.merge(left=cur, right=Doge, on="date")
write_pickle(output_pickle_path, "MEmDoge_VC.pkl", m3)