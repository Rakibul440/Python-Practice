# Slicing 
'You can return a range of characters by using the slice syntax.'
'Specify the start index and the end index, separated by a colon, to return a part of the string'

'''Get the characters from position 2 to position 5 (not included):'''

b = "Rakibul Islam Mondal"
print(b[2:5])

# slice from the start
print(b[:5]) 

# slice to end
print(b[2:])

# Negetive Indexing 
'''Use negative indexes to start the slice from the end of the string:'''
a = "Hello, World!"

'''Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
print(a[-5:-2])