#prompt user forr two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Ask the type of operation
operation = input("choose the operation (+, -, *, /): ")

# Perform the calculation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")

    case "-":
        result = num1 - num2
        print(f"The result is {result}")

    case "*":
        result = num1 * num2
        print(f"The result is {result}")
        
    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")   
        else:
            result = num1 / num2
            print(f"The result is {result}")
            
    case _:

        print("Invalid operation selected.")                           
