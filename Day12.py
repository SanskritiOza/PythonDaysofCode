def reverse_string(input_string):
    # Using slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string

# Get user input
user_input = input("Enter a string: ")

# Call the function to reverse the string
result = reverse_string(user_input)

# Display the reversed string
print("Reversed String:", result)
