def print_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Get user input for the number
user_input = input("Enter a number to print its multiplication table: ")

# Check if the input is a valid integer
try:
    number = int(user_input)
    print_multiplication_table(number)
except ValueError:
    print("Please enter a valid integer.")
