## generators
def lis(n):
    for i in range(1,n+1):
        yield (i)
numbers = lis(10) # generator can give sequence only once if you save generator in an variables
for i in numbers: 
    print (i)
for i in numbers:
    print (i)
def only_even_generator(n):
    for i in range(1,n+1):
        if i%2 == 0:
            yield (i)
for i in only_even_generator(20): # print generator many time without adding it to variable
#     print (i)
    list_square = [i**2 for i in range(1,11)] #[] is used for list comprehension
print (list_square)
generator_square = (i**2 for i in range (1,11)) #() is used for generator comprehension
for num in generator_square:
    print (num)

# object oriented programming
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return (f"{self.first_name} {self.last_name}")
    def above_18(self):
        return self.age>18
p1 = Person('mes','shahadat',17) # this is called object or instances
p2 = Person('mohammad', 'yasin',17)
print (p2.first_name)
print (p1.last_name)
print (p2.above_18())
class Circle:
    pi = 3.14 #this is called class variable
    def __init__ (self,radius):
        self.radius = radius
    def calc_radius(self):
        return 2*Circle.pi*self.radius
c = Circle(4)
c1 = Circle(5)
print (c.calc_radius())

class Laptop:
    discount_percent = 90 # this is called class variable or class attribute
    def __init__(self,laptop_name, laptop_model, laptop_price):
        self.laptop_name = laptop_name
        self.laptop_model = laptop_model
        self.laptop_price = laptop_price
        self.laptop_brand = laptop_name + ' ' + laptop_model
    def apply_discount(self):
        discount = (Laptop.discount_percent/100)*self.laptop_price
        return self.laptop_price - discount
Laptop.discount_percent = 53
laptop1 = Laptop('del','v55',15000)
laptop2 = Laptop('hp','e61',20000)
print (laptop1.laptop_name)
print (laptop2.laptop_name)
print (laptop1.laptop_brand)
print (laptop2.apply_discount())
print (laptop1.__dict__) # to see what this variable has

class Laptops:
    discount_percent = 30 # class variable
    def __init__(self,laptop_name, laptop_model, laptop_price):
        self.laptop_name = laptop_name
        self.laptop_model = laptop_model
        self.laptop_price = laptop_price
        self.laptop_brand = laptop_name + ' ' + laptop_model
    def apply_discount(self):
        discount = (self.discount_percent/100)*self.laptop_price
        return self.laptop_price - discount
laptop1 = Laptops('advent','k4000',25000)
laptop2 = Laptops('mi','420',20000)
laptop2.discount_percent = 50 # objects own variable # when apply_discount is self, the function first check for if it's has it's own variable or else it uses the class variable
print (laptop1.apply_discount())
print (laptop2.apply_discount())

class Student:
    count_instance = 0 # this is called class variable
    def __init__(self, first_name, last_name, age):# this is called instance method
        Student.count_instance += 1
        self.first_name = first_name # this are called instance or object variable
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name
    @classmethod
    def count_instances(cls): # this is class method
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"
    @classmethod
    def from_string(cls,string):#only good for string like age but not for price like int which you can't change
        first_name,last_name,age = string.split(",")
        return cls(first_name,last_name,age)
    @staticmethod
    def hello():# this is called static method
        print ('hello, you called static method')

student1 = Student('mohammad','zihad', 19)# this is called object or instances 
student2 = Student('abdur', 'rahim', 18)
student3 = Student('antor', 'das', 17)
student4 = Student.from_string("mes,shahadat,17")
print (student1.full_name )
print (student2.full_name )
print (Student.count_instances())
print (student4.full_name)
Student.hello()

class Phone:
    def __init__(self, phone_brand, phone_model, phone_price):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self._phone_price = max(phone_price,0)#use max function so this variable so the price can't be print in -value
        # self.phone_specification = f"your phones {self.phone_brand} {self.phone_model} and price is {self._phone_price}tk"#this is wrong method beacause the price is not being update

    @property# this is used so we don't have call this like function (), it will be called as a attribute
    def full_specification(self):
        return f"your phones {self.phone_brand} {self.phone_model} and price is {self._phone_price} tk"

    @property #error code doesn't even work
    def phone_price(self):
        return self._phone_price

    @phone_price.setter
    def phone_price(self, new_price):
        self._phone_price = max(new_price, 0)

    def full_name(self):
        return f"{self.phone_brand} {self.phone_model}"

    def make_call(self,phone_number):
        return f'calling {phone_number}...'

phone1 = Phone('nokia', 'e61', 1500)
phone2 = Phone('sympony', 'v55',5000)
phone1._phone_price = -4430
print (phone2.full_name())
print (phone1.full_specification)
print (f'phone1 price = {phone1.phone_price}')
print (f'phone2 price ={phone2.phone_price}')
print (phone2.full_specification)


class Old_phone:# base class/parent class
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = max (price,0)
        self.full_name = f"{self.brand} {self.model}"

    def full_specification(self):
        return f"your {self.brand} {self.model} is {self.price}tk"

phone1 = Old_phone("nokia","e61",2500)
print (phone1.full_specification())

class Smartphone(Old_phone):#derive/child class
    def __init__(self,brand,model,price,camera,ram,internal_storage):
        # Old_phone.__init__(self,brand,model,price)# uncommon way
        super().__init__(brand,model,price)#inheritence 
        self.camera = camera
        self.ram = ram 
        self.internal_storage = internal_storage
    def __add__ (self,other): # operator overloading # u can use it for multiply or others
        return self.price + other.price
    def full_details(self):
        return f"{self.brand} {self.model}, {self.camera} camera, {self.ram} ram, {self.internal_storage} internal storage, {self.price}tk only."
Smartphone1 = Smartphone('oneplus', '6', 35000, '16 MP', '8 GB', '256 GB')
Smartphone2 = Smartphone('xiaomi','note 9 pro',25000,'64 MP','8 GB','256 GB')
print (Smartphone1.full_specification())
print (Smartphone1.full_details())
print (Smartphone1+Smartphone2)

class Flagshipphone(Smartphone):#i used multilevel inheritence to this derive
    def __init__(self,brand,model,price,camera,ram,internal_storage,processor):
        super().__init__(brand,model,price,camera,ram,internal_storage)
        self.processor = processor
    def full_details(self):# this is called method overriding
        return f"{self.brand} {self.model}, {self.camera} camera, {self.ram} ram, {self.processor} processor, {self.internal_storage} internal storage, {self.price}tk only."
Smartphone = Flagshipphone('oneplus','7 pro', 75000, '64 Mp', '12 GB', '512 GB', 'snapdragon 875')
print (Smartphone.full_details())
print (Smartphone2.full_details())
#see video number 201 of harshit vashisht python playlist to know more about complex multiple inheritence
print (help(Flagshipphone)) # to check your classes method resolution order
print (Flagshipphone.mro())# to check mro
print (Flagshipphone.__mro__)# to check mro