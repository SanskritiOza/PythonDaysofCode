def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = filter_even_numbers(numbers_list)
print(even_numbers_list)
