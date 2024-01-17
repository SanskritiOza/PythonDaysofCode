def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

# Input from the user
user_input = float(input("Enter a number: "))

# Check the number
check_number(user_input)
