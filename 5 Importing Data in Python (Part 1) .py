# Plain text files: txt, csv
# Files from other softwares
# Relational Databases

# =============================================================================
# IMPORT PLAIN TEXT FILES
# =============================================================================

### Plain Text File
# Reading a text file
# Don't have a great example here, use a flat file.
filename = 'seaslug.txt'
file = open(filename, mode = 'r')   #'r' is to read
text = file.read()
file.close()    # remember to close the connection to the file
print(text) #print the file to the console
# Writing to a file
file = open(filename, mode = 'w')   #'w' is to write
file.close()    # remember to close the connection to the file
# Use 'with' statement to avoid forget close file
with open('seaslug.txt', 'r') as file:
    print(file.read())
# Check whether a file is closed
print(file.closed)
# read the first few lines of a file
with open('seaslug.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

### Appendix
# use '! ls' to check the contents of your current directory
!ls
# also import 'os' (operating system)
import os
wd = os.getcwd()
os.listdir(wd)

### Flat Files
# includes text files containing records
# a flat file can have header
# it's important to know whether your flat file has a header
# .csv: comma seperated values
# .txt: Text file (can be Tab-delimited file)
# if only has numerical data: can use NumPy, have both numericla and strings: pandas
import this  # PEP20

# Importing Flat Files using NumPy
import numpy as np
import matplotlib.pyplot as plt
filename = '...'
data = np.loadtxt(filename, delimiter = ',', skiprows = 1, usecols = [4,9], dtype = str)    # default delimiter is any white space
# use '\t' if is tab-deliminated
data
# Example
file = 'seaslug.txt'
data = np.loadtxt(file, delimiter='\t', dtype=str)
print(data[0])
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)
print(data_float[9])
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
# use 'np.genfromtxt' to deal with complex data
data = np.genfromtxt('titanic_sub.csv', delimiter=',', names=True, dtype=None)
# np.recfromcsv() behaves similarly to np.genfromtxt(), except that its default dtype is None
# it has the defaults delimiter=',' and names=True in addition to dtype=None
d = np.recfromcsv('titanic_sub.csv')
print(d[:3])

# Importing Flat Files using pandas
# df.read_csv() / df.read_table()
import pandas as pd
filename = 'titanic_sub.csv'
data = pd.read_csv(filename, nrows = 10, header = None)
data.head()     # check the first five rows
data_array = data.values    # convert into a numpy array
# Example
import matplotlib.pyplot as plt
file = 'titanic_sub.csv'
data = pd.read_csv(file, sep=',', comment='#', na_values='Nothing')
print(data.head())
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

# =============================================================================
# IMPORT OTHER FILE TYPES
# =============================================================================

### Excel Spreadsheets
import pandas as pd
file = 'urbanpop.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names) #identify the sheets
df1 = data.parse('1960-1966')   # sheet name, as a string
df2 = data.parse(0) # sheet index, as a float
# The values passed to skiprows, names, and usecols all need to be of type list.
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

### MATLAB files
# 'Matrix Laboratory': industry standard in the disciplines of engineering and science
# .mat
import scipy.io
# scipy.io.loadmat()  # read .mat files
# scipy.io.savemat()  # write .mat files
filename = 'ja_data2.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))

### SAS files
# 'Statistical Analysis System': business analytics and biostatistics
# .sas7bdat (dataset files) / .sas7bcat (catalog files)
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()
print(df_sas.head())
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

### Stata files
# 'Statistics + Data': academic social sciences research
# .dta
import pandas as pd
df = pd.read_stata('disarea.dta')
print(df.head())
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

### HDF5 files
# 'hierarchical Data Format version 5': storing largequantities of numerical data
# Large files can be hundreds of gigabytes or even terabytes in size
import h5py
filename = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(filename, 'r')     # 'r' is to read
print(type(data))
# Explore its hierarchical structure
for key in data.keys():
    print(key)  # each of the keys is a HDF group (like directory)
for key in data['meta'].keys():
    print(key)
print(data['meta']['Description'].value, data['meta']['Detector'].value)
# Example
file = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(file, 'r')
group = data['strain']
for key in group.keys():
    print(key)
strain = data['strain']['Strain'].value
num_samples = 10000
time = np.arange(0, 1, 1/num_samples)
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

### Pickled files
# Pickled files are serialized
# Serialize = convert object to btyestream
import pickle
with open('....pkl', 'rb') as file: #use 'rb' to specify read only and binary
    data = pickle.load(file)
# There are a number of datatypes that cannot be saved easily to flat files, such as lists and dictionaries.
# If you want your files to be human readable, you may want to save them as text files in a clever manner. JSONs.
# JSONs are appropriate for Python dictionaries.

# =============================================================================
# Relational Databases
# =============================================================================

# based on relational model of data
# Each row or record represents an instance of the entity type
# Each column represents an attribute of each instance
# Todd's 12 Rules/Commandments
# Many packages: sqlite3, SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')
table_names = engine.table_names()  # return a list of table names

### Workflow of SQL querying
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Chinook.sqlite')
con = engine.connect()
rs = con.execute('SELECT * FROM Album')
df = pd.DataFrame(rs.fetchall())    # fetches all rows
df.columns = rs.keys()
con.close()
print(df.head())

# Avoid to close the connection, same as file
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchmany(size=5))   # imports 5 rows instead of all rows
    df.columns = rs.keys()  
print(len(df))
print(df.head())

# DO IT IN ONE LINE!
engine = create_engine('sqlite:///Chinook.sqlite')
df = pd.read_sql_query('SELECT * FROM Album', engine)

# INNER JOIN in Python(pandas)
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Chinook.sqlite')
df = pd.read_sql_query('SELECT * FROM Album', engine)
print(df.head())
# Example
with engine.connect() as con:
    rs = con.execute('SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
print(df.head())
# Example
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000', engine)
print(df.head())



