import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# trick
df.isnull().sum() # number of missing value in each row
df.drop('colname', axis='columns', inplace=True)
df.dropna(subset=['col1', 'col2'], inplace=True)
df.col1.str.cat(df.col2, sep=' ') # combine two columns
df.col.dtype
pd.to_datetime

df.col.value_counts()  # counts unique values in a series
df.col.value_counts(normalize=True)  # counts proportion in a series

df.col.unique()
df.groupby(['col1', 'col2']).function()

# value_counts excludes missing value by default
value_counts(dropna=False)

df.col.str.contains('...', na=False)

# datateime format series
df.col.dt.month

pd.crosstab(col1, col2)
k_zones.plot(kind='bar', stacked=True)
df.col.sort_values().plot()
df.col.sort_values().plot(kind='barh')


mapping = {'up':True, 'down':False} #ref:new
df[col_new] = df.col_ref.map(mapping)
df.col.unique()
weather.TDIFF.plot(kind='hist', bins=20)

# Category
df.col.memory_usage(deep=True)
cats=[...,...,...]
df.col=df.col.astype('category', ordered=True, categories=cats)
df.col.memory_usage(deep=True)  # check the memory usage again

weather['bad_conditions'] = WT.sum(axis=1)
# Replace missing values in 'bad_conditions' with '0'
weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

# move index to column
df.reset_index(inplace=True)







