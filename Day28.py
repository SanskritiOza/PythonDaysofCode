def remove_nth_element(lst, n):
    if n < 0 or n >= len(lst):
        print("Error: Index out of range")
        return lst
    else:
        del lst[n]
        return lst

# Test the function
my_list = [1, 2, 3, 4, 5]
n = 2
result = remove_nth_element(my_list, n)
print(f"List after removing the {n}th element: {result}")
