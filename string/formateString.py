# String Format
'''
As we learned in the Python Variables chapter, we cannot combine strings and numbers
But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

'''
age = 21
txt = "My name is Rakibul Islam Mondal, and I am {}"
print(txt.format(age))
#-------------
quantity = 3
itemNo = 2536
price = 48.32
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity,itemNo,price))
#-------------
'You can use index numbers {0} to be sure the arguments are placed in the correct placeholders'

myOrder = "I want {2} pieces of item {0} for {1} dollars."
print(myOrder.format(itemNo,price,quantity))

# F-string

print(f"I want {quantity} pieces of item {itemNo} for {price} dollars")

