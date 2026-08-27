# Find all duplicate elements in a list
# lst = [1,2,4,"mohit",2,6,8,"mohit",6]
# duplicate = []
# seen = []
# for i in lst:
#     if i in seen and i not in duplicate:
#         duplicate.append(i)
#     else:
#         seen.append(i)
# print("duplicate elements:", duplicate)
        #    using count()
# lst = [1,2,4,"mohit",2,6,8,"mohit",6]
# duplicate = []
# for i in lst:
#     if lst.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)
# print(duplicate)
    # using set()
# lst = [1,2,4,"mohit",2,6,8,"mohit",6]
# duplicate = []
# for i in set(lst):
#    if lst.count(i)>1:
#       duplicate.append(i)
# print(duplicate)

# 
# Find the frequency of each element.
# lst = [1,2,3,4,5,1,2,2,3,3,3,4,4,4]
# empty_list = []
# for i in lst:
#     if i not in empty_list:
#         count = lst.count(i)
#         print(i,'=',count)
#         empty_list.append(i)

# Rotate a list to the left by one position.
# lst = [1,2,3,4,5]
# store = lst[0]
# for i in range(len(lst)-1):
#     lst[i]= lst[i+1]
# lst[-1] = store
# print(lst)
    #    using slicing
# lst = [1,2,3,4,5]
# lst = lst[1:] + [lst[0]]
# print(lst)
    
# Rotate a list to the right by one position
# lst = [1,2,3,4,5]
# store = lst[-1]
# for i in range(len(lst)-1, 0,-1):
#     lst[i] = lst[i-1]
# lst[0] = store
# print(lst)
#    using slicing
# lst = [1,2,3,4,5]
# lst = [lst[-1]] + lst[:-1]
# print(lst)

# Check whether a list is a palindrome
# lst = [1,2,3,2,1]
# n = len(lst)
# for i in range(0,(n//2)-1):
#     if lst[i] != lst[n-1-i]:
#         print("not palindrome")
#         break
#     else:
#         print("palindrome")
        # or
# lst = [1,2,3,4,5]
# left = 0
# right = len(lst)-1
# while left < right:
#     if lst[left] != lst[right]:
#         print("not palindrome")
#         break
#     left = left + 1
#     right = right + 1
# print("palindrome")


# find the commaon element in two list
# lst1 = [14,76,45,23,90]
# lst2 = [36,87,76,14,23]
# common = set(lst1).intersection(set(lst2))
# print(common)
        # or
# lst1 = [14,76,45,23,90]
# lst2 = [36,87,76,14,23]
# empty_lst = []
# for i in lst1:
#     for j in range(len(lst2)):
#         if i == lst2[j]:
#             empty_lst.append(i)
# print(empty_lst)
        #  or
# lst1 = [14,76,45,23,90]
# lst2 = [36,87,76,14,23]
# common = [i for i in lst1 if i in lst2]
# print(common)


# Find the unique elements from two lists.
# lst1 = [14,76,45,23,90]
# lst2 = [36,87,76,14,23]
# unique = [ i for i in lst1 if i not in lst2] + [j for j in lst2 if j not in lst1]
# print(unique)
    #   or

# lst1 = [14,76,45,23,90]
# lst2 = [36,87,76,14,23]
# empty_lst = []
# for i in lst1:
#     if i not in lst2:
#         empty_lst.append(i)
# for j in lst2:
#     if j not in lst1:
#         empty_lst.append(j)
# print(empty_lst)
        #  or
# lst1 = [14,76,45,23,90]
# lst2 = [36,87,76,14,23]
# unique = set(lst1).symmetric_difference(set(lst2))
# print(unique)


# Separate even and odd numbers into two different lists.
# lst = [1,2,3,4,5,6,7,8,9]
# even = []
# odd = []
# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even", even)
# print("odd", odd)

# Find the largest and smallest elements in one traversal
# numbers = [19, 5, 30, 2, 45, 10]
# largest = numbers[0]
# smallest = numbers[0]
# for i in range(len(numbers)):
#     if numbers[i] > largest:
#         largest = numbers[i] 
#     if numbers[i] < smallest:
#         smallest = numbers[i]
# print(largest)
# print(smallest)

# Implement list sorting without using sort() (e.g., Bubble Sort or Selection Sort).
#  BUBBLE sort 
# lst = [4,9,2,6,5]
# for i in range(len(lst) - 1):
#     for j in range(len(lst) - 1 -i):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j + 1] = lst[j+1], lst[j]
# print(lst)  
        
#      selection short
# lst = [4,9,2,6,5]
# for i in range(len(lst)-1):
#     min_index = i
#     for j in range(i +1,len(lst)):
#         if lst[j] < lst[min_index]:
#             min_index = j
#     lst[min_index],lst[i] = lst[i], lst[min_index]
# print(lst)       


    
        