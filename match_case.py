# write a program using match case statement to print the day of the week for the number 1-7
day = int(input("enter the number : "))
match day:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thurasay")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("no such day exist")

# craete a calculator using match case for +,-,*,/
a = int(input("enter first number"))
b = int(input("enter second number"))
calculation =input("what you want to do =" )
match calculation:
    case "addition":
        print("result =", a + b)
    case "subtraction":
        print("result =", a - b)
    case "multiplication":
        print("result =", a * b)
    case "division":
        print("result =", a / b)
    case _:
        print("invalid case")

ch = input("Enter the character")
match ch:
    case "a"|"e"|"i"|"o"|"u":
        print("it is a vowel")
    case _:
        print("it is not a vowel")    
        
grades = input("grade:").upper()
match grades:
    case "A":
        print("A means excelent")
    case "B":
        print("B means very good")
    case "c":
        print("c means good")
    case "D":
        print("D means pass")
    case "E":
        print("E means fail")
    case _:
        print("invalid grade")      

# print("MENU\n1.addition\n2.subtraction\n3.multiplication\n4.division")
choice = int(input("enter your choice from 1-4: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
match choice:
    case 1:
        print(f"{a}+{b}=", a+b)
    case 2:
        print(f"{a}-{b}=", a-b)
    case 3:
        print(f"{a}x{b}=", a*b)
    case 4:
        print(f"{a}/{b}=", a/b)
    case _:
        print("error")

# write a program where the deafult case contain if ekse statement 
num = int(input("Enter the number:"))
match num:
    case 1:
        print("you have selected:", num)
    case 2:
        print("you have selected:", num)
    case _:
        if num >= 20:
            print("you have selected:", num)
        else:
            print("number:",num)

num = int(input("enter the number"))
match num:
    case 1|3|5|7|9:
        print("it is an odd number")
    case 2|4|6|8:
        print("it is an even number")
    case _:
        print("invalid case")

# program using pattern matching 
x = int(input("enter x-corrdinate: "))
y = int(input("Enter y-coordinate: "))
match (x,y):
    case (0,0):
        print("point is at the orign.")
    case (_,0):
        print("point is at the X-axis.")
    case (0,_):
        print("point is at the Y-axis.")
    case _:
        print("point is not on any axis")

# create a ATM Menu using match case with opiton like balance , deposite ,withdraw ,  and exit
Balance = 50000
print("ATM Menu\n1.Balance\n2.Deposite\n3.withdraw\n4.Exit")
choice = int(input("enter the choice from the menu: "))
match choice:
    case 1:
        print("your balance is:", Balance)
    case 2:
        amount = int(input("Enter the amount you want to deposite: "))
        Balance = Balance + amount
        print("deposited successfully")
        print("your new bank balance is: ", Balance)
    case 3:
        amount = int(input("Enter the amount you want to deposite: "))
        if amount <= Balance:
           Balance = Balance - amount
           print("Withdraw succesfully.")
           print("your new balance is: ", Balance)
        else:
            print("you does not have sufficient balance to withdraw this much amount.")
    case 4:
        print("you have exit the ATM!")
    case _:        
        print("Invalid choice")
print("Thank You for using the ATM!")
