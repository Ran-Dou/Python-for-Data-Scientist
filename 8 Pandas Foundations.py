import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
# Data ingestion & inspection
# =============================================================================

import pandas as pd
import numpy as np
df = pd.read_csv('world_ind_pop_data.csv')
# NaN: Not-a-Number
df.iloc[::3, -1] = np.nan  # '::3' means every third row
# a column in a dataframe is a pandas serie
# the value in the column is a numpy ndarray
df = pd.read_csv('world_ind_pop_data.csv')
# assign numerical values in df to an array
np_vals = df.values

### Build DataFrames from dictionary
data = {'weekday': ['Sun', 'Sun', 'Mon', 'Mon'],
        'city': ['Austin', 'Dallas', 'Austin', 'Dallas'],
        'visitors': [139, 237, 326, 456],
        'signups': [7, 12, 3, 5]}
users = pd.DataFrame(data)

### Build DataFrames from lists
cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekdays]   # a list of lists
zipped = list(zip(list_labels, list_cols))
data = dict(zipped)
user = pd.DataFrame(data)
print(user)

### Broadcasting
user['fees'] = 0    # broadcasts to entire column
# broadcasting with a dict
heights = [ 59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1 ]
data = {'height': heights, 'sex': 'M'}
results = pd.DataFrame(data)
print(results)

filepath = 'world_ind_pop_data.csv'
df = pd.read_csv(filepath, header=None, #indicates the file doesn't have column name
                 names=...,      # also can define new names using a created list
                 na_values={'column':['-1']},   # turning all '-1' into NA value 
                 parse_dates = [[0, 1, 2]])     # infers dates intelligently, tell which columns include dates and combine them
df.index.name = 'number' # assign a name to an index

### Excersice
file_messy = 'messy_stock_data.tsv'
df1 = pd.read_csv(file_messy)
print(df1.head(5))
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')
print(df2.head())
df2.to_csv(file_clean, index=False)
df2.to_excel('file_clean.xlsx', index=False)

### Plotting
import matplotlib.pyplot as plt
# plot all columns
df.plot()
# Plot all columns as subplots
df.plot(subplots=True)

plt.savefig('....png')
plt.savefig('....jpg')
plt.savefig('....pdf')

# =============================================================================
# EDA: EXPLORATORY DATA ANALYSIS
# =============================================================================

# Histogram options: bins(integer), range(tuple), normed(boolean), cumulative(boolean)
# CDF: Cumulative Distribution Function
# df.plot(kind='hist') / df.plt.hist() / df.hist()
# ax=axes[0] means that this plot will appear in the first row.

# Two plots
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)
# Plot the PDF
df.fraction.plot(ax=axes[0], kind='hist', normed=True, bins = 30, range=(0,.3))
plt.show()
# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', normed=True, bins = 30, cumulative=True, range=(0,.3))
plt.show()

# statistical method: ignore NaN entries
# .count()
# .mean()
# .std()
# .median()
# .quantile(q)  #q can be a value or an array between 0-1
# IQR: Inter-quartile range
# .min()/.max()
# can specify axis='columns'
# .unique() for categorical data
# del ..., ...      # easy way to delete column
# data.drop("Area", axis=1, inplace=True).
# Note that the original 'data' object is changed when inplace=True
# np.abs()      # compute the absolute value.

# =============================================================================
# TIME SERIES
# =============================================================================

# parse_dates = True
# index_col = 'Date'
# Partial selections
# df.loc['February 5, 2015'] / df.loc['2015-Feb-5'] / df.loc['2015-2-5']
# whole month or year: df.loc['2015-2'] / df.loc['2015']
# partial daytime: df.loc['2015-2-16':'2015-2-20']

# df = pd.read_csv(filename, index_col='Date', parse_dates=True)
# pd.to_datetime
# df.reindex(..., method = 'ffil'/'bfil')   # default is NaN (forward, backward)

### Resampling
# Downsampling: Daily to Weekly
# Upsampling: Daily to Hourly
# df.resample('D', 'W', '2W')      # 'D' stands for daily
# common arguments: 'min'/'T'/'H'/'D'/'B'/'W'/'M'/'Q'/'A'
# Upsampling: df.resample('4H').ffill()
# df.resample('A').first().interpolate('linear')

### Rolling
# To use the .rolling() method, you must always use method chaining, first calling .rolling() and then chaining an aggregation method after it.
# smoothed = unsmoothed.rolling(window=24).mean()   # 24hr window

# df.column.str.upper()
# df.column.str.contains()
# df.column.dt.hour
# df.column.dt.tz_localize('US/Central').dt.tz_convert('US/Eastern')    # convert timezone

# df.columns = df.columns.str.strip()   # strip extra whitespace
# df.plot(style = 'k.-')        # color(k:black), marker(.:dot)
# other color styles: b(blue) / g(green) / r(red) / c(cyan)
# other marker styles: o(circle) / *(star) / s(square) / +(plus)
# other line styles: :(dotted), -(dashed)













