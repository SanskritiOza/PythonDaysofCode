def second_smallest(lst):
    if len(lst) < 2:
        return "List must contain at least two elements"
    
    # Find the minimum element
    min_element = min(lst)
    
    # Initialize second_min with infinity or a value larger than any possible value in the list
    second_min = float('inf')
    
    # Iterate through the list to find the second smallest element
    for num in lst:
        if num > min_element and num < second_min:
            second_min = num
            
    # If second_min remains infinity, it means there was no second smallest element
    if second_min == float('inf'):
        return "No second smallest element found"
    else:
        return second_min

# Test the function
my_list = [3, 1, 5, 7, 2, 8]
print("Second smallest element:", second_smallest(my_list))
