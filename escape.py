# #  ********print this following lines*******
# # this is \\ double  black slash
# # these are /\/\/\/\/\/\/\ mountains
# # he      is awesome ( use escape sequence insrtead of manual spaces)
# # \" \n  \t \' ( print this as an output) ( use escape sequence as normal text )




# print (" this is \\\\ double blackslash") # \\= \, \\\\=\\ 
# print ( " these are /\/\/\/\/\ mountains \n he \t is awesone") # or type /\\/\\/\\/\\/
# print ( " \\\" \\n \\t \\\' ")
# print (r" \" \n \t \' ") # use r to ignore any escape sequence and print it as a plain text
# print ("\U0001F602")
# print (" emozi \U0001F97A yomozi \U0001F47B moneymozie \U0001F911") # use emozi in python with unicode




# # operators
# print (2+2)
# print (4-4)
# print (4*4)
# print (10/5)
# print (10//5)
# print (10**10)
# print (5%10)


# #variables
# name = "mes"
# print (name)
# mes = "smart guy"
# print (mes)
# number420 = "don't say that word kid"
# print (number420)



# #strings
# first_name = "mes "
# last_name = "shahadat "
# print (first_name)
# print (last_name)
# print (first_name + last_name)
# print ( (first_name + last_name) *3 )



# #input function
# name = input ( "type your name ")
# print ( "welcome " + name )


# #int- function
# number_one = input ( "write your first number ")
# number_two = input ( "write your second number ")
# total = number_one + number_two
# print ( "your number is " + total )


# number_one = int (input ( "write your number "))
# number_two = int (input ("write your second number "))
# total = number_one + number_two
# # print (" your number is" + str(total))
# print (" your float number is" + str(total))



# # multiple variables
# name, age = "mes", "17"
# print ( "your name is " + name + " your age is " + age )

# x=y=z=1
# print (x+y+z)




# name, age = input ( " input your name and age with coma in between ") .split (",")
# print ("your name is " + name)
# print ("your age is " + age)


name, age = "mes", 17
print (f"hello {name} your age is {age}")