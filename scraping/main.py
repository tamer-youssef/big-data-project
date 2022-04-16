# run this file first
import twint
import pandas as pd

c = twint.Config()
c.Pandas = True

#creating search queries
c.Search = "pfizer vaccine"
c.Limit = 2000

# searching for data that meets the query
twint.run.Search(c)

# converting the dataset and storing to csv 
df = twint.storage.panda.Tweets_df
df.to_csv('pfizer.csv', index=False) 
