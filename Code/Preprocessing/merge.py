#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:08:10 2021

@author: jasonti
"""

from utils import *
import pandas as pd
from datetime import timedelta, datetime
#Replace both paths with the one on your machine 
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

df_price = pd.read_csv(output_path + "bit_price.csv")

df_price = df_price.drop(columns=['Unnamed: 0'])
df_price["date"]=pd.to_datetime(df_price["date"]).dt.date


df_price["DateIndex"]=df_price["date"]
df_price = df_price.set_index('DateIndex')

df_tweet = pd.read_csv(output_path + "tweets_score.csv")

df_m = pd.DataFrame()

df_m["date"]=pd.to_datetime(df_tweet["date"]).dt.date

df_m["sent_score"]=df_tweet["sent_score"]

df_m["Vol"]=df_tweet["Vol"]

df_m["DateIndex"]=df_m["date"]
df_m = df_m.set_index('DateIndex')

df_m["t-1"]=""
df_m["t-2"]=""
df_m["t-3"]=""
df_m["t-4"]=""
df_m["t-5"]=""
df_m["t-6"]=""
df_m["label"]=""


for i in df_m.date:
    cur = i+timedelta(days=1)
    for j in df_price.date:
        if i == j:
            df_m["t-1"][i]=df_price.loc[j, "t-1"]
            df_m["t-2"][i]=df_price.loc[j, "t-2"]
            df_m["t-3"][i]=df_price.loc[j, "t-3"]
            df_m["t-4"][i]=df_price.loc[j, "t-4"]
            df_m["t-5"][i]=df_price.loc[j, "t-5"]
            df_m["t-6"][i]=df_price.loc[j, "t-6"]
        if cur == j:
            temp = df_price.loc[j, "t-1"]
            if temp > 0:
                df_m["label"][i] = 1
            if temp == 0:
                df_m["label"][i] = 0
            if temp < 0:
                df_m["label"][i] = -1
    
            


df_m = df_m.drop(columns=['date'])
write_pickle(output_pickle_path, "merge3.pkl", df_m)
df_m.to_csv(output_path+"/merge3.csv")