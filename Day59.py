import math

def is_perfect_square(number):
    square_root = math.sqrt(number)
    return square_root.is_integer()

# Test the function
print(is_perfect_square(16))  # True (16 is a perfect square)
print(is_perfect_square(25))  # True (25 is a perfect square)
print(is_perfect_square(10))  # False (10 is not a perfect square)
print(is_perfect_square(0))   # True (0 is a perfect square)
