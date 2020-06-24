name, age, year= input (" input your name age and year with coma in between ") .split(",")
print (f" your name is {name}, your age is {age} and your birth of date is {year} thank you for your input ")

number1, number2, number3= input (" plz enter 3 numbers with coma to add ignore coma at last ") .split (",")
# print (f"your total number is: {number1} + {number2} + {number3}") # error try
print(f"your total number is: {int(number1) + int(number2) + int(number3)}")



# python string indexing []

language = "python"
# p = 0, -6
# y = 1, -5
# t = 2, -4
# h = 3, -3
# o = 4, -2
# n = 5, -1

print (f"index test {language [5]} ")
        # or
print (f"index test {language [-1]} ")

print("writing python practice with index:")
print(f"test1 {language [0:6]}")
print(f"test2 {language [:]}")
print(f"test3 {language[0:]}")
print(f"test4 {language[:6]}")
print(f"test5 {language[-6:]}")
#     #   or with just string
python = "python"
print(f"string test1 { python [0:6]}")
print(f"string test2 reverse { python [ : :-1]}") # error can't print two strings, created and used python variable to fix

# practice input reverse
name = input("input a name to revese ")
print(f"reverse is \"{name [ : : -1]}\" 'tada' ") # success at first try


your_name = input("plz input your name ")
character = input ( "plz input a character from your name ")

# 1. len ( ) function
#lenth = len(your_name)
#print (lenth)
lenth = (your_name.replace(" ", ""))
print (f"your name lenth is {len(lenth)}") # error can't replace  space has to use variables


#string methods (.lower, .upper, .title, .count)
# 2. lower ( ) method 
print (f"your name in lower class is {your_name.lower()}")

# 3. upper ( ) method 
print (f"your name in upper class is {your_name.upper()}")

# 4. title ( ) method 
print (f"your name in title is {your_name.title()}")

# 5. count ( ) method
print (f"your character count is {your_name.count(character)}")

print (f"your name in reverse is {your_name.upper() [ : : -1]}") #test for reverse string method

name, word = input("input your name and type a latter with comma in between ") .split (",")
print (f"welcome {name}. your name lenth is {len(name)}, and your \"{word}\" word is used {name.lower().count(word.lower())} times ") # old practice

name, word = input ("input your name and a word with coma in between ").split(",")
print(f"hello {name.strip()}. your name contains {len(name.strip())} caracters, and the {word} character is used {name.strip ().lower().count(word.strip().lower())} times in your name ") # incensitive case practice success at first try #new


# #string method replace, and find practice
remember = "If you learn or read something that doesn't work in real life and gives no profits in real life than that is entertainment. avoid entertainment like movies, news, or any kind of none educational videos"
print (remember.replace(" ", "_"))
profit = input("input a word from above to find in this line ")
print (f"the word {profit} is at {remember.find(profit)} ")


name = input ( "what's your name ")
print ("you are smart ")
print (name.center(len(name)+4, "*"))