import unittest

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

class TestIsPrime(unittest.TestCase):

    def test_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # List of prime numbers
        for prime in primes:
            self.assertTrue(is_prime(prime), f"{prime} is prime but is_prime returned False")

    def test_non_prime_numbers(self):
        non_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]  # List of non-prime numbers
        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime), f"{non_prime} is not prime but is_prime returned True")

    def test_negative_number(self):
        self.assertFalse(is_prime(-5), "-5 is not prime but is_prime returned True")

    def test_zero_and_one(self):
        self.assertFalse(is_prime(0), "0 is not prime but is_prime returned True")
        self.assertFalse(is_prime(1), "1 is not prime but is_prime returned True")

if __name__ == '__main__':
    unittest.main()
