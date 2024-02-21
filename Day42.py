def divide(x, y):
    try:
        result = x / y
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")

# Example usage:
try:
    divide(10, 2)  # This will execute without error
    divide(5, 0)   # This will raise a ZeroDivisionError
except:
    print("An error occurred.")
