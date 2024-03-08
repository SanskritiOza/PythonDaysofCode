def key_with_max_value(dictionary):
    if not dictionary:
        return None
    return max(dictionary, key=dictionary.get)

# Example usage:
my_dict = {'a': 10, 'b': 20, 'c': 5}
max_key = key_with_max_value(my_dict)
print("Key with maximum value:", max_key)
