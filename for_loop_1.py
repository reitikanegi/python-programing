for i in range(1,11):
    print(i)

# print even number from 1-20
for i in range(0,20,2):
    print(i)

# print odd numnbwe from 1-20
for i in range(1,20,2):
    print(i)

a = int(input("Enter the number: "))
for i in range(1,11):
    print(a ,"X", i, "=", a*i)

# sum of all number from 1-100
sum = 0
for i in range(1,101):
 sum = sum+i
print("sum =",sum)

# factorial of a givrn number
num = int(input("enter the number; "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("fact = ", fact)

# count how many number are printed from 1-50
count = 0
for i in range(1,50):
    print(i)
    count = count+1
print("total number; ",count)

# print is character of a string usig a Loop
a = input("string: ")
for i in a:
    print(i)

# count number of vowels in a String
name = input("enter a string:")
count = 0
for i in name:
    if i in "aeiouAEIOU":
        count = count+1
print ("number of count: ", count)

# count the number of lower case and upper case letters in  a string
text = input("Enter a string: ")
upper = 0
lower = 0
for ch in text:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
print("upper letters = ",upper)
print("lower letters = ",lower)

# reverse a string using for loop
text = input("enter the string: ")
reverse = "" 
for i in text:
    reverse = i + reverse
print("reverse string = ", reverse)

# find the largest number in a list
number = [1,5,7,9,6]
largest = number[0]
for i in number:
    if i>largest:
        largest = i
print("largest number = ",largest)

# find the smallest number from the list
number = [67,78,40,45,20]
smallest = number[0]
for i in number:
    if i<smallest:
        smallest = i
print("smaleest number: ",smallest)

# calculate the sum of all elements in the list
number = [67,78,40,45,20]
sum = 0
for i in number:
    sum = sum + i
print("sum of all elements:",sum)

# print all element of a list in reverse order
text = ["apple","mango","grapes","litchi"]
reverse = []
for i in text:
    reverse = [i] + reverse
print("reverse = ",reverse) 

# reverse each string of a list 
text = ["apple","mango","grapes","litchi"]
for word in text:
    reverse = "" 
    for i in word:
        reverse = i + reverse
    print(reverse)