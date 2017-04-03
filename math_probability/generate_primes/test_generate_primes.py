from nose.tools import assert_equal, assert_raises


class TestMath(object):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        assert_raises(TypeError, prime_generator.generate_primes, None)
        assert_raises(TypeError, prime_generator.generate_primes, 98.6)
        assert_equal(prime_generator.generate_primes(20), [False, False, True, 
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