'''
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,
all with different qualities and usage.

Lists are created using square brackets:

'''
# List values are ordered , changeable and allow to duplicates

mylist = ["C language","Java","C++"]
print(mylist)

#Lists Data Types
'A list can contain different data types'

list1 = ["abc", 12,True]
print(list1)

#list Constructor

newList = list(("Laptop","Phone","Book"))
print(newList)

#Accessing List elements by indexing as same as strings

#Check if item exists

if "Book" in newList:
    print("YES exist")

#---------Change list--------
'If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:'

"['Laptop', 'Phone', 'Book']"
newList[1]='Mouse'
print(newList)

#Insert Items
newList.insert(2,"Rakibul")
print(newList)

#append() method to append an items to the end of the list

newList.append("Islam")
print(newList)

#extend() method to append elements from another list to the current list
newList.extend(mylist)
print(newList)

'------------------------------------------------------------'
#Remove list

thisList = ["Books","Phones","WBTA","CSS","HTML","Laptops","Books"]
'remove() methods only remove first occurence'
thisList.remove("Books")
print(thisList)

#remove specified index
thisList.pop(1)
print(thisList)

'only pop() method remove the last element'
thisList.pop()
print(thisList)

#del keyword also removes the specified element and also 'del' keyword delete the entire list
delList = ["Rakibul","Islam","Mondal"]
del delList[2]
print(delList)

del delList
# print(delList) <Output will be 'delList' doesn't decleared

#Clear the list clear() methods clear the entire lists
thisList.clear()
print(thisList)


