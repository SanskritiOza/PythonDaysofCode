# Swapping values using tuple unpacking
def swap_pythonic(a, b):
    return b, a

# Example usage:
x = 5
y = 10
x, y = swap_pythonic(x, y)
print("After swapping (pythonic): x =", x, ", y =", y)
