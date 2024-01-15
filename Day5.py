def find_max_min(lst):
    if not lst:
        return None, None

    max_val = min_val = lst[0]

    for num in lst:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    return max_val, min_val

# Example usage:
my_list = [3, 7, 1, 5, 9, 2]
max_value, min_value = find_max_min(my_list)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
