# Define functions without parameters
# Define functions with one parameter
# Define functions that return a value
# Later: multiple arguments, multiple return values

# =============================================================================
# FUNCTIONS
# =============================================================================

### Define functions without parameters
def square() :              # Function header
    new_value = 4 ** 2          # Indented function body
    print(new_value)            # Indented function body
square()

### Define functions with one parameter
# Docstrings should be places In between triple double quotes """. in the immediate line a!er the function header
def square(value) :                         # Function header with single parameter
    """Return the square of a value."""         # Docstrings: describe what your function does
    new_value = value ** 2                      # Indented function body
    print(new_value)                            # Indented function body
    return new_value                            # Assign it to some variable
num = square(5)
print(num)

### Define functions with multiple parameter and return values
def raise_to_power(value1, value2) :
    """Raise value1 to the power of value2."""
    new_value = value1 ** value2
    return new_value
result = raise_to_power(2, 3)
print(result)
def raise_both(value1, value2) :
    """Raise value1 to the power of value2 and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return new_tuple
result = raise_both(2, 3)
print(result)

### Practices
# Import pandas
import pandas as pd
# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('tweets.csv')
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    # Initialize an empty dictionary: langs_count
    langs_count = {}
    # Extract column from DataFrame: col
    col = df[col_name] 
    # Iterate over lang column in DataFrame
    for entry in col:
        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] = langs_count[entry] + 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1
    # Return the langs_count dictionary
    return langs_count
# Call count_entries(): result
result = count_entries(tweets_df, 'lang')
print(result)

### Scope
# Scope - part of the program where an object or name may be accessible
# Global scope - defined in the main body of a script Local scope - defined inside a function
# Built-in scope - names in the pre-defined built-ins module

# Global scope
new_val = 10
def square(value) :
    global new_val              # Use team in global scope
    new_val = new_val ** 2
    return new_val
square(9)
print(new_val)

# Built-in scope
import builtins
dir(builtins)

# =============================================================================
# NESTED FUNCTIONS
# =============================================================================

def outer() :
    """Prints the value of n."""
    n = 1
    def inner() :
        nonlocal n          # Use nonlocal to create and change names in an enclosing scope.
        n = 2
        print(n)
    inner()
    print(n)

# Scope searched by LEGB rule: local > enclosing > global > built-in

# Practices
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    echo_word = word * 2 
    print(echo_word)
    def shout():
        """Alter a variable in the enclosing scope"""    
        nonlocal echo_word   
        echo_word = echo_word + '!!!'
    shout()
    print(echo_word)
echo_shout('hello')

#### Default and Flexible arguments
#Default arguments
def power(number, pow=1) :
    """Raise number to the power of pow."""
    new_value = number ** pow
    return new_value
power(9,2)
power(9)
#Flexible arguments
def add_all(*args) :                            # use *args or **kwargs
    """Sum all values in *args together."""
    sum_all = 0
    for num in args :
        sum_all += num
    return sum_all
add_all(4,9,1,3,6,8)
# **kwargs turns the identifier-keyword pairs into a dictionary within the function body.
def print_all(**kwargs) :
    """Print out key-value pairs in **kwargs"""
    for key, value in kwargs.items() :
        print(key + ': ' + value)

# Practice 1
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    for key, value in kwargs.items():
        print(key + ": " + value)
    print("\nEND REPORT")
report_status(name='luke', affiliation='jedi', status='missing')
report_status(name='anakin', affiliation='sith lord', status='deceased')

# Practice 2
# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of occurrences as value for each key."""

    cols_count = {}
    for col_name in args:
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
    return cols_count
result1 = count_entries(tweets_df, 'lang')
result2 = count_entries(tweets_df, 'lang', 'source')
print(result1); print(result2)

### Lambda Functions
raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3)
nums = [48, 6, 9, 21, 1]

# map(func,seq) function applies a function over an object
square_all = map(lambda num: num ** 2, nums)
print(list(square_all))

# filter(func,seq) may filter out elements from a list that don't satisfy certain criteria
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
result = filter(lambda member: len(member) > 6, fellowship)
result_list = list(result)
print(result_list)

# reduce() function is useful for performing some computation on a list, returns a single value
from functools import reduce
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
result = reduce(lambda item1, item2: item1 + item2, stark)
print(result)

# =============================================================================
# TUPLES
# =============================================================================
# 1. Similar ot Lists, but are immutable
# 2. Constructed usign parentheses ()
even_nums = (2, 4, 6)
print(type(even_nums))
a, b, c = even_nums
print(a); print(b); print(c) #Unpack a tuple into several variables
print(even_nums[1]) #Access tuple elements like you do with lists

# =============================================================================
# ERROR HANDLING
# =============================================================================

### Passing invalid argument

# Catch exceptions with try-except clause
def sqrt(x):
    """Returns the square root of a number"""
    try :
        return x ** 0.5
    except :    # if there is an error
        print('x must be an int or float')
sqrt(4)
sqrt('wrong')
def sqrt(x):
    """Returns the square root of a number"""
    try :
        return x ** 0.5
    except TypeError:   # only detect TypeError
        print('x must be an int or float')

# use 'raise' to raise a ValueError
def sqrt(x) :
    """Returns the square root of a number."""
    if x < 0 :
        raise ValueError('x must be non-negative')
    try :
        return x ** 0.5
    except TypeError :
        print('x must be an int or float')
sqrt(-2)














