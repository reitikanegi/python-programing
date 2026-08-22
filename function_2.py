# Define a function reverse_string(s) that returns the reversed string.
# def reverse_string(s):
#     reverse = ""
#     for i in s:
#         reverse = i + reverse
#     return(reverse)
# print(reverse_string("mohit"))

# Write a function sum_list(lst) that returns the sum of all elements in a list.
# def sun_list(lst):
#     total = 0
#     for i in lst:
#         total = i + total
#     return total
# list1= [1,2,3,4,5]
# print(sun_list(list1))

# Write a function fibonacci(n) that returns the first n Fibonacci numbers as a list.
# def fibonacci(n):
#     list_ = []
#     a = 0
#     b = 1
#     for i in range(1,n):
#         list_.append(a)
#         c = a + b
#         a = b
#         b = c
        
#     return list_
# print(fibonacci(7))

# Define a function apply_operation(lst, func) that applies a given function to each element of a list.
# def apply_list(lst,func):
#     result = []
#     for i in lst:
#        result.append(func(i))
#     return result
# def square(x):
#     return x * x
# print(apply_list([1,2,3,4],square))

# Write a function digital_root(n) that keeps summing digits until only one digit remains.
# def digital_root(n):
#     while n >= 10:
#         total = 0
#         while n > 0:
#             digit = n % 10
#             total = total + digit
#             n = n // 10
#         n = total
#     return n
# print(digital_root(1234))
        
# Create a function decorator_example(func) that prints "Before function call" and "After function call" around the execution of func
# def decorator_(func):
#     def wrapper():
#         print("before function call.")
#         func()
#         print("after function call")
#     return wrapper
# def greet():
#     print('hello,sir!')

# greet = decorator_(greet)
# greet()

