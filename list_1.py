# Find the maximum element in a list.
numbers = [ 43,74,66,98,93]
maximum = max(numbers)
print(maximum)

numbers = [43,74,66,98,93]
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
print(maximum)

# Find the minimum element in a list.
minimum = numbers[0]
for i in numbers:
    if i < minimum:
        minimum = i
print(minimum)


# Find the sum of all elements in a list.
numbers = [19, 20, 30, 45, 50]
sum = 0
for i in numbers:
    sum = sum + i
print(sum)

# Find the average of all elements.
numbers = [19, 20, 30, 45, 50]
sum = 0
for i in numbers:
    sum = sum + i
print(sum/len(numbers))

# Print all even numbers from a list.
numbers = [19, 20, 30, 45, 50]
for i in numbers:
    if i%2==0:
        print(i)

# print all odd numbers from the list
numbers = [19, 20, 30, 45, 50]
for i in numbers:
    if i%2!=0:
        print(i) 

# Create a new list containing only positive numbers.
numbers = [19, 20, 5, -3, 8, -1, 0, 12, 45, 50]
lst = []
for i in numbers:
    if i>0:
        lst.append(i)
print(lst)

# Remove all negative numbers from a list.
numbers = [19, 20, 5, -3, 8, -1, 0, 12, 45, 50]
lst = []
for i in numbers:
    if i<=0:
        lst.append(i)
print(lst)

# Find the second largest element
numbers = [50, 50, 40, 30]
largest = float('-inf')
second_largest = float('-inf')
for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(second_largest)

# Find the second smallest element.
numbers = [19, 20, 5, 30, 45, 50]
smallest = float('inf')
second_smallest = float('inf')
for i in numbers:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i > smallest and i < second_smallest:
        second_smallest = i
print(second_smallest)

# Print each element of a list using a for loop.
lst = [19, "mohit", 5, "ritika", 45, 50]
for i in lst:
    print(i)

    # Print each element using a while loop
lst = [19, "mohit", 5, "ritika", 45, 50]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

# Count the number of even and odd elements.
numbers = [1,2,3,4,5,6,7,8,9]
even_count = 0
odd_count = 0
for i in numbers:
    if i %2 == 0:
        even_count += 1
    else:
        odd_count+=1
print("total even numbers are:",even_count)
print("total odd numbers are:",odd_count)

# Count positive, negative, and zero values.
lst = [1,2,65,-1,-84,0,75,-87,-3,0]
positive_num = 0
negitive_num = 0
zero = 0
for i in lst:
    if i>0:
        positive_num += 1
    elif i<0:
        negitive_num += 1
    else:
        zero+=1
print("total postive numbes: ",positive_num)
print("total negaitive numbers: ",negitive_num)
print("total numbers of zeros:",zero)

# Replace all negative numbers with 0
lst = [1,2,65,-1,-84,0,75,-87,-3,0]
for i in range (len(lst)):
    if lst[i] < 0:
        lst[i] = 0
print(lst)

# Square every element in a list.
lst = [1,2,3,4,5,6,7,8,9]
empty_lst = []
for i in lst:
    i = i ** 2
    empty_lst.append(i)
print(empty_lst)

# Multiply every element by 2.
lst = [1,2,3,4,5,6,7,8,9]
empty_lst = []
for i in lst:
    i = i * 2
    empty_lst.append(i)
print(empty_lst)

# Print elements at even indices only.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for idx in range(len(lst)):
    if idx % 2 == 0:  
        print(lst[idx])
