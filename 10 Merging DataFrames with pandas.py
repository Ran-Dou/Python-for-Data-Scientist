import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')
 
# =============================================================================
# PREPARING DATA
# =============================================================================

import pandas as pd
filenames = ['sales-jan-2015.csv', 'sales-feb-2015.csv']
dataframes = []
for f in filenames: 
    dataframes.append(pd.read_csv(f))
dataframes = [pd.read_csv(f) for f in filenames]

from glob import glob
filnames = glob('sales*.csv')   # use wildcard pattern to match target names

# Sort
# the principal methods for doing this are .sort_index() and .sort_values().
# reindex doesn't change the index-value pairs

# df.divide(df2, axis='rows)
# df.pct_change() * 100
# df.multiply()
# df.add(df, fill_value='...')  # can have multiple chains
# temps_c.columns.str.replace('F', 'C') 

# Example 1
gdp = pd.read_csv('gdp_usa.csv', index_col='DATE', parse_dates=True)
post2008 = gdp['2008':]
print(post2008.tail(8))
yearly = post2008.resample('A').last()
print(yearly)
yearly['growth'] = yearly.pct_change() * 100
print(yearly)

# Example 2
sp500 = pd.read_csv('sp500.csv', parse_dates=True, index_col='Date') 
exchange = pd.read_csv('exchange.csv', parse_dates=True, index_col='Date')
dollars = sp500[['Open','Close']]
print(dollars.head())
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')
print(pounds.head())

# =============================================================================
# APPENDING & CONCATENATING
# =============================================================================

# df.append(df2, ignore_index=True)
# df.concat([...], ignore_index=True)  #multiple   #both row and columns
# set axis=1 to concat, rows with same index join together

# Example 1
medal_types = ['bronze', 'silver', 'gold']
medals =[]
for medal in medal_types:
    file_name = "%s_top5.csv" % medal
    columns = ['Country', medal]
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)
    medals.append(medal_df)
medals_df = pd.concat(medals, axis='columns')
print(medals_df)

# df.concat([...], keys=[...], axis=0)
# df.concat([...], keys=[...], axis='columns')

import numpy as np
A = np.arange(8).reshape(2,4) + 0.1
B = np.arange(6).reshape(2,3) + 0.2
C = np.arange(12).reshape(3,4) + 0.3
np.hstack([B,A])
np.vstack([A,C])
np.concatenate([B,A], axis=1)
np.concatenate([A,C], axis=0) 

### Outer Join & Inner Join
pd.concat([...], axis=1, join='inner')
pd.concat([...], axis=1, join='outer')

# =============================================================================
# MERGING DATAFRAME
# =============================================================================

pd.merge(df1, df2)  #default by all columns
pd.merge(df1, df2, on='...')
pd.merge(df1, df2, left_on='...', right_on='...')
pd.merge(df1, df2, on=['...', '...'], suffixes=['...', '...'])
pd.merge(df1, df2, on=['...', '...'], suffixes=['...', '...'], how='left')
df1.join(df2, how='left')

# Occam's razor: use the simplest tool that works
pd.merge_orderd(df1, df2, fill_method='ffill')   # index ordered alphabeticly

# Similar to pd.merge_ordered(), the pd.merge_asof() function will also merge
# values in order using the on column, but for each row in the left DataFrame,
# only rows from the right DataFrame whose 'on' column values are less than the
# left value will be kept.
pd.merge_asof()


# =============================================================================
# CASE STUDY
# =============================================================================

# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()















