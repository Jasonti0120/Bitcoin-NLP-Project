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

#Replace both paths with the one on your machine 
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"


df = open_pickle(output_pickle_path, "merge3.pkl")
sent_score=np.array(df.sent_score.astype('float'))
sent_score = stats.zscore(sent_score)


vol=np.array(df.Vol.astype('int'))
Vol = stats.zscore(vol)

df["sent_score"] = sent_score
df["Vol"] = Vol

write_pickle(output_pickle_path, "merge_z.pkl", df)
df.to_csv(output_path+"/merge_z.csv")