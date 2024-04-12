'Loop through a list'
list = ["react","next","HTML"]

'print all elements one by one'
for x in list:
    print(x)

print("\n-----------------\n")

'print all elements by index number'
for i in range(len(list)):
    print(list[i])

print("\n-----------------\n")

#Looping Using List Comprehension
[print(x) for x in list]