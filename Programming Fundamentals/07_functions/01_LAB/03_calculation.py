def multiply(operator, a, b):
    if operator == 'multiply':
        return a * b

def divide(operator, a, b):
    if operator == "divide" and b != 0:
        return int(a / b)  # Integer division
    else:
        return "Error! Can't divide by Zero!"

def add(operator, a , b):
    if operator == 'add':
        return a + b

def subtract(operator, a, b):
    if operator == 'subtract':
        return a - b

def calculator(operator, a, b):
    if operator == 'add':
        return add(operator, a, b)
    elif operator == 'subtract':
        return subtract(operator, a, b)
    elif operator == 'multiply':
        return multiply(operator, a, b)
    elif operator == 'divide':
        return divide(operator, a, b)
    else:
        return "Invalid operator!"  # Handling invalid operators

# Example Usage:
input_operator = input()
num1 = int(input())
num2 = int(input())

result = calculator(input_operator, num1, num2)
print(result)
