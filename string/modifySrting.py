# Upper Case

name = "Rakibul Islam Mondal"
print(name.upper())

# Lower Case

print(name.lower())

# Remove Whitespace
'''Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
'''
a = "    Hey Rakibul        "
print(a.strip())  # returns "Hey Rakibul"

# Replace Strings

sms = "Hello, World!"
print(sms.replace('H','J'))
print(sms.replace("World","Duniya"))

# Split String

'''he split() method splits the string into substrings if it finds instances of the separator:'''
print(sms.split(','))
firstPart = sms.split(',')[0]
print(firstPart)

