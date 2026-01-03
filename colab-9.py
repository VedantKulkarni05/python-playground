# . Sum of list elements
values = [10, 30, 23, 43, 65, 12]
total = 0
for val in values:
    total += val
print("Total sum:", total)


# . Multiplication table
number = int(input("Enter a number: "))
for idx in range(1, 11):
    result = number * idx
    print(number, "x", idx, "=", result)


# . For loop inside for loop
colors = ["red", "big", "tasty"]
items = ["apple", "banana", "cherry"]

for c in colors:
    for it in items:
        print(c, it)


# . Nested loop with range
for row in range(4):
    for col in range(20, 24):
        print(row, col)


# . Star pattern
lines = int(input("Enter rows: "))
for r in range(0, lines + 1):
    for s in range(r):
        print("*", end="")
    print()


# . Number pyramid
levels = int(input("Enter rows: "))
for r in range(0, levels + 1):
    for n in range(r):
        print(r, end="")
    print()


# . Finding length without len()
data = [11, 23, 30, 43]
length = 0
for element in data:
    length += 1
print("Length:", length)


# . Find index of an element
nums_list = [11, 23, 30, 43]
pos = 0
for element in nums_list:
    pos += 1
    if element == 30:
        break
print("Found at position:", pos)


# . Find a letter using break
chars = ['a', 'b', 'c', 'd', 'e']
for ch in chars:
    if ch == 'c':
        print("Found letter")
        break
    else:
        print(ch)
