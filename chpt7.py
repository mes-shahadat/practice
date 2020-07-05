dots = ".........................................................................................................."
numlis = [1,2,3,45, [5,6,7], [12,34]]
print (numlis[4])#we use [index] method to access list
user = {'name' : 'mes shahadat', 'age' : '17'}#dictionary means unorder(means can't use index) collection of data in key:value pair {means(name:'mes shahadat')}
user1 = dict(name = 'mes shahadat' , age = 17)# you can write dictionary this way also
print (user)
print (user1)
print (user['name'])#we use keys to access dictiontionary values
print (user1['age'])
user_info = {}#empty dictionary
user_info['name'] = 'mes'# add to empty dictionary via this method
user_info['age'] = 17
user_info['favorite content'] = ['anime']
user_info['favorite music'] = ['english nightcore songs']
moreinfo = {"name":"mes shahadat","hobby" : "playing games", "friends" : ["zihad, antor, rahim"]}
user_info.update(moreinfo)# update method in dictionary will not just add but will update values if found an key releated to that
print (user_info)
print (dots)
user_infopoped = user_info.pop('friends')#using pop methos just input the key and it will remove whole key and value and will only return popvalue
#or you can use .popitem() it will remove any random key and value
print (f"your poped item is {user_infopoped}")
if 'name' in user_info:#check if key is present or not #doesn't check for value only checks for keys
    print ('key present')
else:
    print ('key not present')
if 'mes shahadat' in user_info.values():#.values() is used to check if value is present or not like str or [list] values
    print ('value present')
else:
    print ('value not present')
print ("keys:")
for i in user_info:
    print (i)
print ("values:")
for i in user_info.values():
    print (i)
user_info_values = user_info.values()# this values method shows all values so we can use loop
print (f"values = {user_info_values}")
user_info_keys = user_info.keys()# this keys method shows all keys so we can use loop
print (f"key = {user_info_keys}") 
mesitem = user_info.items()# item method important  # item method is used so we can see all items in tuple form
print (mesitem)
print (dots)
for key, value in user_info.items():# item method is used for this
    print (f"your {key} is: {value}")
user2 = {
    'name' : 'mes shahadat',
    'age' : 17,
    'favorite_content' : 'anime',
    'favorite music' : 'nightcore',
}
print (user2['favorite_content'])
# user3 ={#error codes i will learn this later by practicing projects
#     user4 : {
#         'name' : 'antor',
#         'age' : 17,
#         'favorite content' : 'hot hindi movies',
#         'favorite music' : 'hot sexy songs',
#     },
#     user5 : {
#         'name' : 'zihad',
#         'age' : 17,
#         'favorite content' : ['social media' , 'youtube'],
#         'favorite music' : 'hindi hot songs',
#     }
#     user6 : {
#         'name' : 'rahim',
#         'age' : 17,
#         'favorite content' : ['porn', 'top movies'],
#         'favorite music' : 'hindi songs',
#     }
# }
# print (user6('name', 'favorite content'))
#test = {'name' : unknown , 'age' : 'unknow' , 'hight' : 'unknown'}
test = dict.fromkeys(['name', 'age', 'hight'],'unknown')#dict.fromkeys method
print (f"test = {test}")
test2 = dict.fromkeys("abc", 'unknown')#dict.fromkeys method in str key
print (f"test2 = {test2}")
test3 = dict.fromkeys(range(1,11),"unknown")#dict.fromkeys method in key range function
print (f"test3 = {test3}")
test4 = dict.fromkeys(['name', 'age', 'hight'], ['unknown', 'unknown'])# dict.fromkeys method with list value
print (f"test4 = {test4}")
# print (test['hobby'])#this method show error if the key is not present
print (test.get('hobby'))# .get method doesn't show error even if the key is not present #.get is batter method for accessing keys
print (test.get("mess" , "not found !")) #or you can use any other string instead of none
if test.get('hobby') in test:
    print ('present')
else:
    print ('not present')
test0 = test.copy()#.copy method # copy from a dictionary and copy it to another dictionary which you can treat like a completly different dictionary
test.clear()# .clear method
print (f"test = {test}")
print (f"test0 = {test0}")
test5 = {'name' : 'messy', 'age' : 23 , 'hobby' : 'watchin tech', 'age':17}# if same keys present more times the last key will be used not the first keys
print (f"test5 = {test5}")
def getcub (k):
    cube = {}
    for i in range (1,k+1):
        cube [i]= i **3
    return cube
print (getcub(10))
def dictionary_counter (n):#.count in dictionary
    count = {}
    for i in n:
        count[i] = n.count(i)
    return count
print (dictionary_counter('mes shahadat'))
testpro = {}
name = input("what is your name ")
age = int(input ("what is your age "))
fav_movie = input ("input 3 movies name that you like. separated with comma ").split(",")
fav_song = input("plz input your favorite songs. separated with comma ").split(",")
testpro['name'] = name
testpro['age'] = age
testpro['fav_movie'] = fav_movie
testpro['fav_song'] = fav_song
for key,value in testpro.items():
    print (f"your {key} is {value}")
s = {1,2,3.0,'string'}#this is called set data type, you can't add [list], {dict} or (tuple) in set data type
print (f"s = {s}")
s1 = {1,2,3,4,3,3,4,5,6,7,5,5,5,5,5,8}#can't use index to access set #set will ignore duplicate sets and will only show uniqe sets and only be count once
print (f"s1 = {s1}")
s2 = {1.0,2,1,3}#in set if int and float values are same the first will be shown other will be ignored
print (f"s2 = {s2}")
s3 = {22,34,64,91}
s3.add(55)#using .add method you can add set in sets data type
print (f"s3 = {s3}")
#set is used for removing duplicate items
listt = [1,2,3,4,4,4,5,5,6,7,5,5,5,7,7,8,8,9,8,7,9]
s4 = list(set(listt)) #set() is used to remove duplicate eliment from list
print (f"s4 = {s4}")
s5 = {1,2,3,4,5,8}
s5.add(6) #.add () method is used for adding eliment in set data type
s5.add(7)
s5.add(5)
print (f"s5 = {s5}")
s5.remove(8) #.remove is use to remove an eliment for set data type and will give error if eliment is not found to remove
s5.discard(9) #.discard () is best for removing cause even if eliment is not present it will not give any error
print (f"s5 = {s5}")
s6 = s5.copy()
s5.clear()#.clear is used for clearing set
print (f"s5 = {s5}")
print (f"s6 = {s6}")
print (dots)
if 6 in s6:#use in method to check if item is present or not
    print ("present")
else:
    print ("not present")
for i in s6:#loop in set
    print (i)
#set maths
s7 = {1,2,3,4,5,6}
s8 = {1,2,3,4,5,6,7,8,9}
s9 = s7 | s8# | is called pipe or union to perform union math methics
print (s9)
s10 = s7 & s8# & is used for intersection mathmathics in python
print (s10)