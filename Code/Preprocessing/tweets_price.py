#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:54:05 2021

@author: jasonti
"""

from utils import *
import pandas as pd
from datetime import timedelta
#Replace both paths with the one on your machine 
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"


df = open_pickle(output_pickle_path, "price.pkl")

dt1 = pd.to_datetime("2018-12-27")
dt2 = pd.to_datetime("2019-05-30")


for i in df.date:
    cur1 = i+timedelta(days=1)
    cur2 = i+timedelta(days=2)
    cur3 = i+timedelta(days=3)
    cur4 = i+timedelta(days=4)
    cur5 = i+timedelta(days=5)
    cur6 = i+timedelta(days=6)
    for j in df.date:
        if j==cur1:
            df["t-1"][j]=(df.loc[j, "price"]-df.loc[i, "price"])
        if j==cur2:
            df["t-2"][j]=(df.loc[j, "price"]-df.loc[i, "price"])
        if j==cur3:
            df["t-3"][j]=(df.loc[j, "price"]-df.loc[i, "price"])
        if j==cur4:
            df["t-4"][j]=(df.loc[j, "price"]-df.loc[i, "price"])
        if j==cur5:
            df["t-5"][j]=(df.loc[j, "price"]-df.loc[i, "price"])
        if j==cur6:
            df["t-6"][j]=(df.loc[j, "price"]-df.loc[i, "price"])

dt1 = pd.to_datetime("2019-01-01")

df=df[(df['date'] >= dt1)].reset_index()
df = df.drop(columns=['DateIndex'])
write_pickle(output_pickle_path, "price_preprocessed.pkl", df)
df.to_csv(output_path+"/bit_price.csv")










price = pd.read_csv(price_path + "BTCUSD_day.csv")

price["date"]=pd.to_datetime(price['Date'])
price["price"]=price["Open"]
price = price.drop(columns=['Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume BTC', 'Volume USD'])


dt1 = pd.to_datetime("2018-12-26")
dt2 = pd.to_datetime("2019-05-30")

price=price[(price['date'] >= dt1)].reset_index()

price=price[(price['date'] <= dt2)].reset_index()

price = price.drop(columns=['level_0', 'index'])

price["DateIndex"]=price["date"]
price = price.set_index('DateIndex')

price["t-1"]=""
price["t-2"]=""
price["t-3"]=""
price["t-4"]=""
price["t-5"]=""
price["t-6"]=""