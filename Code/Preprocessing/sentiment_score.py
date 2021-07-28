#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:43:28 2021

@author: jasonti
"""
from utils import *
import pandas as pd
import csv
#Replace with your own
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

BitTweets = open_pickle(output_pickle_path, "Bittweet.pkl")


BitTweets['date'] = pd.to_datetime(BitTweets['date'])
BitTweets = BitTweets.drop(columns=['user_created', 'user_followers', 'user_friends', 'splitted_date', 'length'])
BitTweets=BitTweets.resample('D', on='date').mean()

BitTweets.to_csv(output_path+"/tweets_sentscore_day.csv")
# df = pd.DataFrame()

# df["text"]=BitTweets["text_sw"]

# df.to_csv(output_path+"/swtweets.csv")



# score=[]
# with open (output_path+"/swtweets.csv",'r') as csv_file:
#     reader =csv.reader(csv_file)
#     next(reader) # skip first row
#     n=0
#     for row in reader:
#         score.append(sentiment_scores(row[1]))
#         n+=1
#         if n%1000==0:
#             print(n)

# write_pickle(output_pickle_path, "score.pkl", score)

# var = open_pickle(output_pickle_path, "score.pkl")
# score=[]
# for i in var:
#     score.append(i["compound"])

# BitTweets["sent_score"]=score


# BitTweets.to_csv(output_path+"/tweets_sentscore.csv")

