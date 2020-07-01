number = [1, 2, 3, 4, 5, 6]
word = ["word1", "word2", "word3", "word4", "word5", "word6"]
mixed = ["char1", "char2", "char3", 4,5,6, 3.35, None]
print (number)
print (word)
print (mixed)
#slicing list
print (number[1])
print (word[ :3])
print (mixed[-1])
mixed[1: ] = ['two', 'three']
print (mixed)
#append method to add into list
mes = ["mes1", "mes2"]
mes.append("mes3")
print (mes)
fruits = ["apple", "mango", "grapes"]
fruits.append("mango")
fruits.append("strawbarry") #append is batter for only 1 string
fruits.append("apple")
fruits.append("cocumber")
print (fruits)
#but if i want to add variable
fruits1 = ["bitches", "whores"]
# fruits.append(fruits1) #adds a a list. so, the batter method is .extend
# print (fruits)
fruits.extend(fruits1) #extend is batter
print (fruits)
fruits.insert(3, "banana") #insert is used for inserting a string at certain position
print (fruits)
fruits.pop(3) # by default .pop() will remove the last string
print (fruits)
fruits.remove("bitches") # if string is not available there will be x not list error #used for removing written string
print (fruits)
del fruits[-1] #using del operator you can remove string via index number
print (fruits)
if "django" in fruits: #check if eliment is present in your list or not
    print ("django is present")
else:
    print ("django is not present")
print (fruits.count("apple"))
fruits.sort() # sort the original list
print (fruits)
sornum = 5,6,12,1,3,4,9
print (sorted (sornum)) #not sorted the actual list but shows sorted 
fruits1_2 = fruits1.copy()
fruits1.clear()
print (fruits1)
print (fruits1_2)
print (fruits1)
for fruit in fruits: #for loop in list
    print (fruit)
spoiled = ["mes", "shahadat"]
print (",".join(spoiled))
print (type(spoiled))#with type function you can check variable class (see if it's str, int, or list or special character)
#list inside list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print (matrix[0][2])# to print from list of list
for sublist in matrix:
    for i in sublist:
        print (i, end = " " )
numbers = list(range(1,11))
numbers.pop()
print (numbers)
cherrypop = numbers.pop()#.pop can also show the deleted number if you want to see
print (cherrypop)
nambers = [1,2,3,4,5,6,7,8,9,10]
print (nambers.index(9))#.index shows the inputted string position in index number 0,1 i mean
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print (negative_list(nambers))
snum = list(range(1,11))
def square_num(n):
    squarevalue = []
    for i in n:
        squarevalue.append(i*i) #or i**2 that is harshits vashisth uses for squaring
    return squarevalue
print (square_num(snum))
testrev = list(range(1,11))
def reversefunc(mess):
    messreverse = []
    for i in range(len(mess)):
        poped = mess.pop()
        messreverse.append(poped)
    return messreverse
print (reversefunc(testrev))

lis1 = input ("plz input 3 words : ")
lis2 = input ("plz input 3 words : ")
lis3 = input ("plz input 3 words : ")
three = []
three.append(lis1)
three.append(lis2)
three.append(lis3)
# def revthree (l):
#     return three[0][ : :-1],three[1][ : :-1],three[2][ : :-1]
# print (revthree(three))
def reberse (r):
    reb = []
    for i in r:
        reb.append(i[ : :-1])
    return reb
print (reberse(three))
filteroddeven = [1,2,3,4,5,6,7,8,9,10]
def forfilter (oel):
    odd = []
    even = []
    for i in oel:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even
print (forfilter(filteroddeven))
def similar(sim1, sim2): #check matrix for list input
    similar_num = []
    for i in sim1:
        if i in sim2:
            similar_num.append(i) 
    return similar_num
print (similar([1,2,3,4,5], [1,2,4,5,6,8,9]))
minmaxnum = [60,99,2,10]
print (f"maximum numbers from minmaxnum is: {max(minmaxnum)}")#max function is used for showing maximum number
print (f"minimum numbers from minmaxnum is: {min(minmaxnum)}")#min function is used for showing minimum number
def max_minimum (liss):
    return max(liss) - min(liss)
print (f"max - min = {max_minimum(minmaxnum)}")
threelist = [[1,2,3,4],[5,6,7,8],[9,10,11]]
def for_checking_type(tl):
    count = 0
    for i in tl:
        if type(i) == list:
            count += 1
    return count
print (for_checking_type(threelist))