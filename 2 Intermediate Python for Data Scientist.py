# =============================================================================
# Matplotlib
# =============================================================================

###Basic plots with matplotlib
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]  #unit: billion
plt.plot(year, pop)  #plt.plot(x, y)
# ? plt.show()  #python wait for the 'show' function to display the plot
plt.scatter(year, pop)  #Scatter plot
plt.xscale('log')  #Put the x-axis on a logarithmic scale

###Histogram
#get idea about distribution
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins = 3)
plt.show()  #displays a plot
plt.clf()  #cleans it up again so you can start a fresh.

###Plot Customization
#Cutomizaiton depends on 1)data, 2)story you want to tell
import numpy as np
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]  #unit: billion
col = ['green','yellow','red','blue']
plt.scatter(year, pop, s = np.array(pop)**2, c = col, alpha = 0.8)  #plt.plot(x, y) #change size base on 'pop'
plt.xlabel('Year')  #add label to x axis
plt.ylabel('Population')  #add label to y axis
plt.title('World Population Projections')  #add title to the plot
plt.yticks([0, 2, 4, 6, 8, 10],['0', '2B', '4B', '6B', '8B', '10B'])  #change y ticks
plt.text(1950, 3, 'text1')
plt.grid(True)

# =============================================================================
# DICTIONARIES
# =============================================================================

#Old way of retriving a value
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]
ind_alb = countries.index("albania")
print(ind_alb)
pop[ind_alb]
#New way of retriving a value
### Dictonary{key:value}
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
world["albania"]  #dict_name[key] returns the corresponding value
print(world.keys())  #Print out the keys in europe
print(world.values())  #Print out value that belongs to key 'norway'
print('algeria' in world)  #check whether a key is in a dictionary
#keys have to be 'immutable' objects: strings, booleans, integers, but not list
#keys are also identical and unique in a dictionary.

#Add more keys to a dictionary
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
world['algeria'] = 40.00  #change the value of a key, or add a new key
print(world)
del(world['afghanistan'])  #delete a key in the dictionary
print(world)
world['afghanistan'] = 30.55
print(world)

#List vs. Dictionary
#List: Collection of values; Indexed by range of numbers; Select entire subsets
#Dictionary: Lookip table with unique keys
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
europe['france']['capital']  # Print out the capital of France
data = {'capital':'rome', 'population': 59.83 }  # Create sub-dictionary data
europe['italy'] = data  # Add data to europe under key 'italy'
print(europe)  # Print europe

# =============================================================================
# PANDAS
# =============================================================================

#Numpy.array is way to store data in the same datatype
#Pandas is a high level data manipulation tool developed by Wes Mckinney
#Built on Numpy package.
import pandas as pd

#Create a dataframe
# 1) DataFrame from Dictionary(keys are the variables))
dict = {"country":["Brazil", "Russia", "India", "China", "South Africa"],
        "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
        "area":[8.516, 17.10, 3.286, 9.597, 1.221],
        "population":[200.4, 143.5, 1252, 1357, 52.98]}
brics = pd.DataFrame(dict)
print(brics)
brics.index = ["BR", "RU", "IN", "CH", "SA"]  #change the index of df
# 2) DataFrame from CSV file (comma-separated values)
# get current work directory
import os
os.getcwd()
os.chdir('/Users/randou/Esther/Coding/Python/Data Scientist with Python/Python-for-Data-Scientist') #change working directory
brics = pd.read_csv("brics.csv")

### Manipulation of DataFrame
brics = pd.read_csv("brics.csv", index_col = 0) #set index column
#Wrong way to do this
type(brics["country"])  #a pandas series
#Right way (limited)
brics[['country','capital']]  #use double square brackets
brics[1:4]  #get the rows only through slicing (index starts at 0)
#Much better way: loc(label-based)/iloc(position-based)
brics.loc[['RU','IN','CH'],['country','capital']] #can have only the row index, but can't only have the column index!
brics.loc[:,['country','capital']]  #all rows
brics.iloc[[1,2,3],[0,1]]
brics.iloc[:,[0,1]]

### Filtering Pandas DataFrame
### Need Pandas Series not DataFrame!!!
brics["area"]
print(brics["area"] > 8)
is_huge = brics["area"] > 8
print(brics[is_huge])
print(brics[brics["area"] > 8]) #those two methods are exactly the same
#multiple filtering
print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)])


# =============================================================================
# COMPARISON & BOOLEAN OPERATORS
# =============================================================================

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
print(bmi)
print(bmi > 23)
print(bmi[bmi > 23])

#simple comparison
print(2 < 3); print(2 == 3); print(2 <= 3)
print(2 > 3); print(2 >= 3); print(2 != 3)
x = 2; y = 3; print(x < y)
print('carl' < 'chris') #only compare the objects of the same type

# Boolean Operators: and, or, not
print(True and True)
x = 7
print(x > 5 and x < 15)
print(x < 5 and x < 15)

# Two-condition comparison for np.array
print(np.logical_and(bmi > 21, bmi < 22))
print(np.logical_or(bmi > 21, bmi < 22))
print(np.logical_not(bmi > 21, bmi < 22))

# =============================================================================
# IF, ELIF, ELSE
# =============================================================================

z = 4
if z % 2 == 0:          # if condition:
    print('z is even')      # expression
                        # expression
                        
z = 5
if z % 2 == 0:          # if condition:
    print('z is even')      # expression
else:                   # else:
    print('z is odd')       # expression

z = 3
if z % 2 == 0:                                      # if condition:
    print('z is divisible by 2')                        # expression
elif z % 3 == 0:                                    # elif condition:
    print('z is divisible by 3')                        # expression
else:                                                # else:
    print('z is neither divisible by 2 nor by 3')       # expression
                        
# =============================================================================
# LOOPS
# =============================================================================

### While Loop
# while loop = repeated if statement
error = 50.0
while error > 1 :       # while condition:
    error = error / 4       # expression
    print(error)            # expression

### For Loop
# for each 'var' in 'seq', execute expression
fam = [1.73, 1.68, 1.71, 1.89]
for height in fam :      # for var in seq:
    print(height)           # expression
# Get access to index
for index, height in enumerate(fam):
    print("index" + str(index) + ": " + str(height))
# print out each letter in a string
for c in 'family':
    print(c.capitalize())

### Looping Data Structures
# Dictionary
world = {'afghansitan': 30.55,
         'albania': 2.77,
         'algeria': 39.21}
for key, value in world.items():    #use dic.items() to get reference
    print(key + '--' + str(value))
# Numpy Arrays
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.3, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in meas:
    print(val)
for val in np.nditer(meas):         # use np.nditer() to get every elements
    print(val)
# Data Frame
for val in brics:
    print(val)
for lab, row in brics.iterrows():   # use df.iterrows() to get index and value
    print(lab + ': ' + row['capital'])
for lab, row in brics.iterrows():
    brics.loc[lab, 'name_length'] = len(row['country'])
# Efficient method to creat a new column
brics["name_length"] = brics["country"].apply(len)      #apply(str.upper)

# =============================================================================
# CASE STUDY: HACKER STATISTICS
# =============================================================================

### Random Generators
import numpy as np
np.random.rand()    # get a number between 0 and 1
# Pseudo-random numbers, Mathematical formula, Starting from a seed
np.random.seed(123) # for the same seed: same random numbers
coin = np.random.randint(0,2)   # 2 will not be included
print(coin)
if coin == 0:
    print('heads')
else:
    print('tails')

### Random Walk
# Path of molecules
# Initialize random_walk

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))  # np.transpose reverse x/y/z three dimensions
# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]
# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
# Probability
np.mean(ends >= 60)


















