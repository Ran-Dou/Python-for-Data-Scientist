import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
<<<<<<< HEAD
# EXTRACTING AND TRANSFORMING DATA
# =============================================================================

import pandas as pd
df = pd.read_csv('sales.csv', index_col='month')
print(df)
# indexing
print(df['salt']['Jan'])
print(df.eggs['Mar'])
print(df.loc['May', 'spam'])
print(df.iloc[4, 2])
print(df_new = df[['salt', 'eggs']])
# Series or Dataframe
print(type(df['eggs']))    #Series
print(type(df[['eggs']]))  #DataFrame
# Selection in reverse order
print(df['Mar':'Jan':-1])
# filtering
print(df[df.salt > 60])
# logical combine: & | 
print(df[(df.salt >= 60) & (df.eggs < 200)])
# DataFrames with zeros and NaNs
df2 = df.copy()
df2['bacon'] = [0, 0, 50, 60, 70, 80]
df2.loc[:, df2.all()]   # exclude column with zero entries
df2.loc[:, df2.any()]   # exclude column with all zero entries
df.loc[:, df.isnull().any()]  # return column with NaN
df.loc[:, df.notnull().all()]
df.dropna(how='all')
df.dropna(how='any')
# Example
titanic = pd.read_csv('titanic.csv')
# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())
# Transforming DataFrame
df.floordiv(12)     # convert to dozens unit
import numpy as np
np.floor_divide(df, 12)
def dozens(n):
    return n//12
df.apply(dozens) 
df.apply(lambda n: n//12)
# String Transformation
df.index = df.index.str.upper()
print(df)
# for index, there is no apply method, instead its df.index.map
df.index = df.index.map(str.lower)
print(df)
# create new column
df['salty_eggs'] = df.salt + df.eggs

### Example
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue', 'Romney':'red'}
# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election['winner'].map(red_vs_blue)
print(election.head())

# When performance is paramount, you should avoid using .apply() and .map()
# because those constructs perform Python for-loops over the data stored in a pandas Series or DataFrame.
# By using vectorized functions instead, you can loop over the data at the same speed as compiled code (C, Fortran, etc.)!
# NumPy, SciPy and pandas come with a variety of vectorized functions (called Universal Functions or UFuncs in NumPy).
from scipy.stats import zscore 
eggs_zscore = zscore(df['eggs])

# =============================================================================
# ADVANCED INDEXING
# =============================================================================

# Index can only be modified by all at once

### Hierarchical indexing
titanic = titanic.set_index(['name', 'sex'])
print(titanic.head())
print(titanic.index)    # Multiindex
print(titanic.index.name)
print(titanic.index.names)
titanic = titanic.sort_index()
print(titanic.head())

# The tuple used for the index does not recognize slicing with columns natively
titanic.loc[(slice(None), slice('female')), :]

# =============================================================================
# REARANGING AND RESHAPING
# =============================================================================

### Pivoting
df.pivot(index='...', columns='...', values='...')
df.pivot_table(index='...', columns='...', values='...', aggfunc='...', margins=True)
# if not setting values, all remaining will be used

### Stacking & unstacking
# unstack # pivot multiindex dataframe by gender
titanic_unstack = titanic.unstack(level='sex')
titanic_unstack = titanic.unstack(level=1)
titanic_stack = titanic_unstack.stack(level='name')
swapped = titanic.swaplevel.sort_index(0, 1)   #switch levels

### melting
pd.melt(df, id_vars=[...], value_vars=[...], var_name=..., value_name=...)
=======
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

# =============================================================================
# CASE STUDY
# =============================================================================



>>>>>>> master








