from nose.tools import assert_equal

class TestFoo(object):

    def test_foo(self):
        assert_equal(group_ordered(None), None)
        assert_equal(group_ordered([]), [])
        assert_equal(group_ordered([1]), [1])
        assert_equal(group_ordered([1,2,1,3,2]),[1,1,2,2,3])
        assert_equal(group_ordered(['a','b','a']),['a','a','b'])
        assert_equal(group_ordered([1,1,2,3,4,5,2,1]),[1,1,1,2,2,3,4,5])
        assert_equal(group_ordered([1,2,3,4,3,4]),[1,2,3,3,4,4])
        print('Success: test_foo')

def main():
    test = TestFoo()
    test.test_foo()

if __name__ == '__main__':
    main()
