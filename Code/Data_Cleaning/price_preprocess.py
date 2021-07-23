#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt


the_path = "/Users/nan/Desktop/21Summer/raw_data/"
output_path = "/Users/nan/Desktop/21Summer/clean_data/"
           
price_df = pd.read_csv(the_path + "bitcoin_price.csv")
price_df.columns = [c.replace(' ', '_') for c in price_df.columns]
price_df.head()

price_df.Open_Time = pd.to_datetime(price_df.Open_Time, unit='ms')
price_df.Close_Time = pd.to_datetime(price_df.Close_Time, unit='ms')

price_df.head()

#No missing value
price_df.shape
price_df.info()

price_df.nunique().sort_values()


plt.figure(figsize=(12,6))
plt.plot(price_df['Close_Time'],price_df['Close'],color='b',linestyle='-')
plt.xlabel('Close Time')
plt.ylabel('Close Price')
plt.title('price')


price_df.to_csv(output_path + 'clean_price.csv')

