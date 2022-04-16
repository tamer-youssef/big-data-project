# run this file second
import pandas as pd

# reading the original csv file
df = pd.read_csv('pfizer.csv')

# selecting the columns for the new dataset
df = df.loc[:, ['username','date','tweet','hashtags','link']]

# storing the new dataset to csv
df.to_csv('pfizernew.csv', index=True)