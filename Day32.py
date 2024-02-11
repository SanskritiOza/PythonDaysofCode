def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): List of numbers.
        
    Returns:
        float: Average of the numbers.
    """
    if not numbers:
        return None  # Return None if the list is empty
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
numbers = [1, 2, 3, 4, 5]
avg = calculate_average(numbers)
print("Average:", avg)
