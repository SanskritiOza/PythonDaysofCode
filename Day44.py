def read_integer():
    while True:
        try:
            num = int(input("Please enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Example usage:
if __name__ == "__main__":
    integer = read_integer()
    print("You entered:", integer)
