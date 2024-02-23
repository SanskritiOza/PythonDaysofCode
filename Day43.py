def remove_whitespace(input_string):
    return input_string.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "").replace("\f", "").replace("\v", "")

# Example usage:
input_string = "Hello   World!\n\tThis\tis\r a\f test \vstring."
output_string = remove_whitespace(input_string)
print("Original string:", input_string)
print("String without whitespaces:", output_string)
