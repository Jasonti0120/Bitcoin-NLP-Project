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

tweet = open_pickle(output_pickle_path, "tweets_sentscore.pkl")


df1=tweet.groupby(tweet['date'].dt.date)['sent_score'].mean().reset_index()


df2= pd.DataFrame()
df2["Volume"]=tweet.groupby(tweet['date'].dt.date).size()
cur=[]
for i in df2["Volume"]:
    cur.append(i)
df1["Vol"]=cur

dt2 = pd.to_datetime("2019-05-30")

df1=df1[(df1['date'] < dt2)].reset_index()
# s_score(tweet,"dict", "sent_score")





# write_pickle(output_pickle_path, "tweets_sentscore.pkl", tweet)
# BitTweets['date'] = pd.to_datetime(BitTweets['date'])

# BitTweets["sw_dict"]=BitTweets["text_sw"].apply(dictionary_check)

# write_pickle(output_pickle_path, "tweets_sentscore.pkl", BitTweets)
# BitTweets = BitTweets.drop(columns=[ 'user_created', 'user_followers', 'user_friends','length'])




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


# BitTweets.to_csv(output_path+"/tweets_swd.csv")

df1.to_csv(output_path+"/tweets_score.csv")