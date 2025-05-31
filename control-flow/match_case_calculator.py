# match_case_calculator.py

def calculator():
    try:
        # Prompt user for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Prompt user for operation
        operation = input("Choose the operation (+, -, *, /): ")

        # Perform calculation using match-case
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}.")
            case "-":
                result = num1 - num2
                print(f"The result is {result}.")
            case "*":
                result = num1 * num2
                print(f"The result is {result}.")
            case "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}.")
            case _:
                print("Invalid operation selected.")
    
    except ValueError:
        print("Please enter valid numbers.")

# Run the calculator
if __name__ == "__main__":
    calculator()
