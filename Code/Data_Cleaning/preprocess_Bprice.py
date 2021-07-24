#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 07:31:10 2021

@author: jasonti
"""

from utils import *
import pandas as pd

#Replace both paths with the one on your machine 
tweet_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/tweets/"
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

Bit = pd.read_csv(price_path + 'Bitcoin_price.csv')

Bit["Date"] = Bit["Open_Time"]
Bit["Date"]=pd.to_datetime(Bit['Date'])

write_pickle(output_pickle_path, "Bprice.pkl", Bit)