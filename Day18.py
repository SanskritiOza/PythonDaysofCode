def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the function to find the largest number
largest_number = find_largest(num1, num2, num3)

# Display the result
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")
