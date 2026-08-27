# Find the frequency of every element in a tuple
t = (1, 2, 2, 3, 1, 4, 2)
visited = []
for i in t:
    if i not in visited:
       print(i, "=", t.count(i))
       visited.append(i)
        #  without count
t = (1, 2, 2, 3, 1, 4, 2)
visited = []
for i in t:
    if i not in visited:
        count = 0
        for j in t:
            if i == j:
                count += 1
        print(i, "=", count)
        visited.append(i)

# Find all pairs whose sum equals a target.
t = (2, 4, 3, 5, 7, 8, 1)
target = 9
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i] + t[j] == target:
            print(t[i],t[j])
        #        OR
t = (2, 4, 3, 5, 7, 8, 1)
target = 9
seen = []
for i in t:
    needed = target - i 
    if needed in seen:
        print(needed, i)
    seen.append(i) 

# Find the common elements between two tuples.
t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)
t = []
for i in range(len(t1)):
    for j in range(len(t2)):
       if t1[i] == t2[j]:
        t.append(t1[i])
print(tuple(t))
        #       or
t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)   
common = set(t1) & set(t2)
print(tuple(common)) 

# Find elements that are present in the first tuple but not in the second.
t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)   
unique = []
for i in t1:
    if i not in t2:
        unique.append(i)
print(tuple(unique))
        #      or
t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)  
unique = set(t1) - set(t2)
print(tuple(unique)) 

# Unpack this tuple into separate variables:
student = ("Mohit", 21, "Python")
name, age, course = student
print(name)
print(age)
print(course)

# Swap two variables using tuple unpacking.  
a = (10)
b = ("mohit","rimo")
a, b = b, a
print(a)
print(b)

# Find the third-largest element in a tuple without using sort() or sorted()
        #    for distinct values
tup = (23,12,89,34,56,90)
largest = tup[0]
second_largest = tup[0]
third_largest = tup[0]
for i in range(len(tup)):
    if tup[i]>largest:
        third_largest = second_largest
        second_largest = largest
        largest = tup[i]
    elif tup[i]>second_largest:
        third_largest = second_largest
        second_largest = tup[i]
    elif tup[i]>third_largest:
        third_largest = tup[i]
print(third_largest)
            
                #   for same values
tup = (90, 80, 80, 70, 60)
largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')
for i in range(len(tup)):
    if tup[i] == largest or tup[i] == second_largest or tup[i] == third_largest:
        continue
    if tup[i]>largest:
        third_largest = second_largest
        second_largest = largest
        largest = tup[i]
    elif tup[i]>second_largest:
        third_largest = second_largest
        second_largest = tup[i]
    elif tup[i]>third_largest:
        third_largest = tup[i]
print(third_largest)

# create a tuple containing squares of all numbers from another tuple.
t = (1, 2, 3, 4, 5)
square = []
for i in t:
    i = i ** 2
    square.append(i)
print(tuple(square)) 

# Check whether two tuples contain the same elements.
t1 = (1, 2, 3, 4)
t2 = (1, 2, 3, 4)
if t1 == t2:
    print("both tuples are same.")
else:
    print("tuples are different.")

# Find the element that occurs most frequently in a tuple.
tup = (1, 2, 2, 3, 1, 2, 4)
most_frequent = tup[0]
highest_count = 0
visted = []
for i in tup:
    if i not in visted:
        count = 0
        for j in tup:
            if i == j:
                count += 1
        if count > highest_count:
            highest_count = count
            most_frequent = i
        visted.append(i)
print(most_frequent)


            
            