n = int(input("enter the number: "))
largest = 0
while n>0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10
print("greatest digit in a number = ", largest)

# find the smallest digit in a number
num = int(input("enter the number:"))
smallest = 9
while num>0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10
print("smallest digit in a number is : ",smallest)

# find the GCD(HCF) of two number using  a while loop
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
while b != 0: 
    remainder = a % b
    a = b
    b = remainder
print("gcd: ",a)

# find the lcm of two number
num_1 = int(input("enter the first number: "))
num_2 = int(input("enter the second number: "))
a = num_1
b = num_2  
while b != 0:
    remainder = a % b
    a = b
    b = remainder
gcd = a
lcm = (num_1*num_2)//gcd
print("lcm is : ",lcm)

n = int(input("enter the nunmber: "))
a = 0
b = 1
count = 0
while count<n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count = count + 1

n = int(input("enter the number: "))
while n >= 1:
    print(n, end=" ")
    n = n - 1

# print the following pattern
row = int(input("enter the number of rows: "))
i = 1
while i <= row:
    j = 1
    while j<= i:
        print("*", end=" ")
        j+= 1
    print()
    i += 1

row = int(input("enter the number of rows: "))
i = row
while i >= 1:
    j = 1
    while j<= i:
        print(j, end=" ")
        j+= 1
    print()
    i -= 1

row = int(input("enter the number of rows: "))
i = 1
while i <= row:
    j = 1
    while j<= i:
        print(j, end=" ")
        j+= 1
    print()
    i += 1

n = 10
i = 1
while n >= i:
    square = i ** 2
    print("square of",i,"is", square)
    i = i + 1    

n = 10
i = 1
while n >= i:
    square = i ** 3
    print("square of",i,"is", square)
    i = i + 1    

# keep asking the user for a number until they enter zero
n = int(input(" enter the input: "))
while n != 0:
    print("you enter: ", n)
    n = int(input(" enter the input: "))
print('the loop ended because you entered zero')

correct_password = "reitikanegi03"
password = input("enter the password: ")
while password != correct_password:
    print("incorrect password. try again")
    password = input("enter the password: ")
print("login successfully! ")

balance = 50000
while True:
    print("ATM menu.")
    print("1.Deposit\n2.Withdraw\n3.balance\n4.exit")
    choice = int(input("enter your choice: "))
    if choice == 1:
        amount = int(input("enter the aomunt "))
        balance = balance + amount
        print("amoont deposited succesfully! ")
        print("your new balance is: ", balance)
    elif choice == 2:
        amount = int(input("enter the aomunt "))
        if amount <= balance:
            balance = balance - amount
            print("amount withdraw succesfully! ")
            print("your new balance is: ", balance)
        else:
            print("insufficiant balance!")
    elif choice == 3:
        print("current balance: ",balance)
    elif choice == 4:
        print("thank you for using the ATM!!")
        break
    else:
        print("invalid choice! Please try again.")

secret_number = 7
guess = int(input("guess any number from 1-10: "))
while guess != secret_number:
    if guess < secret_number:
        print("too low!, try again.")
    else:
        print("too high!, try again.")
    guess = int(input("guess any number from 1-10: "))
print("Congratulations, You guessed the correct number.")

# build a calculator that keep run until user choose to exit
while True:
    print("------calculator------")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice = int(input("enter the choice number: "))
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

# string qustions
# reverse a string using a while loop
text = input("enter a string: ")
i = len(text) - 1
reverse = ""
while i >= 0:
    reverse = reverse + text[i]
    i = i - 1
print(reverse)

# count the numbers of vowels in a string
text = input("enter the string: ")   
count = 0
index = 0
while len(text) > index: 
    if text[index] in "aeiouAEIOU":
        count = count +  1
    index = index + 1
print("numbers of vowels: ",count)

text = input("enter the string: ")   
count = 0
index = 0
while len(text) > index: 
    if text[index].isalpha()and text[index] not in "aeiouAEIOU":
        count = count +  1
    index = index + 1
print("numbers of consonants : ", count)
