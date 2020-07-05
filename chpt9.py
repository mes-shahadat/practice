##list comprehension with loop
square = [i**2 for i in range (1,11)]
print (square)
negative = [-i for i in range (1,11)]
print (negative)
names = ['mes', 'rahim', 'zihad', 'antor']
name_first_char = [name[0] for name in names]
print (name_first_char)
strings = ['name', 'mes', 'other', 'things']
def reverse (name):
    return [i[ : :-1] for i in name]
print (reverse(strings))
even_nums = [i for i in range (1,11) if i%2 == 0]
odd_nums = [i for i in range (1,11) if i%2 != 0]
print (even_nums)
print (odd_nums)
liss = [4, 'mes', [1,2,3,4], {'fruit': 'mango'}, ('really', 'so,sad'), 1.0, 2.0, 3.0]
def justint_float (l):
    return [str(i) for i in l if type(i) == int or type (i) == float]
print (justint_float(liss))
nums = [1,2,3,4,5,6,7,8,9,10]
new_list = [i*2 if i%2==0 else -i for i in nums]#list comprehension with if else
print (new_list)
example = [[1,2,3], [1,2,3], [1,2,3]]
nested = [[i for i in range (1,4)] for j in range (3)]#make nested list in list comprehension
print (nested)
# dictionary comprehension
square = {f"square of {num} is ":num**2 for num in range (1,11)}
for k,v in square.items():
    print(f"{k} : {v}")
my_name = "mes shahadat"
word_count = {char:my_name.count(char) for char in my_name}
print (word_count)
odd_even = {i:('even' if i%2 == 0 else 'odd')for i in range (1,11)}
print (odd_even)
#set comprehansion
s = {k**2 for k in range (1,11)}
print (s)
names = {'mes', 'rahim', 'antor'}
tes = {name[0] for name in names}
print (tes)