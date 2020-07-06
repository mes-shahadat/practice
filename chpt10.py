def all_total(*args): # *arg convert any argument to (tuple) so you can put any number of argument
    total = 0
    for i in args:
        total += i
    return total
# print (all_total(1,2,3,4,5))
def multiply_num (*args):# you can also write def multiply_num (num1, *args), so the first argument will be used as a num and others will be converted to tuple
    tot_mul = 1
    for i in args:
        tot_mul *= i
    return (tot_mul)
print (multiply_num(2,4,8))
list_nums = [2,4,6,8]
print (multiply_num(*list_nums)) # using * before argument will unpack the (tuple or list) argument value so your function doesn't take the argument as list
nums = [1,2,3]
def mul_args_bynum (numb, *args):
    if args:
        return [i**numb for i in args]
    else:
        return "u didn't pass any argument"
print (mul_args_bynum(3, *nums))
def dic (name,**kwargs):# **kwargs convert any argument to dictionary
    for k,v in kwargs.items():
        print (f"{k} : {v}")
dic ('mes shahadat', first_name = 'mes', last_name = 'shahadat')
for_dic = {'name' : 'rahim', 'name1' : 'mes shahadat', 'age' : 17}
dic(**for_dic) # ** will unpack the dictionary cause writing only dictionary will give you error
#parameters order is (name, *args, default parameter, **kwargs)
def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('harshit', 1,2,3, a = 1, b = 2)
def first_char_upper (l, **kwargs):
    if kwargs.get ('reverse_str') == True:
        return [i[ : :-1].title() for i in l]
    else:
        return [i.title() for i in l]
my_list = ['mes', 'shahadat']
print (first_char_upper(my_list, reverse_str = True))
##lambda
add = lambda a,b : a+b
multiply = lambda a,b : a*b
print (add(12,34))
print (multiply(5,6))