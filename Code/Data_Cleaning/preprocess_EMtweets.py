#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:37:23 2021

@author: jasonti
"""

from utils import *
import pandas as pd
#Replace both paths with the one on your machine 
the_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/tweets/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"


data = seek_and_clean(the_path, "TweetsElonMusk.csv", "tweet", "new_tweet")

# #Unify the date
data["Date"]=pd.to_datetime(data['date'])


data['rem_sw']=data["new_tweet"].apply(rem_sw)
data["sw_dictionary"]=data.rem_sw.apply(dictionary_check)


write_pickle(output_pickle_path, "EM_tweet.pkl", data)
