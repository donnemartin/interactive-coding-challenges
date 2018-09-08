import sys
from nose.tools import assert_equal


class TestStackMin(object):

    def test_stack_min(self):
        print('Test: Push on empty stack, non-empty stack')
        stack = StackMin()
        stack.push(5)
        assert_equal(stack.peek(), 5)
        assert_equal(stack.minimum(), 5)
        stack.push(1)
        assert_equal(stack.peek(), 1)
        assert_equal(stack.minimum(), 1)
        stack.push(3)
        assert_equal(stack.peek(), 3)
        assert_equal(stack.minimum(), 1)
        stack.push(0)
        assert_equal(stack.peek(), 0)
        assert_equal(stack.minimum(), 0)

        print('Test: Pop on non-empty stack')
        assert_equal(stack.pop(), 0)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 3)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 1)
        assert_equal(stack.minimum(), 5)
        assert_equal(stack.pop(), 5)
        assert_equal(stack.minimum(), sys.maxsize)

        print('Test: Pop empty stack')
        assert_equal(stack.pop(), None)

        print('Success: test_stack_min')


def main():
    test = TestStackMin()
    test.test_stack_min()


if __name__ == '__main__':
    main()
