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
























