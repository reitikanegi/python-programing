# print the number from 1 to 20,but stop when the numbers is 12
for i in range(1,21):
    if i == 12:
        break
    print(i)

n = int(input("enter the number: "))
while True:
    if n == 0:
        break
    print(n)
    n = int(input("enter the number: "))

list1 = [ 1, 2, 4, 7, 3]
search = int(input("enter the number you want to search: "))
for i in list1:
    if i == search:
        print("found.")
        break
else:
    print("not found.")

# print the multiplication table of a number but stop after the 5th iteration 
n = int(input("enter the number: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    if i == 5:
        break

# create a password cheacker that keep asking for the password until the correct one is entered
correct_password = "reitika_03"
password = input("Enter the password : ")
while password != correct_password:
    print("incorrect password! try again...  ")
    password = input("Enter the password : ")
else:
    print("correct password!!")

# find te first vowel in a string and stop checking after finding it
text = input("enter the string: ")
count = 0
for i in text:
    if i in "AEIOUaeiou":
        print("vowel found:", i)
        count = count + 1
        if count == 1:
            break

# print the numebr from 2 - 100 , but stop checking after finding it
num = 2
count = 0
while num <= 100:
    i = 2
    is_prime = True
    while i < num:
        if num %  i == 0:
            is_prime = False
            break
        i = i + 1
    if is_prime:
        print(num)
        count   = count + 1
        if count == 10:
            break
    num += 1

# create a menu_driven calculator that exist when the user chooses the exit option
while True:
    print("-----Menu-----")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice = int(input("enter the choice number : "))
    if choice == 5:
        print("calculator closed!")
        break
    num_1 = float(input("enter the first number: "))
    num_2 = float(input("enter the second number: "))
    if choice == 1:
        print('result:', num_1+num_2)
    elif choice == 2:
        print("result:",num_1-num_2)
    elif choice == 3:
        print("result:",num_1*num_2)
    elif choice == 4:
        if num_2!=0:
            print("result:",num_1/num_2)
        else:
            print("error! division byy zero is not possible.")
    else:
        print("Invalid choice! Please try again")






