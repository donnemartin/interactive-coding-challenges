from nose.tools import assert_equal


class TestFoo(object):

    def test_foo(self):
        assert_equal(foo(None), None)
        assert_equal(foo(0), 0)
        assert_equal(foo('bar'), 'bar')
        print('Success: test_foo')

def main():
    test = TestFoo()
    test.test_foo()

if __name__ == '__main__':
    main()