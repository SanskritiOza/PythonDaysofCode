def check_key_in_dictionary(my_dict, key_to_check):
    if key_to_check in my_dict:
        print(f"The key '{key_to_check}' exists in the dictionary.")
    else:
        print(f"The key '{key_to_check}' does not exist in the dictionary.")

# Example usage:
my_dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}
key_to_check = 'age'

check_key_in_dictionary(my_dictionary, key_to_check)
