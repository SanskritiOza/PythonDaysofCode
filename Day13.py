import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy()  # Create a copy of the original list to avoid modifying it
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)

print("Original List:", original_list)
print("Shuffled List:", shuffled_result)
