def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs an arithmetic operation on two numbers.

    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: The result of the operation, or an error message for division by zero
    """

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "DIVISION_BY_ZERO"   # A code your main.py can check
        else:
            return num1 / num2

    else:
        return "INVALID_OPERATION"       # In case operation is outside the 4 valid ones

