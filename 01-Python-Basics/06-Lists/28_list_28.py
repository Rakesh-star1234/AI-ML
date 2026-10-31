
# Q28: Find common elements in two lists

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = list(set(list1) & set(list2))
print(common)
