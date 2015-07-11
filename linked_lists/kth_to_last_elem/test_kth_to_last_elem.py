from nose.tools import assert_equal


class Test(object):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        assert_equal(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        assert_equal(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        assert_equal(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()