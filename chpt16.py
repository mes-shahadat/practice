## name error means you are printing something that is not defind means it doesn't exits. for example you didn't created any variable or function with a name but you are trying to print it, it means you have name error.
## type error means you are doing wrong operation with wrong type
print (5 * 'mes shahadat')
## value error means you have type wrong value, like for int operation you have typed str value. so it will show value error
def add(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    raise TypeError ('oops some idiot is inputing wrong input')
print (add(1,2))
class Animal:
    def __init__(self,name):
        self.name = name

    def animal_sound(self):
        raise NotImplementedError ('you have to implement sound for every subclass'
)
class Dog(Animal):
    def __init__(self,name,breed):
        self.breed = breed
        super().__init__(name)

    def animal_sound(self):
        return "bow bow"

class Cat(Dog):
    def __init__(self,name,breed):
        super().__init__(name,breed)

    def animal_sound(self):
        return "meaow meaow"

pet1 = Dog('bujo','pugo')
pet2 = Cat('doraemon', 'robot')
print (pet1.name)
print (pet1.animal_sound())
print (pet2.name)
print (pet2.animal_sound())

class Mobile:
    def __init__(self,name):
        self.name = name
    
class Mobile_store:
    def __init__(self):
        self.other_mobiles = []

    def add_mobile(self,new_mobiles):
        if isinstance(new_mobiles,Mobile):
            self.other_mobiles.append(new_mobiles)
        else:
            raise TypeError ("added mobile should be from Mobile class")

oneplus = Mobile('oneplus 6 pro')
samsung = 'samsung a30'
mobstore = Mobile_store ()
mobstore.add_mobile(oneplus)
mobphones = mobstore.other_mobiles
print (oneplus.name)
print (mobphones[0].name)

# exception/error handling with try except
while True:
    try:
        age = int(input('plz input your age '))
        break
    except ValueError:
        print ("only numbers are allowed, plz try again")
    except:
        print ("unexpected error !!!")

if age < 18:
    print ("you can't play this game")
else:
    print ("you can play this game")
# exception/error handling with try, except, else, finally
while True:
    try:
        ages = int(input("plz input your age "))
    except ValueError:
        print ("not excepted, try again !!!")
    except:
        print ("unexpected error!! report to developers")
    else:
        print (f"your age is {ages}")
        break
    finally:
        print ("remember input only in numbers ")

#excersize1
def devide(a,b):
    try:
        return (a/b)
    except ZeroDivisionError as err: # as err shows error without any devprint
        print (err)
    except TypeError:
        print ("plz input only int numbers ")
    except:
        print ("unexpected error!!!. plz report bug to developer")
    
print (devide(10,0))

class name_is_too_short_error(ValueError):# maked my own sub class error by classing it from real error like value error
    pass

def validate(name):
    if len(name)<9:
        raise name_is_too_short_error('name is too short')

username = 'mes shahadat'
print (validate(username))