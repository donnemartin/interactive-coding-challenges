from nose.tools import assert_equal


class TestCheckBalance(object):

    def test_check_balance(self):
        node = Node(5)
        insert(node, 3)
        insert(node, 8)
        insert(node, 1)
        insert(node, 4)
        assert_equal(check_balance(node), True)

        node = Node(5)
        insert(node, 3)
        insert(node, 8)
        insert(node, 9)
        insert(node, 10)
        assert_equal(check_balance(node), False)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.test_check_balance()


if __name__ == '__main__':
    main()