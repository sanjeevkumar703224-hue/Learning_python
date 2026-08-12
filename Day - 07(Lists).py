#day - 07(Lists)
#Example 1 — Print all elements
num = [2,3,4,5,6]
for x in num:
    print(x)
#Example 2 — Find sum
num = [2,3,4,5,6,7]
print(sum(num))
#Example 3 — Count even numbers
num = [10, 20, 20, 30, 30]
count = 0
for x in num:
    if x % 2 == 0:
        count += 1 
print(count)
#Example 4 — Find largest manually
num = [2,6,7,8,4,5]
largest = 0
for x in num:
    if x > largest:
        largest = x
print(largest)
#
