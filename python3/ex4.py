#!/usr/bin/env python
# --* coding: utf-8 -*-

print(not True)
print(-5 != False !=True)
print(1 < 2 < 3)
print(2 < 3 < 2)
a = [1,2,3,4]
b = a
print( b is a)
print(b ==a)
print("hello" + ", world!")
print("This is a string"[0])
a = "a string"
print(len(a))
print("{} can be {}".format("strings","interpolated"))
print("{0} be nimble,{0} be quik,{0}, jump over the {1}".format("Jack","candle stick"))
print("{name} wants to eat {food}".format(name="Bob",food="lasagna"))
name="Reiko"
print(f"She said her name is {name}")
print("%s can be %s the %s way" % ("String", "interpolated","old"))
print("etc" is None)
print(None is None)
print(bool(0) == bool("") == bool([]) == bool({}) == bool(()) == False)
print("I'm pthon.Nice to meet you!")
print("hello,world",end="!")   #not next line.
#input_string_var = input("Enter some data:")
#print(input_string_var)
some_var = 5
print(some_var)
#print(some_unknow_var)#Raise a NameError.
##(print("yahoo" if 3 > 2 else 2)


li = []
other_li = [4,5,6]
li.append(3)
print(li)
#Remove the end with pop.
other_li.pop()
print(other_li)
print(li[0],li[-1])
l=[1,2,3,4,5,6,7,8]
print(l[::2])
print(l[::-1])
li2 = l[:]
print(li2)
print(li2 is l)
del l[2]
print(l)
l.remove(2)
print(l)
l.insert(1,2)
print(l)
print(l.index(6))
print(l + li)
l.extend(li)
print(l)
print(2 in l)
print(len(l))

tup =(1,2,3)
print(tup[0],tup[2])
print(type((1)),type((1,)),type(()))
print(len(tup))
print(tup + (4,5,6))
print(tup[:2])
print(6 in tup)
a, b, c = (1,2,3)
d, *e, f = (4, 5, 6, 7)
print(a,b,c,d,e,f)

#dict
empty_dict = {}
filled_dict = {"one" : 1,"two" : 2, "teree":3}
#invalid_dict = {[1,2,3] : "123"}
valid_dict = {(1,2,3) : [1,2,3] }
print(filled_dict["one"])
print(list(filled_dict.keys()),list(filled_dict.values()))
print("one" in filled_dict, 1 in filled_dict)
#print(filled_dict["four"])   #KeyError
print(filled_dict["one"],filled_dict.get("four"),filled_dict.get("one",4),filled_dict.get("four",4))
print(filled_dict.setdefault("five",5),filled_dict.setdefault("five",6),filled_dict.get("five"))
filled_dict.update({"four":10})
print(filled_dict["four"])
print({'a':1,**{'b':2}},{'a':1,**{'a':2}})

#set
empty_set = set()
some_set = {1,2,3,4,5,6,1,2,3,4}
#invalid_set = {[1],1}
valid_set = {(1,),1}
filled_set = some_set
filled_set.add(5)
other_set = {3,4,5}
print(some_set,other_set,filled_set,filled_set & other_set,filled_set | other_set)
print({1,2,3,4} - {2,3,5}, {1,2,3,4}^{2,3,5}, {1,2} >= {1,2,3},{1,2}<={1,2,3},2 in filled_set,10 in filled_set)

#Contral Flow and Iterables
some_var = 5
if some_var > 10:
    print("some_var is totally bigger than 10")       
elif some_var <10 :
    print("some_var is smaller than 10")
else :
    print("some_var is indeed 10.")

for animal in ["dog","cat","mouse"]:
    print("{} is a mammal".format(animal))

for i in range(4):
    print(i)

for r in range(4,8):
    print(r,end=",")

print()    
for i in range(4,20,3):
    print(i)
x = 0
while x < 4:
    print(x)
    x +=1

try:
    raise IndexError("This is am index error.")
except IndexError as e:
    pass
except (TypeError, NameError):
    pass
else :
    print("all good")
finally:
    print("We can clean up resources here.")

filled_dict = {"one":1,"two":2,"three":3}
our_iterable = filled_dict.keys()
print(our_iterable)
for i in our_iterable:
    print(i)
#print(our_iterator[0])
our_iterator = iter(our_iterable)
for i in range(3):
#for i in range(4):
    print(next(our_iterator))

print(list(filled_dict))

# functions
def add(x, y):
    print("x is {} and y is {}.".format(x,y))
    return x+y
add(3 ,5)
add(y = 3,x = 9)

def varargs(*args):
    return args
print(varargs(1,2,3,4))

def keyword_args(**kwargs):
    return kwargs
print(keyword_args(bid="foot",loch="ness"))

def all_the_args(*args,**kwargs):
    print(args,kwargs)
#    print(kwargs)
all_the_args(1,2,a=3,b=4)

args = (1,2,3,4)
kwargs = {"a":3,"b":4}
print("#")
all_the_args(*args)
all_the_args(**kwargs)
all_the_args(*args,**kwargs)

def swap(x,y):
    return y,x
x=1
y=2
x,y= swap(x,y)
print(x,y)

