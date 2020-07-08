names = ['mes', 'zihad', 'yasin']
pos = 0
for i in names:
    print(f"{pos} ----> {i}")
    pos += 1

for pos, i in enumerate(names):
    print (f"{pos} ----> {i}")
def pos_finder(l,target):
    for pos, i in enumerate(l):
        if i == target:
            return pos
    return -1
print (pos_finder(names,"mess"))
##map without function, i used lambda for function
numbers = [1,2,3,4]
square = list(map(lambda l: l**2, numbers))# you can also loop in map but only once then you can't loop in map again, for unlimited loop you have to convert it to tuple or list
print (square)
squares_new = [i**2 for i in numbers] #list comprehension
print(squares_new)
words = ['abc', 'abcd', 'abcde']
lenth = list(map(len, words))
print (lenth)
numbers1 = [1,4,2,5,8,9,7,3,6]
even = filter(lambda i: i%2 == 0, numbers1)# filter function
print (list(even))
even2 = [i for i in numbers1 if i%2==0]
print (even2)
users = ['user1', 'user2', 'user3', 'user4']
first_name = ['mes', 'antor', 'mohammad', 'abdur']
last_name = ['shahadat', 'das', 'zihad', 'rahim']
print (list(zip(users, first_name, last_name)))# you can print any list in zip with list type
print (dict(zip (users,first_name)))# you can print only two list in zip with dictionary
list2 = [(1,2),(3,4),(5,6),(7,8)]
l1, l2 = list(zip(*list2))
print (list(l1))
print (list(l2))
l3 = [1,3,5,7,9]
l4 = [2,4,6,8,10]
new_list = []
for i in zip(l3,l4):# for loop with zip
    new_list.append(max(i))
print (new_list)
def avareg_finder (*args):
    avareg = []
    for pair in zip(*args):
        avareg.append(sum(pair)/len(pair))
    return avareg
print (avareg_finder([1,2,3] , [4,5,6], [7,8,9]))
avareg_finder2 = lambda *arg: [sum(i)/len(i) for i in zip(*arg)]
print (avareg_finder2([1,2,3] , [4,5,6], [7,8,9]))
def my_sum (*args):
    total = 0
    if all ([type(arg) == int or type(arg) == float for arg in args]):# all, any function
        for i in args:
            total += i
        return total
    else:
        return 'wrong input'
print (my_sum(1,2,3,4,5,6,7,8,9, 'my dick is big' ))
names = ['mes shahadat', 'abdur rahim', 'mohammad zihad', 'antor das']
print (max (names, key = lambda item: len(item)))# advance use of max or min. with lambda function check which string is bigger
students = [
    {'name':'harshit', 'score':90, 'age':24},
    {'name':'mohit', 'score':70, 'age':19},
    {'name':'rohit', 'score':60, 'age':25}
]
print (max(students, key = lambda item: item.get('score'))['name']) # to check max from dictionary

students1 = {
    'harshit' : {'score':99, 'age':24},
    'mohit' : {'score':75, 'age':19},
    'rohit' : {'score':76, 'age':23}
}
print(max(students1, key = lambda item : students1[item] ['age']))# to check max from a complex dictionary

fruits = ('grapes', 'mango', 'apple')
print (sorted(fruits))# sorted gives you sorted list of tuple but not change the actual tuple
print (fruits)
fruits2 = {'grapes', 'mango', 'apple'}# sorted gives you sorted list of set but not change the actual set
print(sorted(fruits))

guitars = [
    {'model': 'yamaha f310' , 'price' :8490},
    {'model': 'faith naptune', 'price':50000},
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 4500000}
]
print (sorted(guitars, key = lambda d: d['price'], reverse = True))

def add (a,b):
    '''add 2 numbers or string and return sum of that numbers or returns strings side by side'''
    return a+b
print (add(2,3))# you can write doc center of '''''' single quote. this is really helpful for developers to understand what this function is maded for

def squares (a):
    return a**2
s = squares
print (s (7))
print (s.__name__) # you can use .__name__ to see the variables function

print (add.__doc__)#use (function name).__doc__ to check the doc name like (sum.__doc__)
print (sum.__doc__)
print (help(max))# or you can use help() to check what that built in function is used for