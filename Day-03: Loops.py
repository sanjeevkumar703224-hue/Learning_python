history = []
last_table = []

while True:
    print("\n" + "=" * 40)
    print(" MULTIPLICATION TABLE GENERATOR ")
    print("=" * 40)
    print("1. Generate Table")
    print("2. View History")
    print("3. Save Last Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        while True:
            try:
                number = int(input("Enter Number: "))
                limit = int(input("Generate table till: "))

                if limit <= 0:
                    print("Limit must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter valid integers.")

        last_table = []
        print()

        for i in range(1, limit + 1):
            line = f"{number} x {i} = {number * i}"
            print(line)
            last_table.append(line)

        history.append((number, limit))

    elif choice == "2":

        if len(history) == 0:
            print("\nNo tables generated yet.")
        else:
            print("\nHistory")
            print("-" * 30)

            for index, item in enumerate(history, start=1):
                print(f"{index}. Number = {item[0]}, Till = {item[1]}")

    elif choice == "3":

        if len(last_table) == 0:
            print("\nGenerate a table first.")
        else:
            with open("table.txt", "w") as file:
                for line in last_table:
                    file.write(line + "\n")

            print("\nTable saved successfully as table.txt")

    elif choice == "4":

        print("\nThank you for using the program.")
        break

    else:
        print("\nInvalid Choice. Try Again.")
