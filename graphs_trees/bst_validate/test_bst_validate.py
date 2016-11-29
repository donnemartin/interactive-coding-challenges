from nose.tools import assert_equal
from nose.tools import raises


class TestBstValidate(object):

    @raises(Exception)
    def test_bst_validate_empty(self):
        validate_bst(None)

    def test_bst_validate(self):
        bst = BstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        assert_equal(bst.validate(), True)

        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        assert_equal(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.test_bst_validate_empty()
    test.test_bst_validate()


if __name__ == '__main__':
    main()