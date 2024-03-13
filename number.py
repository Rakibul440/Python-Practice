# Python Numbers
'''
three type of numeric types in python
1. int  ---> Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
2. float ---> Float, or "floating point number" is a number, positive or negative, containing one or more decimals
3.complex --->
'''

x = 1 #int
y = 2.8 #float
z = 1j #complex

print("x= ",type(x), "\ny= ",type(y),"\nz= ",type(z), "\n")

# Float
'''
Float can also be scientific numbers with an "e" to indicate the power of 10.
'''
f = 35e3
fa = 15E4
faa = -45.2e100

# Complex Number
c = 3 +5j
ca = 5j
caa = -5j

# Convert from one type to another:

p = 1
q = 3.14
r = 7j

# convert from int to float
u = float(p)
# convert from float to int
v = int(q)
# Convert from int to complex
w = complex(p)

print(u,v,w)

