x, y = 15, 45
if y > x:
    print("y is greater than x")

p, q = 10, 50
if q > p:
    print("q is greater than p")

num = int(input("Enter a number: "))
if num == 0:
    print("The number is neither even nor odd.")
elif num % 2 == 0:
    print("It's an even number.")
else:
    print("It's an odd number.")

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

if n1 > n2 and n1 > n3:
    print("n1 is the largest")
elif n2 > n3:
    print("n2 is the largest")
else:
    print("n3 is the largest")

m, n = 120, 80
print("n is greater than m" if n > m else "n is not greater than m")

age = int(input("Enter your age: "))
print("You are eligible to vote" if age >= 18 else "You are not eligible to vote")

value = 2
if value == 1:
    print("value is one")
elif value == 2:
    print("value is two")
elif value == 3:
    print("value is three")
else:
    print("value not found")

choice = int(input("Enter a number: "))
if choice in (30, 40, 50):
    print(f"You entered {choice}")
else:
    print("You entered some other number")

score = int(input("Enter your score: "))
if score > 85:
    print("Grade A")
elif score > 60:
    print("Grade B+")
elif score > 40:
    print("Grade B")
elif score > 30:
    print("Grade C")
else:
    print("Fail")

num_check = 35
if num_check > 10:
    print("Above ten")
    print("and also above 20" if num_check > 20 else "but not above 20")
