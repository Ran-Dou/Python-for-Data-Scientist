# =============================================================================
# PYTHONG BASICS
# =============================================================================

#Python was conceived by Guido Van Rossum
#Python Scrip (.py): List of Python commands.

#Addition, Subtraction, Multiplication, Division, Exponentiation, Modulo
print(1+2)
print(1-2) 
print(1*2)
print(1/2)
print(4**2) 
print(8%7)

### Give object case specific sensitive name
height = 1.79
weight = 68.7
bmi = weight / height **2 
print(bmi)

###Python Types
type(bmi)  #float
day_of_week = 5
type(day_of_week)  #integers
x = "body mass index"  #single or double quotes are ok.
type(x)  #string
z = True
type(z)  #boolean
print(2+3)  #sum of two integer
print("ab" + "cd")  #sum of two string
#str(), int(), float() and bool() will help you convert Python values into any type.
savings = 100
result = 100 * 1.10 ** 7
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")
pi_string = "3.1415926"
pi_float = float(pi_string)
print(True + False)

# =============================================================================
# PYTHON LISTS
# =============================================================================

#When dealing with many data points, assign values to many objects seems inconvenient.
#[a, b, c]
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]  #give single name to a collection of values
print(fam)  #list can contains any type, and different types
fam2 = [["liz", 1.73],
        ["emma", 1.68],
        ["mom", 1.71],
        ["dad", 1.89]]
print(fam2)
print(type(fam2))

### Subsetting lists
print(fam[3])  #index: 0-(n-1)
print(fam[-1])  #inxex: (-n)-(-1)
print(fam[3:5])  #[start(inclusive):end(exclusive)]
print(fam[5:])  #index to the end
print(fam2[0][1])  #double index

### List Manipulaiton
fam[7] = 1.86  #cahnging list elements
print(fam)
fam[0:2] = ["lisa", 1.74]
print(fam)
fam_ext = fam + ["me", 1.79]  #add elements to the list
print(fam_ext)
del(fam[2])  #delete the third element in the list 'fam'
print(fam)

### Behind the scenes
#a list stores the position of the list, not the value of it
x = ["a", "b", "c"]
y = x
y[1] = "z"  #When updating an element in the list, it changes all the objects bounded to the list.
print(x)
#if want to store y seperately
x = ["a", "b", "c"]
y = list(x)
y = x[:]

#The ; sign is used to place commands on the same line.

# =============================================================================
# FUNCTIONS and PACKAGES
# =============================================================================

###Functions
#Function is a piece of reusable code for solving particular task
#Call funciton instead of writing code yourself
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)
tallest = max(fam)
print(tallest)
print(round(1.68, 1))  #one decimal
print(round(1.68))  #without the second input, automatically round to the closest integer
help(round)  #open up documentation
#find functions before creat one, casue there probably function exists!!!

### Built-in Functions
#output = function_name(input)
#The general recipe for calling functions and saving the result to an object
print()
type()
str(); int(); bool(); float()
len()
help()  #can also use ?functionname
#in python documentation, the square bracket [] means the argument is optional
sorted(__, key = __, reverse = __)

### Methods
#Methods are the functions that belong to objects
#list methods
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.index("mom")  #get index for "mom"
fam.count(1.73)  #count times 1.73 occured in list
#string methods
sister = "liz"
sister.index("z")  #get index of the string
sister.capitalize()  #capitalize the first letter
sister.replace("z","sa")  #replace "z" with "sa"
#In python, everything is an object; objects have methods associated, depending on type
#some methods can change the object they called on
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam.append("me")
fam.append(1.79)  #add new element to the list
print(fam)
#some other methods
str.upper()  #for string, capitalize all the letter
str.count(sub[, start[, end]])  #for lists and string, count the number of sub-str/list
#most lists methods will change the list they're called on
list.append()  #adds an element to the list
list.extend()
list.remove()  #removes the first element of a list that matches the input
list.reverse()  #reverses the order of the elements

###Packages
#think packages as a directory of Python scripts, each script is a so-called module
#thousands of Python packages available from the internet
#NUMPY, MATPLOTLIB, SCIKIT-LEARN
#Download packages on your own computer: 1. check whether neccessary to install pip.
#                                        2. if neccesary, install pip
#                                        3. import packages
#run /python --version/ in terminal
#run /pip --version/ in terminal
#upgrading pip, run /pip install -U pip/ in terminal
#run /pip install package_name/ in terminal
import numpy as np  #in python console pane
#use of numpy package
np.array([1, 2, 3])
#if only need specific function in a package
from numpy import array
array([1, 2, 3])  #don't need to use np. anymore
#HOWEVER, the more standard import numpy call is preferred.
#to use the constant pi, need math package
import math
print(math.pi) #must use math. before calling the constant pi.
from math import radians  #radians equals to 2π * Degree / 360
#import the function in the subpackage
from package.subpackage import function as ...

# =============================================================================
# NUMPY
# =============================================================================

###NumPy is the short for Numeric Python
#For basic python, we can't calculate list and integer together
#Alternative to Python List: Numpy Array, can do calculations over entire arrays
#NumPy array can only contain only one type
np.array([1.0, "is", True])
#NumPy array can do calculations
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.3, 88.4, 68.7])
bmi = np_weight / np_height ** 2
print(bmi)
#Difference between list and NumPy array
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])
python_list + python_list
numpy_array + numpy_array
#Another way to do subsetting
bmi[1]  #general index
bmi[bmi > 23]  #boolean index
print(type(bmi))  #the type of NumPy array is numpy.ndarray
#ndarray = N-dimensional array

###2D NumPy Arrays
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                 [65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_2d.shape)  #2 rows, 5 columns
print(np_2d.ndim)
np_3d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                 [65.4, 59.2, 63.6, 88.4, 68.7],
                 [65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_3d.shape)  #2 rows, 5 columns
print(np_3d.ndim)
np_2d[0][2]  #select the first row and the third column
#Special index for NumPy array
np_2d[0,2]  #returns exactly the same value
np_2d[:,1:3]  #returns all rows and the second to third column

###Numpy: Basic Statistics
np.mean()  #don't forget to start with np.
np.median()
np.corrcoef( , )  #check the correlation
np.std()  #check the standard deviation
np.round( , decimal)
np.random.normal(mean, std, n)  #sample random distribution
np.column_stack(( , ))
np.vstack(( , ))
#others like sum(), sort() also exists in basic python, but different in speed!!!



































