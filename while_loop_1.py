# orint the number from 1 - 10
# a = 1
# while(a<=10):
#     print(a)
#     a = a + 1

# print even number from 1-20
# a = 2
# while(a<=20):
#     print(a)
#     a = a + 2

# print odd number
# a = 1
# while(a<=20):
#     print(a)
#     a = a + 2

# print sum of number from 1 to n
# n = int(input("enter the number: "))
# a = 1
# sum = 0
# while(a<=n):
#     sum = sum + a
#     a = a + 1
# print(sum)
    
# find the product of number from 1-n(factorial)
# n = int(input("enter the number"))
# a = 1
# product = 1
# while(a<=n):
#     product = product * a
#     a = a+1
# print(product)

# print the multiplication table of a given number
# number = int(input("enter the number: "))
# a = 1
# while(a<=10):
#     print(number,"x",a,"=",number*a)
#     a = a + 1
 
# count the number of digits in an integer
# digit = int(input("enter the digit"))
# count = 0
# while(digit>0):
#     count = count + 1
#     digit = digit // 10
#  print("count:",count)

# revrse a number
# n = int(input("enter the number: "))
# reverse = 0
# while(n>0):
#    digit = n % 10
#    reverse = reverse*10 + digit
#    n = n // 10
# print(reverse)

# find the sum of digits of a number
# n = int(input("enter the digits: "))
# sum = 0
# while(n>0):
#     digit = n % 10
#     sum = sum + digit
#     n = n//10
    
# print(sum)

# check wheter a number is a palindromme
# n = int(input("enter the number: "))
# original = n
# reverse = 0
# while(n>0):
#     digit = n%10
#     reverse = reverse * 10 + digit
#     n = n//10
# if original == reverse:
#     print('the number is palindrome')
# else:
#     print("the number is not a palindrome.")

# check whether a number is amstrong number
# n = int(input("enter the number: "))
# original = n
# temp = n
# count = 0
# sum = 0
# while temp>0:
#     count = count + 1
#     temp = temp // 10
# temp = original
# while temp>0:
#     digit = temp % 10
#     sum = sum + digit ** count
#     temp = temp // 10
# if sum == original:
#     print('armstrong number.')
# else:
#     print('not a armstrong number.')

# check wheather the number is prime number
# n = int(input("enter the number: "))
# if n <= 1:
#     print(n,"is not a prime number.")
# else:
#     i = 2
#     prime= True
#     while i < n:
#         if n % i == 0:
#             prime = False
#             break
#         i = i + 1
#     if prime:
#         print(n,"is prime.")
#     else:
#         print(n,"is not a prime number.")

# print al prime number from 1- 10
# n = int(input('enter the number: '))
# num = 2
# while num <= n: 
#     i = 2
#     prime = True
#     while i < num:
#         if num % 2 == 0: 
#             prime = False
#             break
#         i = i + 1
#     if prime:
#         print(num)
#     num = num + 1

