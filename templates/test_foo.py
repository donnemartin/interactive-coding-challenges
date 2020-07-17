import unittest


class TestFoo(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(foo(None), None)
        self.assertEqual(foo(0), 0)
        self.assertEqual(foo('bar'), 'bar')
        print('Success: test_foo')


def main():
    test = TestFoo()
    test.test_foo()


if __name__ == '__main__':
    main()
