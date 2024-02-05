# Function to square each element of a list using a lambda function
square_elements = lambda x: x**2

# Sample list
original_list = [1, 2, 3, 4, 5]

# Use map to apply the lambda function to each element in the list
squared_list = list(map(square_elements, original_list))

# Print the original and squared lists
print("Original List:", original_list)
print("Squared List:", squared_list)
