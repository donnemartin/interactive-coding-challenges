from random import randint
from nose.tools import assert_equal


class TestSortStack(object):
    
    def get_sorted_stack(self, numbers):
        stack = MyStack()
        for x in numbers:
            stack.push(x)
        sorted_stack = stack.sort()
        return sorted_stack

    def test_sort_stack(self):
        print('Test: Empty stack')
        sorted_stack = self.get_sorted_stack([])
        assert_equal(sorted_stack.pop(), None)

        print('Test: One element stack')
        sorted_stack = self.get_sorted_stack([1])
        assert_equal(sorted_stack.pop(), 1)

        print('Test: Two or more element stack (general case)')
        num_items = 10
        numbers = [randint(0, 10) for x in xrange(num_items)]
        sorted_stack = self.get_sorted_stack(numbers)
        sorted_numbers = []
        for _ in xrange(num_items):
            sorted_numbers.append(sorted_stack.pop())
        assert_equal(sorted_numbers, sorted(numbers, reverse=True))
        
        print('Success: test_sort_stack')

def main():
    test = TestSortStack()
    test.test_sort_stack()

if __name__ == '__main__':
    main()