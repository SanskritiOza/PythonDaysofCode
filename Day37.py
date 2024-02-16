def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

# Example dictionary
example_dict = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

# Printing keys and values
print("Printing keys and values of the dictionary:")
print_dictionary(example_dict)
