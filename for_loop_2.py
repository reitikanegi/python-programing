# print the pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print() 

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()

# for i in range(1,6):
#     for j in range():
#         print(i,end="")
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("",end="")
#     for j in range(2*i-1):
#          print("*",end="")
#     print()

# check whether a number is prime or not
# number = int(input("enter the number: "))
# if number<=1:
#     print("the number is not prime.")
# else:
#     prime = True
#     for i in range(2,number):
#         if number%i==0:
#             prime = False
#             break
#     if prime:
#         print("it is a prime numebr.")
#     else:
#         print("not a prime number.")
    
# print all prime nymbers between 1 to 0
# for num in range(2,101):
#     prime = True
#     for i in range(2,num):
#         if num%i==0:
#             prime = False
#             break
#     if prime:
#          print(num)

# genrate a fibonachi series of n number
# n = int(input('enter the numner of terms: '))
# a = 0
# b = 1
# for i in range(n):
#     print(a,end=" ")
#     c = a + b
#     a = b
#     b = c

# find all factor of a givrn number
# num = int(input("enter th enumber:"))
# print("factors of",num, "are:")
# for i in range(1,num +1):
#     if num % i == 0:
#         print(i, end=" ")

# check wheateher a number is perfect number or not
# num = int(input("enter the number: "))       
# sum = 0
# for i in range(1,num):
#     if num%i==0:
#         sum = sum + i
# if num == sum:
#     print("the number is perfect number.")
# else:
#     print("the number is not perfect number.")

# check whether a string is a palindrome using a for loop
# text = input("enter the string: ")
# reverse = "" 
# for i in text:
#     reverse = reverse + i
# if text == reverse:
#     print("The string is palindrome.")
# else:
#     print("The string is not a palindrome,")

# count the fequency of each character in a string
# text = input("enter the string:")
# freq = {}
# for ch in text:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch] = 1
# for ch in freq:
#     print(ch,":",freq[ch])

# print the multiplication table from 1 to 10
# for i in range(1,11):
#     print("table  of", i)
#     for j in range (1,11):
#         print(i ,"x",j,"=",i*j)
#     print()

# find the second largest element in a list
# number = [10,25,8,45,30]
# largest = number[0]
# second_largest = number[0]
# for i in number:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i!= largest:
#         second_largest = i
# print("second largest number is: ", second_largest)

# remove duplicate element from a for loop
# number = [10,20,10,30,28,40,20,40,50]
# unique = []
# for num in number:
#     if num not in unique:
#         unique.append(num)
# print('original list; ',number)
# print("list after remove duplicates: ",unique)
    
