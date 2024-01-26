def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Starting with the first two numbers in the sequence

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

# Example usage:
n = int(input("Enter the value of n: "))  # You can also set n to a specific value
fibonacci_result = generate_fibonacci(n)

print(f"The first {n} numbers of the Fibonacci sequence are:")
print(fibonacci_result)
