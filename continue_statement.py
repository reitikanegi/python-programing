for i in range(1,21):
    if i%3 == 0:
        continue
    print(i)

# print only odd numbers from 1-50
for i in range(1,51):
    if i%2==0:
        continue
    print(i)

# print all vowels in a string , skkiping consonents 
text = input("enter the string : ")
index = 0 
while len(text)>index:
    if text[index] not in "aeiouAEIOU":
        index = index + 1
        continue
    print(text[index],end=" ")
    index = index + 1
            #  OR
text = input('enter the string: ')
index = 0
while len(text)>index:
    if text[index] in "aeiouAEIOU":
        print(text[index],end=" ")
    index = index + 1    

# print numder from 1 to 100 , skipping numbes divisible by both 2 and 5
for i in range(1,101):
    if i%2 == 0 and i%5 == 0:
        continue
    print(i)
            #    OR
num = 1
while num <= 100:
    if num % 2 == 0 and num % 5 == 0:
        num = num + 1
        continue
    print(num) 
    num = num + 1

# read 10 numbers from the user and print only positive numbers
count = 1
for i in range(1,11):
    if count<=10:
        num = int(input("enter a number: "))
        if num <= 0:
            count = count + 1
            continue
        print(num)
        count = count + 1

# print all character in a string except space
text = input("enter the string: ")
for i in text:
    if i == " ":
        continue
    print(i)

# print all the numbers from 1 to 30 , skipping prime numbers
for n in range(1,31):
    if n <= 1:
        prime = False
    else:
        prime = True
        for i in range(2,n):
            if n%i==0:
                prime = False
                break
    if prime:
        continue
    print(n)

# display all the students marks except those who are absent (represented by -1)
student = 10
count = 0
while count<student:
    n = int(input("enter the marks of a student: "))
    if n == -1:
        count = count + 1
        continue
    print(n)
    count = count + 1
    





    


