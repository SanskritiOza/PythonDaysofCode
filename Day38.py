def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

# Example usage:
nested_list = [1, [2, 3], [4, [5, 6]], 7]
print("Original nested list:", nested_list)
flattened_list = flatten_list(nested_list)
print("Flattened list:", flattened_list)
