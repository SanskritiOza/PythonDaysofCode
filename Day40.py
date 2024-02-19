def gcd(a, b):
    """
    Function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Parameters:
        a (int): First number.
        b (int): Second number.
    
    Returns:
        int: The greatest common divisor of the two numbers.
    """
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18
print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))
