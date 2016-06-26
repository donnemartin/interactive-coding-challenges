from nose.tools import assert_equal
from nose.tools import raises


class TestBstValidate(object):

    @raises(Exception)
    def test_bst_validate_empty(self):
        validate_bst(None)

    def test_bst_validate(self):
        node = Node(5)
        insert(node, 8)
        insert(node, 5)
        insert(node, 6)
        insert(node, 4)
        insert(node, 7)
        assert_equal(validate_bst(node), True)

        root = Node(5)
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        root.left = left
        root.right = right
        root.left.right = invalid
        assert_equal(validate_bst(root), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.test_bst_validate_empty()
    test.test_bst_validate()


if __name__ == '__main__':
    main()