import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# trick
df.isnull().sum() # number of missing value in each row
df.drop('colname', axis='columns', inplace=True)
df.dropna(subset=['col1', 'col2'], inplace=True)
df.col1.str.cat(df.col2, sep=' ') # combine two columns
df.col.dtype
pd.to_datetime













