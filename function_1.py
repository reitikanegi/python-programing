def greet():
    print("hello!",name)
name = "ritika"
greet()
greet()
greet()
    
# Create a function add_numbers(a, b) that returns the sum of two numbers.
def add_numbers(a,b):
    return a + b
print(add_numbers(4,5))

# Define a function is_even(n) that returns True if a number is even, otherwise False.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
        #    OR 
def is_even(n):
    return n % 2 == 0
print(is_even(7))

# Write a function factorial(n) using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# without recurssion
def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
print(fact(5))

# write a fuction to check wheather the number is prime.
def is_prime(n):
    if n <= 1:
       return False
    for i in range(2,n):
        if n%i == 0:
            return False        
    return True
print(is_prime(8))
print(is_prime(7))

# write a function to count vowels in a string
def  vowels(n):
    count = 0
    for ch in n:
        if ch in "aeiouAEIOU":
            count = count + 1
    return count
print(vowels("Mohit"))
        #   OR
def vowel(n):
    count = 0
    index = 0
    while index <len(n):
        ch = n[index]
        if ch in "aeiouAEIOU":
            count = count + 1
        index = index + 1
    return count
print(vowel("Mohit"))

# Write a function to reverse a string without using slicing ([::-1]).
def reverse(n):
    result = ""
    for i in n:
       result = i + result
    return result
print(reverse("mohit"))
        # or
def reverse(n):
    result = ""
    i = len(n) - 1
    while i >= 0:
        result = result + n[i]
        i = i - 1
    return result
print(reverse("mohit"))

# Write a function to check if a string is a palindrome (same forwards and backwards).
def is_palindrome(n):
    original = n
    reverse = ""
    for i in n:
        reverse = i + reverse
    if reverse == original:
        return True
print(is_palindrome("madam"))

# Write a function to generate the Fibonacci sequence up to n terms.
def fibonacci(n):
    a = 0 
    b = 1
    for c in range(n):
        print(a,end=" ")
        c = a + b
        a = b
        b = c
fibonacci(7)

# Write a function to find the largest number in a list
def largest_number(list_):
    largest = list_[0]
    for i in list_:
        if i > largest:
            largest = i
    print(largest)
list_= [24,63,87,55,32]
largest_number(list_)

# Write a function to find the sum of digits of a number
def sum_of_digits(n):
    empty = 0
    while n >0:
        digit = n % 10
        empty = empty + digit
        n = n // 10
    return(empty)
print(sum_of_digits(12345))

# Write a function to check if a number is an Armstrong number 
def armstrong_number(n):
    empty = 0
    while n>0:
        digit = (n % 10) ** 3
        empty = empty + digit
        n = n // 10
    return empty
print(armstrong_number(153))

# Write a function to return all prime numbers up to n.
def prime_numbers(n):
    collect = []
    for num in range(2,n+1):
        prime = True  
        for i in range(2,num):
            if num % i == 0:
                prime = False
                break
        if prime:
            collect.append(num)
    return collect
print(prime_numbers(7))

# Write a function to check if two strings are anagrams (contain the same letters in any order).
def anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
print(anagram("race","care"))