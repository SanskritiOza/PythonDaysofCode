import math

def main():
    # Using math.sqrt() to calculate square root
    number = 25
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")

    # Using math.pow() to calculate power
    base = 2
    exponent = 3
    result = math.pow(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")

    # Using math.sin() to calculate sine
    angle = math.pi / 2  # 90 degrees in radians
    sine_value = math.sin(angle)
    print(f"The sine of {angle} radians is {sine_value}")

    # Using math.cos() to calculate cosine
    cosine_value = math.cos(angle)
    print(f"The cosine of {angle} radians is {cosine_value}")

    # Using math.pi to get the value of pi
    print(f"The value of pi is approximately {math.pi}")

if __name__ == "__main__":
    main()
