# this is an implementation of data structures and algorithms

############################################################
# Part I Python Primer
############################################################

# computing the sum of a list of numbers
# (build-in sum() function)
total = 0
for val in data:
    total += val

# finding the maximum value in a list of elements
# (build-in max() function)
biggest = data[0]
for val in data:
    if val > biggest:
        biggest = val

# find the index of the maximum element of a list
big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j

############################################################
# Define a Function
#
def count(data, target):
    n = 0
    for item in data:
        if item == target:  # found a match
            n += 1
    return n

# objects that passing to and from a function are not copied

# mutable parameter
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

# open a file
# open(), return a proxy for interactions with the underlying file

###################################################################
# 1.7 Exception Handling
# to be continued

#####################################################################
# iterator
# an object that manages an iteration through a series of values.

# iterable
# an object, obj, that produces an iterator via the syntax iter (obj).

# the for-loop syntax in Python simply automate the iteration process,
# creating an iterator for the give iterable, and then repeatedly calling
# for the next element until catching the StopIteration exception

# Python also supports functions and classes that produce an implicit
# implicit iterable series of values, that is, without constructing a
# data structure to store all of its values at once.
# For example, range(10000), does NOT return a list of numbers;
# it returns a range object that is iterable.

# generator
# use yield, instead of return, and not both
# the results are only computed if requested,
# and the entire series need not reside in memory at one time.

# Conditional expression
# itself can serve as a parameter to the function
result = foo(n if n >= 0 else -n)

# Comprehension syntax
#
# list comprehension
squares = [k*k for k in range(1, n+1)]
# set comprehension
{ k*k for k in range(1, n+1) }

# generator comprehension
( k*k for k in range(1, n+1) )

# dictionary comprehension
{k: k*k for k in range(1, n+1) }


##
# If a series of comma-separated expressions are given in a larger context,
# they will be treated as a single tuple, even if no enclosing parentheses
data = 2,3,4,6,8
# assigned tuple(2,3,4,6,8)
# this is called automatic packing of tuple

##
# simultaneous assignments
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
