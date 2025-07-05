#String data type 

# literal assignment 
first = "Johnny"
last = "Sky"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a strings
decade = str(1980)
print(type(decade))
print(decade)

statement = "i like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

i was just checking in.
                                All good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\they!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                    "
multiline = "                          " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))