def safe_string_to_int(string):
    try:
        return int(string)
    except ValueError:
        print("Error: Input is not a valid integer")
        return None

# Example usage:
input_string = "123"
result = safe_string_to_int(input_string)
if result is not None:
    print("Converted integer:", result)
