# making functions
dots = "............................................................"
def add_two(mes , shahadat):
    return (mes+ " ") + (shahadat)
print (dots)
first_name = input ("input your first name: ")
last_name = input ("input your last name: ")
full_name = add_two (first_name, last_name)
print (f"your full name is: {full_name}")
print ("or without saving in variable ")
print (f"your full name is: {add_two(first_name, last_name)}")
print (dots)
def add_num(a,b,c):
    print (a+b+c)
md = int(input ("input your 1st number: "))
mes = int(input("input your 2nd number: "))
shahadat = int(input ("input your 3rd number: "))
print ("your total is: ")
add_num(md,mes,shahadat)
print (dots)
def first_char(a):
    return a[-1]
func_name =input ("plz input a name: ")
firstchar = first_char(func_name)
print (f"your names last character is: {firstchar}")
print (dots)
def song():
    return "thank you"
empty = input ("dont input anything, just enter ")
if empty == "":
    print (song())
else:
    print ("i said not to type anything")
print (dots)
#motherfucker odd even practice with function
def odd_even(num1):
    if num1%2 == 0:
        return "true"
    else:
        return "false"
userodd = int (input ("plz input a number to see if it's even or odd "))
print (odd_even(userodd))
print ("testing with 1 line code with adding 1 with user input:")
def even_odd(num2):
    return num2%2 == 0
print (even_odd(userodd+1))
print (dots)
def bigger(num3, num4):#success at first try
    if num3 < num4:
        return num4
typ1, typ2 = input("plz input 2 number with coma in between {to see which is bigger}: ").split(",")
print (f"{bigger(typ1, typ2)} is bigger")
print (dots)
def greater(nu1, nu2, nu3):
    if nu1 > nu2 and nu1 > nu3:
        return nu1
    elif nu2 > nu1 and nu2 > nu3:
        return nu2
    else:
        return nu3
print ("input number to see which is bigger")
n1 = int(input("plz input a number "))
n2 = int(input("plz input a number again "))
n3 = int(input("plz input another number "))
print (f"{greater(n1, n2, n3)} is greater")
print (dots)
# palindrome pracice
def user_word (word):
    return word[ : : -1] == word
user_pal = input ("plz input a palindrome word {means word is same even when you reverse like 'nanan'}: ")
print (f"palindium = {user_word(user_pal)}")
print (dots)
#fibonaci sequence
def febonaciseq (n):
    a = 0
    b = 1
    if n == 0:
        print (a) 
    elif n == 1:
        print (a,b )
    else:
        print (a, b, end = " ")
        for i in range (n-2):
            c = a+b
            a = b
            b = c
            print (b, end = " ")
feb = int(input("plz input a number to febonaci sequence: "))
febonaciseq(feb)
#default parameter in function
print (dots)
def user_info (firstname = "unknown", lastname = "unknown", age = None):
    print (f"\nyour first name is {firstname}")
    print (f"your last name is {lastname}")
    print (f"your age is {age}")
user_info()
print ("without any input this function will not show error it will show like above")