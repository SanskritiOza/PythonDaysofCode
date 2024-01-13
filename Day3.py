def count_vowels(input_string):
    # Define a set of vowels for case-insensitive comparison
    vowels = set("aeiouAEIOU")
    
    # Use a generator expression within the sum function to count vowels
    num_vowels = sum(1 for char in input_string if char in vowels)
    
    return num_vowels

# Example usage:
input_str = input("Enter a string: ")
result = count_vowels(input_str)
print(f"The number of vowels in the given string is: {result}")
