import unittest


class TestMath(unittest.TestCase):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        self.assertRaises(TypeError, prime_generator.generate_primes, None)
        self.assertRaises(TypeError, prime_generator.generate_primes, 98.6)
        self.assertEqual(prime_generator.generate_primes(20), [False, False, True, 
                                                           True, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True])
        print('Success: generate_primes')


def main():
    test = TestMath()
    test.test_generate_primes()


if __name__ == '__main__':
    main()
