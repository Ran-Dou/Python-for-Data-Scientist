import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# Inconsistent column names
# Missing data
# Outliers
# Duplicate rows
# Untidy
# Need to process columns
# Column types can signal unexpected data values
# EDA: Exploratory data analysis

# =============================================================================
# EXPLORING DATA
# =============================================================================

import pandas as pd
df = pd.read_csv('dob_job_application_filings_subset.csv')
df.head()
df.tail()
df.columns
df.shape
df.info()
df.index

df.State.value_counts(dropna=False)
df['Site Fill'].value_counts(dropna=False)
df.describe()   #only for numerical type

import matplotlib.pyplot as plt
df.State.value_counts().plot('bar')
plt.show()
df.State.value_counts()[df.State.value_counts() < 500].plot('bar')
df.boxplot(column='Block', by='State')
df.Block.plot('hist', rot=70, logy=True)    # rot is for rotating axis lables
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)

# =============================================================================
# TIDYING DATA
# =============================================================================

# Columns represent separate variables
# Rows represent individual observations

### melting
pd.melt(frame=df, id_vars='', value_vars=['', ''],
                              var_name='', value_name='')
# Example
airquality = pd.read_csv('airquality.csv')
# Print the head of airquality
print(airquality.head())
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')
print(airquality_melt.head())

### pivot (opposite of melting)
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')
print(airquality_pivot.head())
# After pivoting airquality_melt in the previous exercise, you didn't quite get back the original DataFrame.
# What you got back instead was a pandas DataFrame with a hierarchical index (also known as a MultiIndex).
# need to reset the index
print(airquality_pivot.index)
airquality_pivot_reset = airquality_pivot.reset_index()
print(airquality_pivot_reset.index)
print(airquality_pivot_reset.head())
# can also add 'aggfunc = np.mean'

### melting and parsing
tb = pd.read_csv('tb.csv')
tb_melt = pd.melt(tb, id_vars=['country', 'year'])
tb_melt['sex'] = tb_melt.variable.str[0]    # treat the column as a string
tb_melt['agegroup'] = tb_melt.variable.str[1:]    # treat the column as a string
# split and get
ebola = pd.read_csv('ebola.csv')
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')
ebola_melt['str_split'] = ebola_melt['type_country'].str.split('_')
ebola_melt['type'] = ebola_melt['str_split'].str.get(0)
ebola_melt['country'] = ebola_melt['str_split'].str.get(1)
print(ebola_melt.head())











