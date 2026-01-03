# Tuple definition
courses = ('ba', 'bcom', 'bsc')
print(courses, type(courses))

# Access elements
print(courses[1], courses[3-1])
print(courses[3:5], courses[-3:])

# Functions: count() and index()
courses = ('ba','bcom','bsc','bsc','ba')
print(courses.count('bsc'), courses.index('bsc'))

# Iterating tuples
for item in courses:
    print(item)
for idx, item in enumerate(courses):
    print(idx, item)

# Length
print(len(courses))

# Mixed data types
data = ('ba', 2, True, 'bsc')
for item in data:
    print(item, type(item))

# Single-element tuple
single1 = ('50')   # string
single2 = ('50',)  # tuple
print(type(single1), type(single2))

# Combining tuples
print(('a','b') + (1,2))
print(('50',) + ('apple',) + ('mango','orange'))

# Membership check
fruits = ('apple','mango')
print('mango' in fruits, 'mangoes' in fruits)

# Max, Min
print(max(2,1,3,7), min(2,1,3,7))

# List → Tuple
num_list = [1,2,3,4]
num_tuple = tuple(num_list)
print(num_list, num_tuple)

# Negative indexing
num = (1,2,3,4,5,6,7)
print(num[-1], num[-2])
print(num[6])

# Tuple slicing
courses = ('ba','bcom','bsc','be','ma','mcom','msc','me')
print(courses[3:5], courses[3:], courses[:3], courses[-3:])
