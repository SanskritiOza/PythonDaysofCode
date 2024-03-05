def reverse_words(string):
    # Split the string into words
    words = string.split()

    # Reverse each word
    reversed_words = [word[::-1] for word in words]

    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string

# Example usage:
input_string = "Hello world, this is a test."
reversed_string = reverse_words(input_string)
print(reversed_string)
