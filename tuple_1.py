# Create a tuple containing 5 integers and print it.
# tup = (1, "mohit", 67, 94 , "rimo")
# print(tup)

# Find the length of a tuple without using len().
# tup = (1, "mohit", 67, 94 , "rimo")
# count = 0
# for i in tup:
#     count = count + 1
# print(count)

# Access the first and last element of a tuple.
# tup = (1, "mohit", 67, 94 , "rimo")
# print(tup[0])
# print(tup[-1])

# Print the elements of a tuple using a for loop.
# tup = (1, "mohit", 67, 94 , "rimo")
# for i in tup:
#     print(i)

# check whether a given element exists in a tuple.
# tup = (1, "mohit", 67, 94, "rimo", 83)
# element = "mohit"
# if element in tup:
#     print("element eixist")
# else:
#     print("element does not exist")

# Count how many times a particular element occurs in a tuple
# tup = (1, "mohit", 67, 94, "rimo", 83, 67,1,1)
# element = 1
# count = tup.count(element)
# print(cou)

# Find the index of a particular element in a tuple.
# tup = (10,20,30,40,50)
# element = 10
# index = tup.index(element)
# print(index)

# Convert a list into a tuple.
# lst = [10,20,30,40,50]
# tup = tuple(lst)
# print(tup)

# Convert a tuple into a list.
# tup = (10,20,30,40,50)
# lst = list(tup)
# print(lst)

# Find the largest element in a tuple without using max().
# tup = (10,20,30,40,50)
# largest = 0
# for i in tup:
#     if i > largest:
#         largest = i
# print(largest)

# Find the smallest element without using min().
# tup = (10,20,3,40,50)
# smallest = tup[0]
# for i in range(len(tup)):
#     if tup[i] < smallest:
#         smallest = tup[i]
# print(smallest)

# Find the sum of all elements without using sum().
# tup = (36,27,35,98,30)
# total = 0
# for i in tup:
#     total = i + total
# print(total)

# Count how many even and odd numbers are present in a tuple.
# tup = (1,2,3,4,5,6,7,8,9)
# even_count = 0
# odd_count = 0
# for i in tup:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("total even:",even_count)
# print("total odd:",odd_count)

# Create a new tuple containing only the even numbers
# tup = (10, 15, 22, 31, 40, 53, 64)
# even = ()
# for i in tup:
#     if i % 2 == 0:
#         even = even + (i,)
# print(even)
#                or    
# tup = (10, 15, 22, 31, 40, 53, 64)
# lst_2 = []
# for i in tup:
#     if i % 2 == 0: 
#         lst_2.append(i)
# print(tuple(lst_2))

# Reverse a tuple without using reverse()
# tup = (10, 15, 22, 31, 40, 53, 64)
# reverse = []
# for i in range(len(tup)-1,-1,-1):
#     reverse.append(tup[i])
# print(tuple(reverse))

# Find the second-largest element in a tuple.
# tup = (45, 12, 89, 23, 67, 34, 91)
# largest = tup[0]
# second_largest = tup[0]
# for i in range(len(tup)):
#     if tup[i]>largest:
#         second_largest = largest
#         largest = tup[i]
#     elif  tup[i]>second_largest:
#         second_largest = tup[i]
# print(second_largest) 

# Remove duplicate elements from a tuple
# tup = (45, 12, 89, 23, 12, 34, 91)
# unique = []
# for i in tup:
#     if i not in unique:
#         unique.append(i)
# print(tuple(unique))

# Check whether a tuple is sorted or not.
# tup = (10, 20, 30, 40, 50)
# is_sorted = True
# for i in range(len(tup) - 1):
#     if tup[i] > tup[i + 1]:
#         is_sorted = False
#         break
# if is_sorted:
#     print("Tuple is sorted")
# else:
#     print("Tuple is not sorted")

# Merge two tuples into one tuple.
# tup1 = (1,2,3,4,5,6,7)
# tup2 = (8,34,25,99,2)
# tup = tup1 + tup2
# print(tup)


