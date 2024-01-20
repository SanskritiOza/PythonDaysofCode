def remove_duplicates(input_list):
    # Use a set to store unique elements
    unique_elements = set()

    # Create a new list without duplicates
    result_list = []
    for item in input_list:
        if item not in unique_elements:
            result_list.append(item)
            unique_elements.add(item)

    return result_list

# Example usage:
input_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(input_list)
print("Original list:", input_list)
print("List without duplicates:", result)
