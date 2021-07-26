#!/usr/bin/env python
# coding: utf-8


#Loading data
import pandas as pd
from func import *
import re


the_path = "/Users/nan/Desktop/21Summer/raw_data/"
output_path = "/Users/nan/Desktop/21Summer/clean_data/"
           
tw_df = pd.read_csv(the_path + "bitcoin_tweets.csv", na_values="?")
tw_df.columns = [c.replace(' ', '_') for c in tw_df.columns]

#Learn Basic Info
print("Shape is" , tw_df.shape)
tw_df.info()
print(tw_df.nunique().sort_values())

#Drop the columns with too many missing values
tw_df.drop(columns='user_location', inplace=True)
tw_df.drop(columns='user_description', inplace=True)

#Drop the column with only one unique value
tw_df.drop(columns='is_retweet', inplace=True)

#Drop the irrelavant columns
tw_df.drop(columns='user_name', inplace=True)

#Drop the column with wrong content
tw_df.drop(columns='user_verified', inplace=True)

# Clean & remove stopwords
tw_df['text'] = tw_df['text'].apply(str)
tw_df['text'] = tw_df['text'].apply(clean_text)
tw_df['text_sw'] = tw_df['text'].apply(rem_sw)

#Drop the rows without value at date column
tw_df['date'] = tw_df['date'].apply(str)
length = [len(re.split('-|:| ',d)) for d in tw_df['date']]
tw_df['length'] = length
tw_df = tw_df[tw_df['length']==6]

#Add a column of splitted dates
# which will be used later 
splitted = [re.split('-|:| ',d) for d in tw_df['date']]
tw_df['splitted_date'] = splitted
   

    
### TF-IDF & Vec
#tfidf = create_tf_idf(tw_df, output_path, 1, 2)
#vec = create_vec(tw_df, output_path, 1, 2)

### Export to csv
#tw_df.to_csv(output_path + 'clean_tweets.csv')


