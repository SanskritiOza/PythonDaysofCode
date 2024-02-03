def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in input_string if char not in vowels)
    return result

# Example usage:
input_string = "Hello, World!"
output_string = remove_vowels(input_string)
print("Input String:", input_string)
print("String without vowels:", output_string)
