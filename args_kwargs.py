#args takes arguments and make it tuple in this way a methot not bounded to number of arguments 
#any number of arguments can use function 



'''

What is Unpacking (*) in Python?

Unpacking means taking a collection (like a list, tuple, or set) and splitting its elements into individual values.

In Python, the * operator is used to unpack values.

If you pass a list directly into a function, Python treats it as one single argument — no matter how many items are inside the list. you use * to unpack the list

'''

def my_sum(*args):
    total = 0
    for i in args: #not using range here because length is not fixed 
        total += i

    return total 

numbers = [2,3,4]
print(my_sum(*numbers))

print(my_sum(2,3,7,8,9,0)) #tupple
print(my_sum(*{4,6,7,3,2}))

'''
args is just a name; it could be anything (*numbers, *values, etc.)

The * is what actually tells Python:

“Collect extra positional arguments into a tuple.”

'''

#kwargs used with dictionary 

def func1(*args, **kwargs):
    print(args)
    print(kwargs)


func1(2,3,4, jack=23, mil = 34, mae= 20) 
