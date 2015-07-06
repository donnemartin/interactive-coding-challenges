from nose.tools import assert_equal


class TestFib(object):

    def test_fib(self, func):
        result = []
        for i in range(num_items):
            result.append(func(i))
        fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert_equal(result, fib_seq)
        print('Success: test_fib')

def main():
    test = TestFib()
    test.test_fib(fib_recursive)
    test.test_fib(fib_dynamic)
    test.test_fib(fib_iterative)

if __name__ == '__main__':
    main()