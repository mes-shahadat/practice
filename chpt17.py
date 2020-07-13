dots = "................................................................................................."
#chapter 17
#import pdb
## l command is used for next line
## n command is used for execute
## c command is used for continue
## q command is used for quit
name = input("plz input your name ")
age = input ("plz input your age ")
year = int(input ("plz input current year "))
# pdb.set_trace()
print (f"ok {name} i got it, you are {age} years old")
age2 = int(age) + 5
year2 = year + 5
print (f"listen {name} after 5 years in {year2} you will be {age2} years old")

print (dots)
##chapter 18
f = open('New Text .txt')# used open() function to open files
print (f"cursor point... {f.tell()}")
print (f.read())# used read() method to read file's content in str 
print (f.read())# even if you use the same read method twice it will only give you print only once
print (f"cursor point... {f.tell()}")
print ('resetting seek to 0....')
f.seek(0) # used seek() method to seek cursor to 0 
print (f.read())# using seek method i can again print the file 
f.close()# used close() method, it's batter to use close method after your files work has done or it can may give you problem later
print (dots)
n = open (r"P:\New folder for txt file\New Text (2).txt")
print (n.readline(), end='')# readline method is used to print only one line from file
print (n.readline(), end='')
print (n.readline())
n.close()#after closing you have to open again if you want to use code on it
print (dots)
m = open (r"P:\New folder for txt file\New Text (2).txt")
lines = m.readlines()# readlines() is used to add all the content from file to variable as a list
print (lines)
print (len(lines))#it's showing it has 3 lines
for line in lines:# you can loop the lines readlines f or variable
    print (line, end='')
print (f"\n{dots}")
for lines in m.readlines()[ :2]:# you can loop readlines like this also, because used first now it will not print quotes again
    print (line, end='')
print (f'\n{m.name}')# .name data discriptor (means don't have to put () at the end) is used for to chcek the file name
print (f'\n{m.closed}')# .closed data discriptor (means don't have to put () at the end) is used to see if the file is closed or not
m.close()
print (dots)
## default open and call is:
## print (dots)
## f = open('New Text .txt')
## print (f.read())
## f.close()
## batter is:
with open('New Text .txt') as f:#with block, context manager
    data = f.read()
    print (data)
print (f.closed)
print (dots)
with open('file.txt', 'w') as a:# w overwrite everything from file (if it has or else it creates a new file)
    a.write('hello there, iam here')
with open('file1.txt', 'a') as a2:# a append everything at the end of file (if it has or else it creates a new file)
    a2.write('\nhello here, iam there go meet me there\n')
with open('file2.txt', 'r+') as a3:# r+ overwrite every word at first till the end and can't create files
    a3.seek(len(a3.read()))
    a3.write("hello there, i don't know iam where. can u tell me where am i ")
print (dots)
with open('new_file.txt') as rf:#readed a file then copy that content to new file
    with open('new_file1.txt', 'w') as wf:
        wf.write(rf.read())

with open('salary.txt') as rs:
    with open('output.txt', 'a') as ro:
        for line in rs.readlines():
            name,salary = line.split(',')
            ro.write(f'{name}\' salary is {salary} \n')
f = open('output.txt')
print (f.read())

from csv import reader

with open('file.csv', 'r') as f:
    csv_reader = reader(f)
    next(csv_reader)
    for row in csv_reader:
        print (row)
print (dots)
from csv import DictReader

with open('file1.csv', 'r') as f:
    csv_reader = DictReader(f,delimiter='|')
    for row in csv_reader:
        print (row)
        ##print (row['name']) # to print only the value you want with the key

print (dots)
from csv import writer

with open('file3.csv','w', newline='') as f:# write row method 
    csv_writer = writer(f)
    csv_writer.writerow(['Name', 'Country'])
    csv_writer.writerow(['mes', 'bangladesh'])
    csv_writer.writerow(['zihad', 'bangladesh'])

with open ('file4.csv', 'w', newline='') as f:#write rows method
    csv_writer = writer(f)
    csv_writer.writerows([['Name', 'Country'],['mes', 'bangladesh'],['zihad', 'bangladesh']])


from csv import DictWriter
with open ('file5.csv', 'w', newline='') as f:# dict writer with write row
    csv_dict_writer = DictWriter(f, fieldnames=['first_name','last_name','age'])
    csv_dict_writer.writeheader()
    csv_dict_writer.writerow({
        'first_name' : 'mes',
        'last_name' : 'shahadat',
        'age' : 17
    })
    csv_dict_writer.writerow({
        'first_name' : 'mohammad',
        'last_name' : 'zihad',
        'age' : 19
    })
    csv_dict_writer.writerow({
        'first_name' : 'antor',
        'last_name' : 'das',
        'age' : 17
    })

with open ('file6.csv', 'w', newline='') as f:# dict writer with write rows
    csv2_dict_writer = DictWriter(f, fieldnames=['first_name', 'last_name', 'age'])
    csv2_dict_writer.writeheader()
    csv2_dict_writer.writerows([
        {'first_name':'mes ', 'last_name':'shahadat', 'age':17},
        {'first_name':'mohammad ', 'last_name':'zihad', 'age':19},
        {'first_name':'antor ', 'last_name':'das', 'age':18},
        {'first_name':'abdur ', 'last_name':'rahim', 'age':17}
    ])


from csv import DictReader, DictWriter#read and write csv files
with open('file7.csv', 'r') as rf:
    with open ('file8.csv', 'w', newline='') as wf:
        csv7_reader = DictReader(rf)
        csv7_writer = DictWriter(wf, fieldnames=['first_name', 'last_name','age'])
        csv7_writer.writeheader()
        for row in csv7_reader:
            fname, lname, age = row['first_name'], row['last_name'], row['age']
            csv7_writer.writerow({# 😭 for loop use write row, other method i don't know
                'first_name':fname,
                'last_name':lname,
                'age':age
            })