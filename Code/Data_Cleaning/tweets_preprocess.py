#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import datetime
from datetime import datetime
from datetime import timedelta


# In[30]:


the_path = "/Users/nan/Desktop/21Summer/raw_data/"
output_path = "/Users/nan/Desktop/21Summer/clean_data/"
           
tw_df = pd.read_csv(the_path + "bitcoin_tweets.csv", na_values="?")
tw_df.columns = [c.replace(' ', '_') for c in tw_df.columns]

tw_df.head()


# In[31]:


tw_df.shape


# In[32]:


tw_df.info()


# In[35]:


tw_df.nunique().sort_values()


# In[ ]:


#Drop the columns with many missing values
tw_df.drop(columns='user_location', inplace=True)
tw_df.drop(columns='user_description', inplace=True)

#Drop the column with only one unique value
tw_df.drop(columns='is_retweet', inplace=True)

#Drop the irrelavant columns
tw_df.drop(columns='user_name', inplace=True)


# In[39]:


#没确定怎么处理这个feature（drop column？转为array去掉内容错误的行？）
#7个unique values中，2个重复（str & Bool),3个irrelevant content
tw_df['user_verified'].unique()


# In[13]:


#时间转换有问题，没确定保留什么格式
tw_df['date'] = tw_df['date'].dt.date


# In[ ]:


price_df.to_csv(output_path + 'clean_tweets.csv')

