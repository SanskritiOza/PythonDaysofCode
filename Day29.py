import random

def generate_random_number(start, end):
    """
    Generate a random number within the given range [start, end].
    
    Args:
        start (int): The lower bound of the range.
        end (int): The upper bound of the range.
        
    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(start, end)

# Example usage:
start_range = 1
end_range = 100
random_number = generate_random_number(start_range, end_range)
print("Random number between", start_range, "and", end_range, ":", random_number)
