import unittest


class TestCheckBalance(unittest.TestCase):

    def test_check_balance_empty(self):
        bst = BstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = BstBalance(Node(5))
        self.assertEqual(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        self.assertEqual(bst.check_balance(), True)

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        self.assertEqual(bst.check_balance(), False)

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        self.assertEqual(bst.check_balance(), True)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.assertRaises(TypeError, test.test_check_balance_empty)
    test.test_check_balance()


if __name__ == '__main__':
    main()
