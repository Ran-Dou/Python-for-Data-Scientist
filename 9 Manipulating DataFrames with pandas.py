import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
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

# =============================================================================
# GROUPBY
# =============================================================================

# Aggregation/Reduction
# mean/std/sum/first/last/min/max/median
df.groupby('eggs').count()
df.groupby('eggs').median()
df.groupby(['eggs','salt']).agg(['max','min'])    # multi-level
df.groupby(level=['eggs','salt']).agg(['max','min'])    # multi-level
# function can also be customized 
# can also use a dictionary in agg
# can also groupby other pandas series with same index value to groupby

### Categorical value
df.column.unique()
df.column = df.column.astype('category')
# Advanteges: less memory/ speed up operations like groupby()

### Example
titanic = pd.read_csv('titanic.csv')
by_class = titanic.groupby('pclass')
count_by_class = by_class.survived.count()
print(count_by_class)
by_mult = titanic.groupby(['embarked', 'pclass'])
count_mult = by_mult.survived.count()
print(count_mult)
# use .strftime('%a') to transform the index datetime values to abbreviated days of the week.
df.index.strfrime('...')

### Transforming
def zscore(series):
    return (series - series.mean()) / series.std()
df.groupby('...')[column].transform(function)
# the agg function applies reduction
# the transform function applies a function elementwise to groups
# apply is used for complicated situation

# Example
from scipy.stats import zscore
def zscore(series):
    return (series - series.mean()) / series.std()
gapminder = pd.read_csv('gapminder_tidy.csv')
standardized = gapminder.groupby('region')['life','fertility'].transform(zscore)
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)
gm_outliers = gapminder.loc[outliers]
print(gm_outliers)

# df.groupby().groups is a dict
under10 = (titanic['age']<10).map({True:'under 10', False:'over 10'})
# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)
# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10, 'pclass'])['survived'].mean()
print(survived_mean_2)




