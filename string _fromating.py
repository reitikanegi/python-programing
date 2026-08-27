# Print "My name is Rahul and I am 20 years old" using an f-string.
name = "ritika"
age = 20
print(f"My name is {name} amd I am {age} old.")

#  Take name and age as input and print:
# My name is ___ and I am ___ years old.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} year old. ")

# Take two numbers and print:
# The sum of 10 and 20 is 30.
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = num1 + num2
print(f"the sum of {num1} and {num2} is {sum}.")

# Use .format() to print a person's name, age, and city.
name = "ritika"
age = 20
city = "khatima"
print("my name is {}. I am {} year old and I live in {}.".format(name, age, city))

#  Print a number with exactly 2 decimal places
num = 23.09877990
print(f"number upto only 2 decimal places is {num:.2f}")

# Print a number as a percentage using string formatting.
num = 0.75
print(f"{num:.0%}")

# Print "Python" inside a field of width 20
word = "python"
print(f"{word:20}")

# Print a number right-aligned in a field of width 10
# Use >:(right)
num = 123
print(f"{num:>10}")

# print a number left-aligned in a field of width 10
# Use <:  (left)
num = 123
print(f"{num:<10}")

# Print a number centered in a field of width 10
# Use ^:
num = 123
print(f"{num:^10}")

# Print:
# Reitika scored 87.46 marks.
name = "Reitika"
marks = 87.4567
print(f"score of {name} is {marks:.2f}")

# Print a number with commas
num = 1000000
print(f"{num:,}")

# Print decimal, binary, octal and hexadecimal
num = 25
print(f'Decimal:{num}')
print(f'Binary: {num:b}')
print(f'Octal: {num:o}')
print(f'hexadecimal: {num:x}')

# Create an aligned table
print(f"{'Name':<10}{'Age':<10}{'Marks':<10}")
print(f"{'Ritika':<10}{20:<10}{85.50:<10.2f}")
print(f"{'Poonam':<10}{21:<10}{91.25:<10.2f}")

# Area of a circle up to 2 decimal places
r = 5
pi = 3.14159
area = pi * r * r
print(f"area of circle = {area:.2f}")

# Create a bill
print("======== BILL ========")
print(f"{'Item':<10}{'Price':<10}{'Qty':<10}")

item1 = "Pen"
price1 = 20
qty1 = 4

item2 = "Bag"
price2 = 900
qty2 = 1

item3 = "Book"
price3 = 100
qty3 = 2

print(f"{item1:<10}{price1:<10}{qty1:<10}")
print(f"{item2:<10}{price2:<10}{qty2:<10}")
print(f"{item3:<10}{price3:<10}{qty3:<10}")

total = price1*qty1 + price2*qty2 + price3*qty3

print("=======================")
print(f"Total: ₹{total}")

# Take user input and display an aligned table
name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
city = input("Enter city: ")
print(F"{'Name':<15}{'Age':<15}{'Salary':<15}{'City':<15}")
print(f"{name:<15}{age:<15}{salary:<15}{city:<15}")

# Calculate discounted price
price = 4999
discount = 15
discount_amount = price * discount / 100
final_price = price - discount_amount
print(f"Original Price: ₹{price:.2f}")
print(f"Discount: {discount}%")
print(f"Final Price: ₹{final_price:.2f}")

# Student report card
name = "Reitika"
roll_no = 101
maths = 85
python = 92
dbms = 88
ai = 90
os = 82
total = maths + python + dbms + ai + os
percentage = total / 5
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"
print("========== REPORT CARD ==========")
print(f"Name       : {name}")
print(f"Roll No.   : {roll_no}")
print("---------------------------------")
print(f"Maths      : {maths}")
print(f"Python     : {python}")
print(f"DBMS       : {dbms}")
print(f"AI         : {ai}")
print(f"OS         : {os}")
print("---------------------------------")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")

# Countdown with width 3
for i in range(10,0,-1):
    print(f"{i:3}")
    