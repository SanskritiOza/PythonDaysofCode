def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of the first dictionary to preserve its original content
    merged_dict.update(dict2)   # Update with the content of the second dictionary
    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Method 1: Using update() method
merged_dict_method1 = merge_dicts(dict1, dict2)
print("Merged dictionary using update() method:", merged_dict_method1)

# Method 2: Using unpacking operator **
merged_dict_method2 = {**dict1, **dict2}
print("Merged dictionary using unpacking operator **:", merged_dict_method2)
