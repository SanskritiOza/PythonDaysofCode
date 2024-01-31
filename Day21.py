def remove_element_from_set(input_set, element_to_remove):
    try:
        input_set.remove(element_to_remove)
        print(f"Element '{element_to_remove}' removed successfully.")
    except KeyError:
        print(f"Element '{element_to_remove}' not found in the set.")

# Example usage:
my_set = {1, 2, 3, 4, 5}
element_to_remove = 3

remove_element_from_set(my_set, element_to_remove)

print("Updated set:", my_set)
