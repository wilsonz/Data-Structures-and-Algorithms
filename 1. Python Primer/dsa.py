# this is an implementation of data structures and algorithms

# Part I Python Primer
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

# add a function
def count (data, target):
    n = 0
    for item in data:
        if item == target:  # found a match
            n += 1
    return n
