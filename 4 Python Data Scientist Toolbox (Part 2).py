import os
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist')

# =============================================================================
# ITERATORS
# =============================================================================

# string, list, a range of objects, dictionaries, file connections
# an object with an associated iter() method
# applying iter() to an iterable creates an iterator 

### Iterator
# an iterable is an object that can return an iterator
# an iterator is an object that keeps state and produces the next value when you call next() on it.
# produces next value with next()
word = 'Da'
it = iter(word)
print(next(it))
print(next(it))
print(next(it)) #StopIteration: the program stop until ther is no more value to return
# Iterating at once with *
it = iter(word)
print(*it)  #only use after iter() is defined, and use in print()

### Useful Function for Iterators

# enumerate()
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)     # value with index
print(type(e))
e_list = list(e)
print(e_list)
for index, value in enumerate(avengers, start = 10):    # assign a start index
    print(index, value)

# zip()
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']
z = zip(avengers, names)    # create a list of tuple
print(type(z))
z_list = list(z)
print(z_list)
# unpack the zip
for z1, z2 in zip(avengers, names) :
    print(z1, z2)
z = zip(avengers, names)    # create a list of tuple
print(*z)
zip(*z) # also a list of tuple

# Iterating over data
# Using iterators to load large files into memory
import pandas as pd
result = []
for chunk in pd.read_csv('tweets.csv', chunksize = 1000) :    # specify the chunk: chunksize
    result.append(sum(chunk['x']))
total = sum(result)
print(total) # give us the total sum of column of interest

total = 0
for chunk in pd.read_csv('tweets.csv', chunksize = 1000) :    # specify the chunk: chunksize
    total += sum(chunk['x'])
print(total)

# Practices
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of occurrences as value for each key."""
    counts_dict = {}
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict
result_counts = count_entries('tweets.csv', 10, 'lang')
print(result_counts)

# =============================================================================
# LIST COMPREHENSION
# =============================================================================

### Single Loop
# Previous Approach
nums = [12, 8, 21, 3, 16]
new_nums = []
for num in nums:
    new_nums.append(num + 1)
print(new_nums)
# New Approach
nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)
# List comprehensions collapse for loops for building lists into a single line
# Need: one iterable, iterator variable

### Nested Loops
# Previous Approach
pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))
print(pairs_1)
# New Approach
#[[output expression] for iterator variable in iterable]
pairs_1 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(0, 5)]
for row in matrix:
    print(row)

### Conditionals in comprehensions
# Conditionals on the iterable
[num ** 2 for num in range(10) if num % 2 == 0]     # add if to the end
# Conditionals on the output expression
[num ** 2 if num % 2 == 0 else 0 for num in range(10)]  # add if to the middle
# Dictionary Comprehensions
# Us e curly braces {} instead of brackets []
pos_neg = {num: -num for num in range(9)}

# =============================================================================
# GENERATOR EXPRESSIONS
# =============================================================================

# Compare to Comprehension: use () instead of []
# It doesn't store the value
# Return a generator object that we can iterate over
result = (num for num in range(6))
print(next(result)); print(next(result))    # Lazy Evaluation
# Extremely useful when dealing with big data

### Generator functions
# Produces generator objects when called, and defined use 'def'
# 'Yield' a sequence of values instead of returning a single value
def num_sequence(n):
    """Generate values from 0 to n."""
    i = 0
    while i < n:
        yield i        # use 'yield' instead of 'return'
        i += 1
# Can be called as you do any other functions

### Practices
        
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""
    for person in input_list:
        yield len(person)
for value in get_lengths(lannister):
    print(value)

# binds the csv file 'datacamp.csv' as datacamp in the context manager.
# the with statement is the context manager
# its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.
# Open a connection to the file

### Example 1
with open('world_ind_pop_data.csv') as file:
    # Skip the column names
    file.readline()
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}
    # Process only the first 1000 rows
    for j in range(1000):
        # Split the current line into a list: line
        line = file.readline().split(',')
        # Get the value for the first column: first_col
        first_col = line[0]
        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1
# Print the resulting dictionary
print(counts_dict)

### Example 2
# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""
    # Loop indefinitely until the end of the file
    while True:
        # Read a line from the file: data
        data = file_object.readline()
        # Break if this is the end of the file
        if not data:
            break
        # Yield the line of data
        yield data      
# Open a connection to the file
with open('world_ind_pop_data.csv') as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)
    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

### Example 3
# Initialize an empty dictionary: counts_dict
counts_dict = {}
# Open a connection to the file
with open('world_ind_pop_data.csv') as file:
    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):
        row = line.split(',')
        first_col = row[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
# Print            
print(counts_dict)

### Example 4
# Import the pandas package
import pandas as pd
# Initialize reader object: df_reader
df_reader = pd.read_csv('world_ind_pop_data.csv', chunksize = 10)
# Print two chunks
print(next(df_reader))
print(next(df_reader))

### Example 5
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=1000)
# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)
# Check out the head of the DataFrame
print(df_urb_pop.head())
# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode']=='CEB']
# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
# Turn zip object into list: pops_list
pops_list = list(pops)
print(pops_list)

### Example 6
# Code from previous exercise
import matplotlib.pyplot as plt
urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)
# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(x * y * 0.01) for x, y in pops_list]
# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

### Example 7
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=1000)
# Initialize empty DataFrame: data
data = pd.DataFrame()
# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:
    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])
    # Turn zip object into list: pops_list
    pops_list = list(pops)
    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb) 
# Plot urban population data 
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

### Example 8
# Define plot_pop()
def plot_pop(filename, country_code):
    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)
    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]
        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])
        # Turn zip object into list: pops_list
        pops_list = list(pops)
        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)
    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()
# Set the filename: fn
fn = 'world_ind_pop_data.csv'
# Call plot_pop for country code 'CEB'
plot_pop('world_ind_pop_data.csv', 'CEB')
# Call plot_pop for country code 'ARB'
plot_pop('world_ind_pop_data.csv', 'ARB')
