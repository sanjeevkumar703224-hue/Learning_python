#Example 1 — Remove Duplicates
num = [1,2,3,4,5,1,2,3,4,5]
kim = set(num)
print(kim)
#Example 2 — Count Unique Values
num = [1,2,3,4,5,1,2,3,4,5]
unique = set(num)
print(len(unique))
#Example 3 — Common Elements
num1 = [2,3,4,6,7,2,2,3,4,5,1]
num2 = [3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
common = set(num1) & set(num2)
print(common)
#Example 4 — Unique Elements From Two Lists
a = [2,3,4]
b = [5,6,7,8,7]
unique = set(a) | set(b)
print(unique)
