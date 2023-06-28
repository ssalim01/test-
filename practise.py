import os
#os is a module allowing the code to be more readable and efficient 
print("Welcome to online calculator!")
while True:
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")
    operator = input("Enter an operator (+, -, *, /): ")

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

        equation = f"{num1} {operator} {num2} = {result}"
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")


    except ValueError as e:
        print("Error:", str(e))