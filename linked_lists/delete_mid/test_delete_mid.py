from nose.tools import assert_equal


class TestDeleteNode(object):

    def test_delete_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        assert_equal(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(1)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node2)
        assert_equal(linked_list.get_all_data(), [1, 3, 1])

        print('Success: test_delete_node')


def main():
    test = TestDeleteNode()
    test.test_delete_node()


if __name__ == '__main__':
    main()