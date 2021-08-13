#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:53:35 2021

@author: jasonti
"""

from utils import *
import pandas as pd

#Replace both paths with the one on your machine 
tweet_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/tweets/"
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"

tweet = pd.read_csv(tweet_path+"tweets.csv")
price = pd.read_csv(price_path+"BTCUSD_day.csv")
