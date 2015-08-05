from nose.tools import assert_equal


class TestTreeLevelLists(object):

    def test_tree_level_lists(self):
        node = Node(5)
        insert(node, 3)
        insert(node, 8)
        insert(node, 2)
        insert(node, 4)
        insert(node, 1)
        insert(node, 7)
        insert(node, 6)
        insert(node, 9)
        insert(node, 10)
        insert(node, 11)

        levels = create_level_lists(node)
        results_list = []
        for level in levels:
            results = Results()
            for node in level:
                results.add_result(node)
            results_list.append(results)

        assert_equal(str(results_list[0]), '[5]')
        assert_equal(str(results_list[1]), '[3, 8]')
        assert_equal(str(results_list[2]), '[2, 4, 7, 9]')
        assert_equal(str(results_list[3]), '[1, 6, 10]')
        assert_equal(str(results_list[4]), '[11]')

        print('Success: test_tree_level_lists')


def main():
    test = TestTreeLevelLists()
    test.test_tree_level_lists()


if __name__ == '__main__':
    main()