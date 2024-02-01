def second_largest_element(lst):
    if len(lst) < 2:
        return "List must have at least two elements"

    largest = second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "There is no second-largest element in the list"
    else:
        return second_largest

# Example usage:
my_list = [10, 5, 8, 15, 7]
result = second_largest_element(my_list)
print(f"The second-largest element is: {result}")
