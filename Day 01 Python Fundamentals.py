#program 1(print name)
print("Sanjeev")
#program 2(store your details)
name = "sanjeev"
age = 21
print(name)
print(age)
#program 3(add two numbers)
a = int(input())
b = int(input())
print(a+b)
#practice 
#problem 1(print your name)
name = input()
print(name)
#problem 2(print your age)
age = int(input())
print(age)
#problem 3(Take two numbers and print)
a = int(input())
b = int(input())
print("Addition:" ,a+b)
print("Subtraction:" , a-b)
print("Multiplication:", a*b)
#problem 4(Take your birth year and calculate age)
birthyear = int(input())
presentyear = int(input())
age = presentyear - birthyear
print(age)
#problem 5(take length and breath)
length = int(input())
breadth = int(input())
area = length * breadth
print(area)
#Student Information Card
name = "Sanjeev"
age = 21
college = "Vardhaman College Of Engineering"
branch = "CSE (AI & ML)"
print("======== Student Card ========")

print("Name     :",name)
print("Age      :",age)
print("College  :",college)
print("Branch   :",branch)

print("===============================")
 # hacker rank problem 1
 input_string = input()

print("Hello, World.")
print(input_string)
# hacker rank problem 2
i = 4
d = 4.0
s = 'HackerRank '
i2 = int(input())
d2 = float(input())
s2 = input()
print(i + i2)
print(d + d2)
print(s + s2)
# hacker rank problem 3
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost/100 * tip_percent
    tax = tax_percent/100 * meal_cost
    total_cost = meal_cost + tip + tax
    print(round(total_cost))
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
# Leetcode problem 1(problem no 1)
#1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
#9. Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
#2235. Add Two Integers
class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return num1 + num2