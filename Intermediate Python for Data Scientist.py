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
world.keys()  #Print out the keys in europe
world.values()  #Print out value that belongs to key 'norway'
'algeria' in world  #check whether a key is in a dictionary
#keys have to be 'immutable' objects: strings, booleans, integers, but not list
#keys are also identical and unique in a dictionary.

#Add more keys to a dictionary
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
world['algeria'] = 40.00  #change the value of a key, or add a new key
print(world)
del(world['afghanistan'])  #delete a key in the dictionary
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
os.chdir("/Users/randou/Esther/Brandeis/2018 Fall/Data Scientist with Python/2 Intermediate Python for Data Scientist")
brics = pd.read_csv("brics.csv", index_col = 0)

### Manipulation of DataFrame
brics = pd.read_csv("brics.csv", index_col = 0)
#Wrong way to do this
type(brics["country"])  #a pandas series
#Right way (limited)
brics[['country','capital']]  #use double square brackets
brics[1:4]  #get the rows only through slicing (index starts at 0)
#Much better way: loc(label-based)/iloc(position-based)
brics.loc[['RU','IN','CH'],['country','capital']]
brics.loc[:,['country','capital']]  #all rows
brics.iloc[[1,2,3],[0,1]]
brics.iloc[:,[0,1]]

















