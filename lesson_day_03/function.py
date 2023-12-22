type(32)
max('hello world')
max('Hello world')
min('hello world')
len('hello world')
int('32')
import math
decibels = 10 * math.log10(0.5)
print(decibels)
import random
x = random.random()
print(x)
num = x * 10
print(int(num))
import random 
def print_lyrics():
    print("i m a lumberjack.")
    print(' isleep well')
    
    
def print_twice(bruce):
    print(bruce)
    print(bruce)
    
    print_twice('Spam')
def add_two(a, b):
    added = a + b
    return added

x =add_two(3, 5)
print(x)

def f(x,y):
    add=x * x + y * y
    return add

x = f(5,6 )
print(x)

def g(x,y):
    return x*x - 2*x*y + y*y

x= f(5,6)
print(x)

def g (x, y):
    return x*x - 2*x*y + y*y

x= g(7,8)
print(x)

def t(x,y,z):
    return (x*x + 3*x*y*z + y*y) / z *z

x = t(5,6,7)
print(x)



def convert_temperature():
     grad = input("enter grad ")
     temperature = int(input('enter temperature '))
     if grad == "C":
         result = temperature * (9/5) + 32
         print(result)
     else:
         result = (temperature - 32) * 5/9
         print(result)
         
    
    
convert_temperature()
          
def find_age(age):
    if (age >= 1) and (age <= 12):
        print('you are a child')
    elif (age >= 13) and (age <= 19):
        print(' you are a tenneger')
    elif (age >= 20) and (age <= 59):
        print(' you are an adult')
    elif (age >= 60) and (age <=100):
        print(' you are a senior')
    else:
        print(' you are a dinosaur')
    

# num_one = int(input("Enter a number: "))  
# --> 23 "23" + "93" = 2390
# num_two = input("Enter another number")
# the_sum = num_one + num_two
# print(the_sum)

age = int(input("enter your age "))
find_age(age)
        
            