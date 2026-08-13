# Remove duplicates without using set()
# lst = [2,4,3,5,3,6]
# empty = []
# for i in lst:
#     if i not in empty:
#         empty.append(i)
# print(empty)
                #   or
# lst = [2,4,3,5,3,6]
# empty =[] 
# [empty.append(i) for i in lst if i not in empty]
# print(empty)

# Move all zeros to the end while maintaining the order of other elements.
# lst = [1,2,3,0,4,5,6,0,7,8]
# store = []
# for i in lst:
#     if i != 0:
#         store.append(i)
# zero_count = lst.count(0)
# for i in range(zero_count):
#     store.append(0)
# print(store)

# Find the missing number in a list containing numbers from 1 to n.
# lst = [1,2,3,4,5,6,7,9]
# n = 0
# for i in range(len(lst)):
#     if lst[i]>n:
#         n = lst[i]
# expected_sum = n * (n + 1) / 2
# actual_sum = sum(lst)        
# missing_number = expected_sum - actual_sum
# print(missing_number)

# Find the first repeating element
# lst = [1,8,3,4,2,5,4]
# empty = []
# first = 0
# for i in range(len(lst)):
#     if lst[i] in empty:
#         first = lst[i]   
#         break
#     else:
#         empty.append(lst[i])
# print(first)

# Find the first non-repeating element.
# lst = [2,3,4,2,3,4,5,6,7,8]
# first = 0
# for i in range(len(lst)):
#     lst.count(lst[i])
#     if lst.count(lst[i]) == 1:
#         first = lst[i]
#         break
# print(first)

# Merge two sorted lists into one sorted list.
# lst1 = [1,3,5,7,9]
# lst2 = [2,4,6,8,10]
# lst = sorted(lst1 + lst2)
# print(lst)
    #    or
# lst1 = [1,3,5,7,9]
# lst2 = [2,4,6,8,10]
# lst = []
# i = 0
# j = 0
# while i < len(lst1) and j < len(lst2):
#     if lst1[i] < lst2[j]:
#         lst.append(lst1[i])
#         i = i + 1
#     else:
#         lst.append(lst2[j])
#         j = j + 1
# while i < len(lst1):
#     lst.append(lst1[i]) 
#     i += 1
# while j < len(lst2):
#     lst.append(lst2[j])
#     j += 1
# print(lst)

# Find the intersection of two lists without using set().
# lst1 = [1,2,5,6,9,8,3]
# lst2 = [2,4,6,8,5,7,3]
# intersect = []
# for i in range(len(lst1)):
#     if lst1[i] in lst2:
#         intersect.append(lst1[i])
# print(intersect)

# Reverse a list without using slicing ([::-1]) or reverse().
# lst = [2,3,1,5,9,4]
# reverse = []
# for i in range(len(lst)-1,-1,-1):
#     reverse.append(lst[i])
# print(reverse)

# Split a list into two equal halves.
# lst = [2,3,1,5,9,4]
# lst1 = []
# lst2 = []
# length = len(lst) 
# middle_index = len(lst)/2 
# for i in range(len(lst)):
#     if i < middle_index:
#         lst1.append(lst[i])
#     else:
#         lst2.append(lst[i])
# print(lst1)
# print(lst2)

# Find all pairs whose sum equals a given number
lst = [2, 4, 3, 5, 7, 8, 1]
target = 9

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i],lst[j])

