mixxes = (1,2,3,4,5.0)# not list cause starts with (), it's tuple means immutable list you can say
for i in mixxes:
    print (i, end = " ")
print (type(mixxes))
tupri = (1, ) #to make one elimant tuple you have to input comma at the end or else it will be a str or int
print (type(tupri))
stare = ("eyes",)# have to use , at the end or it will be used as str
print (type (stare))
withouple = 'tuples', 'without', 'paranthesis'# make tuple without parenthesis
print (type(withouple))
print (min(mixxes))
print (max(mixxes))
print (sum(mixxes))
tupnums = tuple(range(1,11))#you can create like list
print (tupnums)
liststr = str([1,2,3,4,5,6,7,8,9])
tuplestr = str((1,2,3,4,5,6,7,8,9))#tuple str means output = "(1,2,3,4,5,6,7,8,9)"
print (liststr)
print (tuplestr)
friends = 'zihad', 'antor', 'rahim'#this is called tuple unpacking
friend1, friend2, friend3 = friends
print (friend2)
dialouge = ('i', 'me', 'and', 'myself', [ 'an', 'idiot', 'said', 'that' ] )#you can add a list and modify that list even if it's in tuple
print(dialouge[4].pop())
print (dialouge)
dialouge[4].append("what kind of idiot say that")
print(dialouge)
def add_multiply(int1, int2):
    add = int1+int2
    multiply = int1*int2
    return add , multiply#this gives output as tuple
print(add_multiply(5,10))
add1, multiply1 = add_multiply(5,10)#you can save your argument as two different variables
print(add1)
print (multiply1)