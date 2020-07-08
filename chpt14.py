## to learn decorator first learn this
l = [1,2,3,4]
def square (a):
    return a**2
print (list(map(square, l)))# map takes function as a argument
def my_map(func, l): # this is an function that takes a another function as an argument
    items = []
    for i in l:
        items.append(func(i))
    return items
def my_map2 (func, l):# defind function with list comprehension
    return [func(i) for i in l]
print (my_map(square, l))
print (my_map(lambda a: a**2, l))# used anonymous lambda function as argument
print (list(map(lambda a: a**2, l)))
print (my_map2(square,l))
# function returning function
def outer_func ():
    def inner_func():
        print ("THIS IS INNER FUNCTION. understand it")
    return inner_func ()# () means excecute without () it will just call the function
var = outer_func()

def outer_func2 (msg):
    def inner_func2():
        print (f"your msg is {msg}")
    return inner_func2
var1 = outer_func2 ("hi there")
var1()
def to_power (x):
    def calc_power (n):
        return n**x
    return calc_power
var2 = to_power(3)
print (var2(3))
def decorator_function (function1):
    def inner_decorator():
        print ('this is awesome function')
        function1()
    return inner_decorator
def func1 ():
    print ("this is function 1")
dec = decorator_function(func1)
dec()
@decorator_function# use @dec_func_name to use this decorator shortcut. this shortcut is called syntactic sugar.
def func2 ():
    print ("this is function 2")
func2()
from functools import wraps # imported wrap to show the correct doc and name for functions 
def decorator_func (any_func):
    @wraps (any_func)
    def wrapper_function(*args, **kwargs):
        """ this is wraper function"""
        print ("this is awesome function")
        return any_func(*args, **kwargs)
    return wrapper_function
@decorator_func
def funcs (a,b):
    '''this is add function'''
    return (a+b)
print (funcs(2,3))
print (funcs.__doc__)
print (funcs.__name__)
from functools import wraps
def deco_func(any_func):
    @wraps(any_func)
    def wrapper_function2(*args, **kwargs):
        print (f"you are calling {any_func.__name__} function")
        print (any_func.__doc__)
        return (any_func(*args, **kwargs))
    return wrapper_function2
@deco_func
def add (a,b):
    '''this takes two numbers and return sum of them'''
    return (a+b)
print (add(2,3))
import time
t1 = time.time()
def loop_time(num):
    return ['hello world ' for i in range(0,num) ]
print (loop_time(22))
t2 = time.time()
print (t2 - t1)
import time
from functools import wraps
def calculate_time(any_func):
    @wraps(any_func)
    def wraper(*args, **kwargs):
        print (f'excecuting your "{any_func.__name__}" function')
        t1 = time.time()
        returned_value = any_func(*args, **kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print (f"your function took in total {total_time} time")
        return returned_value
    return wraper
@calculate_time
def square_finder (num):
    return [i**2 for i in range (1,num+1)]
(square_finder(1000))
from functools import wraps
def only_int_func(any_func):
    @ wraps (any_func)
    def wraper(*args, **kwargs):
        if all(type(arg) == int for arg in args):
            return any_func(*args, **kwargs)
        print ("invalid input")
    return wraper
@only_int_func
def add_all (*args):
    total = 0
    for i in args:
        total += i
    return total
print (add_all(1,2,3,4,5))

from functools import wraps
def only_allowed_type(data_type):
    def decorator(any_func):
        @ wraps (any_func)
        def wraper(*args, **kwargs):
            if all(type(arg) == data_type for arg in args):
                return any_func(*args, **kwargs)
            print ("invalid input")
        return wraper
    return decorator
@only_allowed_type (str)
def join_string(*args):
    total = ''
    for i in args:
        total += i
    return total
print (join_string('rohit', 'mohit', 'and others'))