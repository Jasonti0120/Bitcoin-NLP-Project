#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:51:20 2021

@author: jasonti
"""

from utils import *
import pandas as pd

#Replace both paths with the one on your machine 
tweet_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/tweets/"
price_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Original/price/"
output_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/DataSets/Preprocessed/"
output_pickle_path = "/Users/jasonti/Desktop/Bitcoin-NLP-Project-Local/Code/pickle/"

EM_tweet = open_pickle(output_pickle_path, "EM_tweet.pkl")
Doge = open_pickle(output_pickle_path, "doge.pkl")
BitPrice = open_pickle(output_pickle_path, "Bprice.pkl")
BitTweets = open_pickle(output_pickle_path, "BTweets.pkl")
BitTweets.rename(columns={'date':'Date'},
inplace=True)

EM_tweet_tf = create_tf_idf(EM_tweet['sw_dictionary'], 1, 1)
EM_tweet_tf["Date"] = EM_tweet["Date"]
EM_tweet_vc = create_vec(EM_tweet['sw_dictionary'], 1, 1)
EM_tweet_vc["Date"] = EM_tweet["Date"]



#merge original EM(clean text) with Doge price
merge_and_csv(EM_tweet, Doge, "Date", output_pickle_path, "M_EMDoge", output_path)

#merge tf_idf EM tweet with Doge price
merge_and_csv(EM_tweet_tf, Doge, "Date", output_pickle_path, "M_EMDoge_tf", output_path)

#merge vector count EM tweet with Doge price
merge_and_csv(EM_tweet_vc, Doge, "Date", output_pickle_path, "M_EMDoge_vc", output_path)

#merge original EM(clean text) with Bitcoin price
merge_and_csv(EM_tweet, BitPrice, "Date", output_pickle_path, "M_EMBit", output_path)

#merge tf_idf EM tweets with Bitcoin Price
merge_and_csv(EM_tweet_tf, BitPrice, "Date", output_pickle_path, "M_EMBit_tf", output_path)

#merge vc EM tweets with Bitcoin Price
merge_and_csv(EM_tweet_vc, BitPrice, "Date", output_pickle_path, "M_EMBit_vc", output_path)

#merge original Btweets with B Price
merge_and_csv(BitTweets, BitPrice, "Date", output_pickle_path, "M_BtweetsPrice", output_path)

#merge bit coin price and dogecoin price
merge_and_csv(BitPrice, Doge, "Date", output_pickle_path, "M_BtweetsPrice_Doge", output_path)


# BitTweets_tf = create_tf_idf(BitTweets['sw_dictionary'], 1, 1)
# BitTweets_tf.insert(0, "Date", BitTweets["Date"])
# BitTweets_vc = create_vec(BitTweets['sw_dictionary'], 1, 1)
# BitTweets_vc["Date"] = BitTweets["Date"]

#merge tf_idf Btweets with B Price
# merge(BitTweets_tf, BitPrice, "Date", output_pickle_path, "M_BtweetsPrice_tf.pkl")

# #merge vc Btweets with B Price
# m2 = pd.merge(left=BitTweets_vc, right=BitPrice, on="Date")

