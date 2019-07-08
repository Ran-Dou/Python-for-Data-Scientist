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

# =============================================================================
# COMBINGING DATA
# =============================================================================

### concatenate data
# use ignore_index=True to reset index
# use axis=1 to indicate column wise concatenate
pd.concat([...,...], ignore_index=True, axis=1)
# concatenating many files
# Globbing: pattern matching for file names
# Wildcards: * match all strings, ? match single character
import glob
csv_files = glob.glob('*.csv')
print(csv_files)
list_data = []
for filename in csv_files:
    data = pd.read_csv(filename)
    list_data.append(data)
pd.concat(list_data)

### merging data
pd.merge(left=..., right=..., on=None, left_on='...', right_on='name')
df.head(20) #first 20 rows

# =============================================================================
# CLEANING DATA
# =============================================================================

### Convert datatype
print(df.dtypes)    #get the data type of each column
df['Zip'] = df['Zip'].astype(str)
# converting categorical data to 'category' dtype can make the dataframe smaller in memory
df.State = df.State.astype('category')
df.Zip = pd.to_numeric(df.Zip, errors='coerce')  # if there is missing value

### String Manipulation
# re library for Regular Expressions
# re library is used for string pattern matching
import re
# \d represent any digit
# \d* represent zero or more times
# $ represents the end of a string
# \$\d* represents any digits follow a dollar sign
# \$\d*\.\d{2} extention for 2 decimals digits
# . the period matches any 1 character
# ^...$ indicates the begining and the end of the value
# Often first compile the pattern
pattern = re.compile('\$\d*\.\d{2}')
result = pattern.match('$17.89')    #return a match object
bool(result)
# find multiple values
# + represents multiple times
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
print(matches)
# Other examples
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)
# [A-Z] represents any capital letters
# \w* represents any letter
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)

### Functions
# cleaning step requires multiple steps
df.apply(np.meam, axis=0, [additional function parameters])
import re
from numpy import Nan   # loading NaN missing value
# Example 1
def recode_gender(gender):
    if gender == 'Male':
        return 1
    elif gender == 'Female':
        return 0
    else:
        return np.nan
tips['recode'] = tips.sex.apply(recode_gender)
print(tips.head(5))
# Example 2
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])
print(tips.head())

### Dealing with duplicate or missing data
df = df.drop_duplicates()
print(df.info())
df_dropped = df.dropna()
df['Existing Height'] = df['Existing Height'].fillna('missing')
df['Proposed Height'] = df['Proposed Height'].fillna(0)
mean_value = df.Borough.mean()
print(mean_value)
df.Borough = df.Borough.fillna(meanvalue)

### Testing
# write assert statement to verify this
assert 1 == 1
assert 1 == 2   # Return error when False
assert df['Non-Profit'].notnull().all()
# chain two .all() methods (that is, .all().all()). The first .all() method will return a True or False for each column, while the second .all() method will return a single True or False.
ebola = pd.read_csv('ebola.csv')
assert ebola.notnull().all().all()
assert (ebola >= 0).all().all()

# =============================================================================
# EXERCISE
# =============================================================================