x=5
def set_x(num):
    x = num
    print(x)
set_x(42)

def set_global_x(num):
    global x
    print(x)
    x = num
    print(x)
set_x(43)
set_global_x(7)

def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_10 = create_adder(10)
print(add_10(3))
print(create_adder(2)(15))

print((lambda x:x > 2)(3))
print((lambda x,y:x ** 2 + y ** 2)(2,1))

list(map(add_10,[1,2,3]))
list(map(max,[1,2,3],[4,2,1]))

list(filter(lambda x:x>5,[3,4,5,6,7,8]))

[add_10(i) for i in [1,2,3]]
[x for x in [3,4,5,6,7,8] if x >5]

{x for x in 'abcdef' if x not in 'abc'}
{x:x**2 for x in range(7)}

# Modules
import math
print(math.sqrt(6400))

from math import ceil,floor
print(ceil(3.7),floor(3.7))

from math import *

import math as m
math.sqrt(16) == m.sqrt(16)

import math
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.

# classes

class Human:
    species = "H.sapiens"
    def __init__(self,name):
         self.name = name
         self._age = 0
    def say(self,msg):
        print("{0}:{1}".format(self.name,msg))
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'
    @classmethod
    def get_species(cls):
        return cls.species
    @staticmethod
    def grunt():
        return "*grunt*"
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age
    @age.deleter
    def age(self):
        del self._age

# if __name__ == '__main__':
#     i = Human(name = "Ian")
#     i.say('hi')
#     j = Human('joel')
#     j.say('hello')
#     i.say(i.get_species())
#     Human.species = "H.neanderthalensis"
#     i.say(i.get_species())
#     j.say(i.get_species())
#     print(Human.grunt())
#     print(i.grunt()) ## ???
#     i.age = 42
#     i.say(i.age)
#     j.say(j.age)
#     del i.age

# Inheritance
# To import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

#from human import Human

class Superhero(Human):
    species = "Superhuman"
    def __init__(self,name,movie=False,
                 superpowers=["super strength","bulletproofing"]):
        self.fictional = True
        self.movie=movie
        self.superpowers = superpowers
        super().__init__(name)
    def sing(self):
        return 'Dun ,dun.DUN!'
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow = power))

# if __name__ == '__main__':
#     sup = Superhero(name = "Liei")
#     if isinstance(sup,Human):
#         print("I am human")
#     if type(sup) is Superhero:
#         print("I am a superpowers")
#     print(Superhero.__mro__)
#     print(sup.get_species())
#     print(sup.sing())
#     sup.say("Spoon")
#     sup.boast()
#     sup.age = 31
#     print(sup.age)
#     print('Am i Oscar eligible?' + str(sup.movie))

# Multiple Inheritance.

class Bat:
    species = 'Byte'
    def __init__(self,can_fly= True):
        self.fly = can_fly
    def say(self,msg):
        msg = '... ... ...'
        return msg
    def sonar(self):
        return '))) ... ((('

    # if __name__ == '__main__':
#     b = Bat()
#     print(b.say('hello'))
#     print(b.fly)

#class Batman(Superhero, Bat):
class Batman(Bat,Superhero):
    def __init__(self,*args,**kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)      
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass arguments,
        # with each parent "peeling a layer of the onion".
        Superhero.__init__(self,'anonymous',movie = True, superpowers = ['Wealthy'],*args,**kwargs)
        Bat.__init__(self,*args,can_fly = False,**kwargs)
        self.name = "Sad Affleck"
    def sing(self):
        return 'nan nan nan ... batman!'

    # if __name__ == '__main__':
#     bat = Batman()
#     print(Batman.__mro__)
#     print(bat.get_species())
#     print(bat.sing())
#     print(bat.say(' s'))
# #    bat.say('I agree')
#     print(bat.sonar())
#     bat.age = 100
#     print(bat.age)
#     print('Can I fly?' + str(bat.fly))
       
# Advanced

# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges.
# NOTE: `range` replaces `xrange` in Python 3.
for i in double_numbers(range(1,10000)):
    print(i)
    if i > 30:
        break
    
# Just as you can create a list comprehension, you can create generator
# comprehensions as well.
values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x)
print(values)
values = (x**2 for x in [1,2,3,4,5,6,7,8])
gen_to_list = list(values)
print(gen_to_list)
        
values = [ x for x in range(1,20)]
print(values)

# Decorators
# In this example `beg` wraps `say`. If say_please is True then it
# will change the returned message.
from functools import wraps
def beg(target_function):
    @wraps(target_function)
    def wrapper(*args,**kwargs):
        msg,say_please = target_function(*args,**kwargs)
        if say_please:
            return "{} {}".format(msg,"Please! I am poor:(")
        return msg
    return wrapper

@beg
def say(say_please = False):
    msg = "Can you buy me a beer?"
    return msg,say_please

print(say())
print(say(say_please= True))
value = list((-x for x in range(2,7)))
for i in value:
    print(i)
for x in (-y for y in range(8,15)):
    print(x)
#print([range(1,2)])
type(range(1,2))
#for key in {'hu':1,'ui':5}.keys:
#    print(key+':')
