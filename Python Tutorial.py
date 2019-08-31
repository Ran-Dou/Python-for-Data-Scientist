# =============================================================================
# 3. An Informal Introduction to Python¶
# =============================================================================

print(r'C:\some\name')  # note the r before the quote
print("""\
Usage: thingy [OPTIONS]
       -h                        Display this usage message
       -H hostname               Hostname to connect to
""")

# Two or more string literals (i.e. the ones enclosed between quotes) next
# to each other are automatically concatenated.
# only works on literals
'Py' 'thon'
text = ('Put several strings within parentheses '
        'to have them joined together.')

# The keyword argument end can be used to avoid the newline after the output
# space is inserted between items
a, b = 0, 1
while a < 1000:
     print(a, end=',')
     a, b = b, a+b

a = ['Mary', 'had', 'a', 'little', 'lamb']
for key, value in enumerate(a):
   print(key, value)
list(enumerate(a))

print(range(5))
list(range(5))

# The default values are evaluated at the point of function definition in the defining scope
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# The default value is evaluated only once
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
# If you don’t want the default to be shared between subsequent calls
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# In a function call, keyword arguments must follow positional arguments.

# 
pairs = [(1, 'one'), (4, 'two'), (3, 'three'), (2, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

f.__doc__
f.__annotations__
# Return annotations are defined by a literal ->, followed by an expression
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


import nltk








