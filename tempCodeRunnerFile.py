def count_(lst, x):
    if len(lst) == 0:
       return 0
    if lst[0] == x:
        return 1 + count_(lst[1:], x)
    else:
        return count_(lst[1:], x)
num = [2, 5, 2, 8, 2, 9]
print(count_(num, 2))