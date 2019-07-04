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

















