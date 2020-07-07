import unittest


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        self.assertEqual(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        self.assertEqual(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


def main():
    test = TestPalindrome()
    test.test_palindrome()


if __name__ == '__main__':
    main()
