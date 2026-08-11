history = 
last_report = []

while True:

    print("\n" + "=" * 50)
    print("        NUMBER ANALYZER PRO")
    print("=" * 50)
    print("1. Analyze Number")
    print("2. View History")
    print("3. Save Last Report")
    print("4. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        try:
            number = int(input("\nEnter Number : "))
        except:
            print("Invalid Input")
            continue

        original = number
        n = abs(number)

        # Digit Count
        digit_count = 0

        if n == 0:
            digit_count = 1
        else:
            temp = n
            while temp > 0:
                digit_count += 1
                temp //= 10

        # Sum of Digits
        digit_sum = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            temp //= 10

        # Reverse Number
        reverse = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10

        if number < 0:
            reverse = -reverse

        # Palindrome
        palindrome = "Yes" if reverse == original else "No"

        # Even Odd
        even_odd = "Even" if number % 2 == 0 else "Odd"

        # Positive Negative
        if number > 0:
            sign = "Positive"
        elif number < 0:
            sign = "Negative"
        else:
            sign = "Zero"

        # Armstrong
        armstrong_sum = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            armstrong_sum += digit ** digit_count
            temp //= 10

        armstrong = "Yes" if armstrong_sum == n else "No"

        # Prime
        if n < 2:
            prime = "No"
        else:
            prime = "Yes"
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    prime = "No"
                    break

        # Perfect Number
        if n <= 1:
            perfect = "No"
        else:
            total = 0
            for i in range(1, n):
                if n % i == 0:
                    total += i
            perfect = "Yes" if total == n else "No"

        binary = bin(n)[2:]

        report = [
            f"Number        : {number}",
            f"Digits        : {digit_count}",
            f"Sum           : {digit_sum}",
            f"Reverse       : {reverse}",
            f"Palindrome    : {palindrome}",
            f"Even/Odd      : {even_odd}",
            f"Sign          : {sign}",
            f"Prime         : {prime}",
            f"Perfect       : {perfect}",
            f"Armstrong     : {armstrong}",
            f"Binary        : {binary}"
        ]

        last_report = report

        history.append(number)

        print("\n" + "=" * 40)

        for line in report:
            print(line)

        print("=" * 40)

    elif choice == "2":

        if len(history) == 0:
            print("\nNo History Found")

        else:

            print("\nHistory")

            for i, num in enumerate(history, 1):
                print(i, ".", num)

    elif choice == "3":

        if len(last_report) == 0:
            print("\nAnalyze a number first.")

        else:

            with open("Number_Report.txt", "w") as file:

                for line in last_report:
                    file.write(line + "\n")

            print("\nReport Saved Successfully")

    elif choice == "4":

        print("\nThank You")
        break

    else:

        print("\nInvalid Choice")
