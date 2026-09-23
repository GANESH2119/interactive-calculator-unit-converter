# Interactive Calculator & Unit Converter
# Intern Circle - Task 1


def calculator():
    print("\n===== Basic Calculator =====")

    # Get first number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Get operator
    while True:
        operator = input("Enter operator (+, -, *, /): ")

        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid operator! Please choose +, -, *, or /.")

    # Get second number
    while True:
        try:
            num2 = float(input("Enter second number: "))

            if operator == "/" and num2 == 0:
                print("Cannot divide by zero. Please enter another number.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Perform calculation
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    else:
        result = num1 / num2

    print(f"\nResult: {result}")


def km_to_miles():
    print("\n===== Kilometers to Miles =====")

    while True:
        try:
            kilometers = float(
                input("Enter distance in kilometers: ")
            )
            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    miles = kilometers * 0.621371

    print(f"{kilometers} km = {miles:.2f} miles")


def celsius_to_fahrenheit():
    print("\n===== Celsius to Fahrenheit =====")

    while True:
        try:
            celsius = float(
                input("Enter temperature in Celsius: ")
            )
            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    fahrenheit = (celsius * 9 / 5) + 32

    print(f"{celsius}°C = {fahrenheit:.2f}°F")


def main():

    while True:

        print("\n========================================")
        print(" Interactive Calculator & Unit Converter")
        print("========================================")

        print("1. Basic Calculator")
        print("2. Kilometers to Miles")
        print("3. Celsius to Fahrenheit")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            km_to_miles()

        elif choice == "3":
            celsius_to_fahrenheit()

        elif choice == "4":
            print("\nThank you for using the program!")
            break

        else:
            print("\nInvalid choice! Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()