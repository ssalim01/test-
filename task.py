
import os

print("Welcome to the online calculator!")

while True:
    choice = input("Enter '1' to calculate equations or '2' to read equations from a file: ")

    if choice == '1':
        # Manually enter equations 
        equations = []

        while True:
            number1 = input("Enter the first number (or 'q' to quit): ")
            if number1.lower() == 'q':
                break

            number2 = input("Enter the second number: ")
            operator = input("Enter an operator (+, -, *, /): ")

            equation = f"{number1} {operator} {number2}"
            equations.append(equation)

            try:
                num1 = float(number1)
                num2 = float(number2)

                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        raise ValueError("Cannot divide by zero!")
                else:
                    raise ValueError("Invalid operator!")

                print("Result:", result)

                equation_with_result = f"{equation} = {result}"
                equations.append(equation_with_result)

            except ValueError as e:
                print("Error:", str(e))
        
        # Save equations to a file
        filename = input("Enter the filename to save equations: ")
        with open(filename, "w") as file:
            file.write("\n".join(equations))

        print("Equations saved to file.")

    elif choice == '2':
        # Read equations from a file
        while True:
            filename = input("Enter the filename to read equations: ")
            if os.path.isfile(filename):
                break
            else:
                print("File does not exist. Please try again.")

        equations = []

        with open(filename, "r") as file:
            for line in file:
                equation = line.strip()
                equations.append(equation)
        
        print("Equations:")
        for equation in equations:
            print(equation)

    else:
        print("Invalid choice. Please try again.")
