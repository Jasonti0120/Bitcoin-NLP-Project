#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:43:28 2021

@author: jasonti
"""
from utils import *
import pandas as pd

#Replace with your own
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

BitTweets = open_pickle(output_pickle_path, "BTweets.pkl")

BitTweets_tf = create_tf_idf(BitTweets['sw_dictionary'], 1, 1)

# BitTweets_vc = create_vec(BitTweets['sw_dictionary'], 1, 1)

score_dataframe(BitTweets_tf)
