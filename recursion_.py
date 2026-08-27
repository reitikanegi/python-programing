# Print numbers from 1 to N using recursion.
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)
print_numbers(5)

# Print numbers from N to 1 using recursion.
def reverse_number(n):
    if n == 0:
        return
    print(n)
    reverse_number(n-1)
reverse_number(5)

# Find the sum of first N natural numbers.
def sum_(n):
    if n == 0:
        return 0
    return n + sum_(n-1)
print(sum_(5))

# Find the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))

# Calculate a^b using recursion.
def power_(a,b):
    if b == 0:
        return 1
    else:
        return a * power_ (a, b-1)
print(power_(2,5))

# Find the sum of digits of a number.
def digit(n):
    if n == 0:
        return 0
    else:
        return n%10 + digit(n//10)
print(digit(1234))

# Count the number of digits in a number.
def count(n):
    if n == 0:
        return 0
    else:
        return 1 + count(n//10)
print(count(12345))

# Reverse a number using recursion.
def reverse(n, rev = 0):
    if n == 0:
        return rev
    rev = rev * 10 + n % 10
    n = n // 10
    return reverse(n, rev)
print(reverse(1234))

# Find the GCD of two numbers using recursion.
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
print(gcd(18,12))

# Print the Fibonacci series using recursion.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(7):
    print(fibonacci(i), end=" ")

    # Find the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# Check whether proa string is a palindrome using recursion.
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
s = input("enter the string: ")
if palindrome(s):
    print("Palindrome.")
else:
    print("Not Palindrome.")
    #  or
def palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s, left + 1, right - 1)
s = input("enter the string: ")
if palindrome(s, 0, len(s) - 1):
    print("Palindrome.")
else:
    print("Not Palindrome.")

# Reverse a string using recursion.

