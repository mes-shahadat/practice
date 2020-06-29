# while loop practice (hello world)
print ("while loop practice: ")
i = 1
while i <= 10:
    print ("hello world ")
    i += 1
# sum with while loop practice
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print (f"total of 10 with loop is = {total}")
dots = "......................................................."
#sum exercise
print (dots)
userinput = int(input ("plz input two number without spaces that you want sum of with loop "))
total = 0
i = 1
while i <= userinput:
    total += i
    i += 1
print (f"total of {userinput} with loop is {total}")
print (dots  )
#sum users inputed numbers
sumnum = input("plz input some single number without spaces to sum: ")
total = 0
i = 0
while i < len(sumnum):
    total += int(sumnum[i])
    i += 1
print (f"total sum is: {total} ")
print (dots)
# count of character used in names # after watching and then took some trials to success
new_name = input("plz input a name: ")
temp = ""
i = 0
while i < len(new_name):
    if new_name[i] not in temp:
        temp += new_name[i]
        print (f"{new_name[i]} : {new_name.count(new_name[i])}")
    i += 1
print ("this many total used characters is in your name ")
print (dots)
# for loop practice
lp = input("type 'yes' to allow loop practice: ")
if lp == "yes":
    print ("loop practice:")
    for i in range (10):
        print ("hello world")
else:
    print ("skipping ")
print(dots)
# sum 10 with for loop
total = 0
for i in range (0,11):
    total += i
print (f"total of 10 with forloop is {total}")
print ( dots )
# user input sum
loopnum = int(input ("plz input some number without spaces: "))
total = 0 
for i in range (1,loopnum+1):
    total += i
print (f"your total {loopnum} with forloop is: {total}")
print (dots)
name_type = input("plz input your number: ")
total = 0
for i in range (0, len(name_type)):
    total += int(name_type [i])
print (f"your total with for loop is: {total}")
print (dots)
loop_name = input ("input your name: ")
loop_temp = ""
for i in range (0, len(loop_name)):
    if loop_name [i] not in loop_temp:
        loop_temp += loop_name [i]
        print (f"{loop_name[i]} : {loop_name.count(loop_name[i])}")
print ("this many total used characters is in your name ")
print (dots)
# break and continue practice 
pt = input ("plz type 'no' if you know break and continue operators: ")
if pt == "no":
    for i in range (1, 11):
        if i == 5:
            break
        print (i)
    for i in range (0, 11):
        if i ==5:
            continue
        print (i)
else:
    print ("skipping")
print (dots)
# number guessing game
print (dots)
print("starting number guessing game: [winning number is 45] ")
winning_number = 45
guess = int(input ("guess a number between 1 to 100: "))
total_guess = 1
game_over = False
while not game_over:
    if guess == winning_number:
        print (f"you win !!! you taked {total_guess} guess to win this game ")
        game_over = True
    else :
        if guess < winning_number:
            print ("too low ")
            guess = int(input ("guess again: "))
            total_guess += 1
        else :
            print ("too high ")
            guess = int(input ("guess again: "))
            total_guess += 1
#random number guessing game with dry code
print (dots)
print ("randomized guessing game, winning is = i don't know")
import random
win_num = random.randint(1,100)
totguess = 0
userguess = int (input ("guess and input a number: "))
rangame_over = False
while not rangame_over:
    if userguess == win_num:
        print (f"you win!!! you taked {totguess} guesses to win this game ")
        rangame_over = True
    else :
        if userguess < win_num:
            print ("too low ")
        else :
            print ("too high ")
        userguess = int (input("guess again: "))
        totguess += 1
print (dots)
# step argument in loop # can't use : instead of , # at the end -1 means reverse
print ("reverse step argument with forloop")
for i in range (10,0,-1): # reverse step argument loop
    print (i)
print ("mes shahadat string for loop without variables")
noob_me = "mes shahadat" #loop code only in python # don't have to use len(name)# you can also use string without variable
for i in noob_me:
    print (i)
print (dots)
lopnu = input ("input some number without spaces to sum with for loop: ")
loptoat = 0
for i in lopnu:
    loptoat += int(i)
print (loptoat)
#end chapter 3 practice