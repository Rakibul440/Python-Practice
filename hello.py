# set variables and Casting
#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)   # x will be '3'
y = int(5)   # y will be 5
z = float(3) # z will be 3.0

print(x,type(x))
print(y,type(y))
print(z,type(z))

# Many Values to Multiple Variables

x,y,z = 'Rakibul','Islam','Mondal'
print(x,y,z)

# One Value to Multiple Variables

x = y = z = 'Rakibul'
print(x,y,z)

# Unpack a Collection
'''
If you have a collection of values in a list, tuple etc.
Python allows you to extract the values into variables. 
This is called unpacking.
'''
fruits = ['apple','banana','cherry']
x,y,z = fruits
print(x,y,z)

# Global Variables
'''
Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

'''
x = 'Rakibul'

def myFunction():
    x = 'Jack'
    print('My name is ',x) # here x is jack bcz ## now here x is a local variable
myFunction()

print('My name is ',x)

# The Global Keyword
'''
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
'''
def myName():
    global name
    name = 'Rakibul Islam Mondal'
    print('Your name is ',name)
myName();
print('The name variables is still : ',name)

# Also, use the global keyword if you want to change a global variable inside a function.

r = 'Clay Janson'
print('Our Character Name is : ',r)
def charName():
    global r
    r = 'Hanna'
charName()
print(" Now Character name is changed to : ",r)
