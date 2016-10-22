from nose.tools import assert_equal


class TestFindLoopStart(object):

    def test_find_loop_start(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: One element')
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Two elements')
        linked_list.append(2)
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Three or more elements')
        linked_list.append(3)
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: General case: Circular linked list')
        node10 = Node(10)
        node9 = Node(9, node10)
        node8 = Node(8, node9)
        node7 = Node(7, node8)
        node6 = Node(6, node7)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node0 = Node(0, node1)
        node10.next = node3
        linked_list = MyLinkedList(node0)
        assert_equal(linked_list.find_loop_start(), node3)

        print('Success: test_find_loop_start')


def main():
    test = TestFindLoopStart()
    test.test_find_loop_start()


if __name__ == '__main__':
    main()