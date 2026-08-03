#DAY -02 (CONDITIONAL STATEMENTS)
#PRACTICES EXAMPLES
#EXAMPLE-01
age = int(input())
if age >= 18:
    print("Adult")
#EXAMPLE-02
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#EXAMPLE-03
marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")
#EXAMPLE -04
username = "sanjeev"
password = 1234
if username == "sanjeev" and password == 1234:
    print("Login Succesfully")
else:
    print("Login Denied")
#EXAMPLE -05
temperature = int(input())
if temperature > 40:
    print("Very Hot")
elif temperature > 30:
    print("Hot")
else:
    print("pleasent")
#PRACTICE
#CHECK EVEN OR ODD
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#CHECK POSITIVE ,NEGATIVE OR ZERO
num = int(input())
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
#CHECK PASS OR FAIL
marks = int(input())
if marks > 35:
    print("Pass")
else:
    print("Fail")
#CHECK VOTING ELIGIBILITY
age = int(input())
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
#FIND THE GREATEST OF TWO NUMBERS
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(num1,"is Greatest")
else:
    print(num2,"is Greatest")
#GREAYEST OF THREE NUMBERS
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2:
    print(n1,"is greatest")
elif n2 > n3:
    print(n2,"is greatest")
elif n3 > n1:
    print(n3,"is greatest")
#DIVISIBLE BY 5
num = int(input())
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
#DIVISIBLE BOTH 3 AND 5
num = int(input())
if (num % 3 == 0) and (num % 5 == 0):
    print("Divisible by both 3 and 5")
else:
    print("Not Divisible by both 3 and 5")
#CHECK LEAP YEAR
year = int(input())
if num % 4 == 0:
    print("Leap year")
elif num % 400:
    print("Not a Leap year")
else:
    print("Leap year")
#CHECK WHEATHER A NUMBER IS POSITIVE AND EVEN
num = int(input())
if (num % 2 == 0) and (num > 0):
    print(num,"Is Positive and Even")
else:
    print(num,"Is Not Positive and Even")
#ATM PIN CHECK
pin = 3445
user = (int(input("enter the atm pin:")))
if pin == user == 3445:
    print("Valid pin")
else:
    print("Incorrect Pin")
#LOGIN SYSTEM
User_id = input("enter the user_id:")
Password = int(input("enter the password:"))
user_id = "Sanjeev@6776"
password = 0000
if user_id == User_id and password == Password:
    print("Login Succesfully")
else:
    print("Invaild Login Details")
#TEMPERATURE CHECKER
temperature = float(input("Enter the temperature (°c):"))
if temperature > 40:
    print("Very hot")
elif temperature > 30:
    print("Hot")
elif temperature > 20:
    print("warm")
elif temperature > 10:
    print("cold")
else:
    print("cold")
#Movie Ticket Eligiblity
age = int(input("enter your age:"))
if age >= 18:
    print("Eligible to take Ticket")
else:
    print("Not Eligible to take Ticket")
#LEETCODE DAY-02
#PROBLEMS

