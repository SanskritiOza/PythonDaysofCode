def count_char_occurrences(input_string, target_char):
    count = 0
    for char in input_string:
        if char == target_char:
            count += 1
    return count

# Example usage:
input_string = "programming is fun"
target_char = "g"
result = count_char_occurrences(input_string, target_char)

print(f"The character '{target_char}' appears {result} times in the string.")
