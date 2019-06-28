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





