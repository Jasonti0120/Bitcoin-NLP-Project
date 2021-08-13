#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 23:28:58 2021

@author: jasonti
"""

from utils import *
import pandas as pd
import numpy as np
import scipy.stats as stats
from datetime import timedelta, datetime
#Replace both paths with the one on your machine 
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"


df = open_pickle(output_pickle_path, "merge8.pkl")


for i in df["date"]:
    cur = i+timedelta(days=15)
    score=[]
    vol = []
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    t6=[]
    for j in df["date"]:
        if j < cur and j >=i:
            score.append(df.loc[j, "sent_score"])
            vol.append(df.loc[j, "Vol"])
            t1.append(df.loc[j, "t-1"])
            t2.append(df.loc[j, "t-2"])
            t3.append(df.loc[j, "t-3"])
            t4.append(df.loc[j, "t-4"])
            t5.append(df.loc[j, "t-5"])
            t6.append(df.loc[j, "t-6"])
        if j == cur:
            score.append(df.loc[j, "sent_score"])
            df.loc[cur, "sent_score"]=round(stats.zscore(score)[-1], 4)
            df.loc[cur, "Vol"]=round(stats.zscore(vol)[-1], 4)
            df.loc[cur, "t-1"]=round(stats.zscore(t1)[-1], 4)
            df.loc[cur, "t-2"]=round(stats.zscore(t2)[-1], 4)
            df.loc[cur, "t-3"]=round(stats.zscore(t3)[-1], 4)
            df.loc[cur, "t-4"]=round(stats.zscore(t4)[-1], 4)
            df.loc[cur, "t-5"]=round(stats.zscore(t5)[-1], 4)
            df.loc[cur, "t-6"]=round(stats.zscore(t6)[-1], 4)


# df["Vol_sr"]=""
# #Simple return for Volume
# for i in df.date:
#     cur1 = i+timedelta(days=1)
#     for j in df.date:
#         if j==cur1:
#             df["Vol_sr"][j]=(float(df.loc[j, "Vol"])-float(df.loc[i, "Vol"]))/float(df.loc[i, "Vol"])

# df["Vol"]=df["Vol_sr"]

dt1 = pd.to_datetime("2019-1-15")
for i in df["date"]:
    if i<=dt1:
        df = df.drop([i])

df = df.drop(columns=['date'])


write_pickle(output_pickle_path, "merge_15_vol5.pkl", df)

