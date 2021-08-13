#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:27:51 2021

@author: jasonti
"""


from utils import *
import pandas as pd

#Replace both paths with the one on your machine 
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_score_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/scores/"


result = open_pickle(output_pickle_score_path, "zscore_3models_sr.pkl")
result2 = open_pickle(output_pickle_score_path, "zscore_5models_sr.pkl")
result3 = open_pickle(output_pickle_score_path, "zscore_7models_sr.pkl")

