# Build-in data types
'''
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text type : str
Numeric Types : int,float,complex
Sequence types : list,tuple,range
Maapping type : dist
Set types : set , frozenset
Boolen Types : bool
Binary : bytes,bytearray,memoryview
None type : NoneType

'''
# Setting the Data Type

a = 'Hello World'
print(a,type(a))

b = 7
print(b,type(b))

c = 3.14
print(c,type(c))

d = 1j
print(d,type(d))

e = ['Rakibul','Islam','Mondal']
print(e,type(e))

f = ('Rakibul', 'Islam','Mondal')
print(f,type(f))

g = range(7)
print(g,type(g))

h = {"name":"Rakibul","age":21}
print(h,type(h))

i = {"apple", "banana", "cherry"}
print(i,type(i))

j = frozenset({"apple", "banana", "cherry"})
print(j,type(j))

k = True 
print(k,type(k))

l = b"Hello"
print(l,type(l))

m = bytearray(5)
print(m,type(m))

n = memoryview(bytes(5))
print(n,type(n))

x = None
print(x,type(x))

# Setting the Specific Data Type

'https://www.w3schools.com/python/python_datatypes.asp'

