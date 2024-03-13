# Python Strings

# Multiline Strings

para = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(para)

# Strings and Arrays
'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.

# remember that the first character has the position 0
'''
str = "Hey, Rakibul"
print("position 1 character is : ",str[1],"\n")

# Looping Through a String
'''Since strings are arrays, we can loop through the characters in a string, with a for loop.
'''
for x in "banana" :
    print(x)

# String Length
'''To get the length of a string, use the len() function.
'''
print("\n",len(str),"\n")

# Check String
'To check if a certain phrase or character is present in a string, we can use the keyword "in"'

text = "The best things in life are free!"
print("free" in text); # it'll say true or false

if "free" in text :
    print("yes, 'free' is present")

# Check if NOT
'To check if a certain phrase or character is NOT present in a string, we can use the keyword "not in"'

print("rakibul" not in text)
if "rakibul" not in text :
    print("No 'rakibul' in NOT present")
    