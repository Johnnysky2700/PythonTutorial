users = ['Johnny','Sky','John']

data = ['Johnny','42','True']

emptylist = []

print("Johnny" in emptylist)

print(users[0])
print(users[-2])

print(users.index('John'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

# Appending items to a list
users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'jimmmy'])
print(users)

# users.extend(data)
# print(users)

# Inserting values at a specific list index
users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

# Replacing list values
users[1:3] = ['Robert', 'JPJ']
print(users)

# Removing, deleting, clearing
users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data 
data.clear()
print(data)

# Sorting lists
users[1:2] = ['johnny']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

# Copying lists
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# List constructor and data type
print(type(nums))

mylist = list([1,"Neil", True])
print(mylist)

# Tuples vs Lists
mytuple = tuple(('Johnny', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# If you need to change a tuple
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# Unpacking tuples
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

# Using dot notation to find methods
print(anothertuple.count(2))