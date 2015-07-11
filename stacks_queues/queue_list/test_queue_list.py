from nose.tools import assert_equal


class TestQueue(object):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Dequeue an empty queue')
        queue = Queue()
        assert_equal(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        assert_equal(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        assert_equal(queue.dequeue(), 2)
        assert_equal(queue.dequeue(), 3)
        assert_equal(queue.dequeue(), 4)

        print('Success: test_end_to_end')


def main():
    test = TestQueue()
    test.test_end_to_end()


if __name__ == '__main__':
    main()