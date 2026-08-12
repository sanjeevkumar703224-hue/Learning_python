#Day - 06(Functions)
#Example 1 – Print Name
def name():
    print("sanjeev")
name()
#Example 2 – Print Age
def age():
    print(21)
age()
#Example 3 – Square
def square(n):
    return n * n
print(square(7))
#Example 4 – Add Two Numbers
def nums(a,b):
    print(a + b)
#Example 5 – Even or Odd
def num(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print(num(8))
#Example 6 – Greater of Two Numbers
def nums(a, b):
    if a > b:
        return a
    return b
print(nums(4, 5))
#Example 7 – Factorial
def main(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= 1
    return fact
print(main(5))
