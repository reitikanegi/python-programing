# Sort a list in ascending order
# lst = [2,5,8,9,3,4]
# lst.sort()
# print(lst)

# Sort a list in descending order
# lst = [2,5,8,9,3,4]
# lst.sort(reverse=True)
# print(lst)

# Copy one list into another
    #    using slicing
# lst = [2,5,8,9,3,4]
# lst_1 = lst[:]
# print(lst_1)
    #   using lsit()construction
# lst = [2,5,8,9,3,4]
# lst_1 = list(lst)
# print(lst_1)
        # using .copy() method
# lst = [2,5,8,9,3,4]
# lst_1 = lst.copy()
# print(lst_1)
#   for nested list (deep copy)
# import copy
# list1 = [[1, 2], [3, 4]]
# list2 = copy.deepcopy(list1)
# print(list2)

# Merge two lists.
    #   (simple merge)concatination
# list1 = [2,5,3,7,8]
# list2 = [5,4,6,9,1]
# merged = list1+list2
# print(merged) 
    #  zip(element wise merge)
# list1 = [2,5,3,7,8]
# list2 = [5,4,6,9,1]
# merge = list(zip(list1, list2))
# print(merge)
    #   unique merge(remove duplicate)
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# merge = list(set(list1+list2))
# print(merge)

# Clear all elements from a list
# lst = [2,4,5,6,78]
# lst.clear()
# print(lst)
    # reassign to an empty list
# lst = [2,4,5,6,78]
# lst = []
# print(lst)
    #  using del
# lst = [2,4,5,6,78]
# del lst[:]
# print(lst)
    #   using pop in a loop
# lst = [2,4,5,6,78]
# while lst:
#     lst.pop()
    #   Using Multiplication
# print(lst)lst = [2, 4, 5, 6, 78]
# lst *= 0
# print(lst)

# Remove duplicate elements from a list
# lst = [1,2,3,2,4,5,6,4,5]
# empty_lst = []
# for i in lst:
#     if i not in empty_lst:
#         empty_lst.append(i)
# print(empty_lst)

# lst = [1,2,3,"ritika","mohit","ritika",4,5,6,4,5]
# list_ = set(lst)
# print(list_)

# Check if a list is empty.
# lst = []
# if len(lst)==0:
#     print("list is empty.")
# else:
#     print(lst)
      #  or
# lst = []
# if lst == []:
#     print("list is empty.")
# else: 
#     print(lst)
    #or
# lst = []
# if not lst:
#     print("list is empty.")
# else:
#     print(lst)

# Convert a string into a list of characters
# text = input("enter a string")
# lst = []
# for i in text:
#     lst.append(i)
# print(lst)    
    #or 
# text = input("enter the string : ")
# lst = list(text)
# print(lst)

# Join two lists without using +
    # method 1: extend()
# lst_1 = [3,45,23,67,85]
# lst_2 = [45,34,76,95,43]
# lst_1.extend(lst_2)
# print(lst_1)
#     #  method 2: unpacking
# lst_1 = [3,45,23,67,85]
# lst_2 = [45,34,76,95,43]
# lst = [*lst_1,*lst_2]
# print(lst)