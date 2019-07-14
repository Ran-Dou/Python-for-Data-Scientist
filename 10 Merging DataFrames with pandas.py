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



















