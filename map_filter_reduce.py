'''
map() is a built-in function that applies a function to every item in a list (or any iterable) and returns a new sequence (a map object).
map(function, iterable)
function → What you want to do to each item

iterable → List, tuple, etc.

'''

numbers = [2,4,5,6]

def sequare(x):
     return x*x

numbers = list(map(sequare,numbers))

print(numbers)

'''
filter the output based on the provided function

'''

numbers = [10,677,899,34,6]

numbers = list(filter(lambda x: x>9, numbers))
print(numbers)

'''
reduce

from functools import reduce
reduce(function, iterable)
function → A function that takes two values and returns one

iterable → List, tuple, etc.

'''
from functools import reduce 
numbers = [2,3,4,5,6]
sum = reduce(lambda x,y: x+y,numbers)
print(sum)


