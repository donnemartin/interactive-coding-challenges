from nose.tools import assert_equal


class TestMinHeap(object):

    def test_min_heap(self):
        heap = MinHeap()
        assert_equal(heap.peek_min(), None)
        assert_equal(heap.extract_min(), None)
        heap.insert(20)
        assert_equal(heap.array[0], 20)
        heap.insert(5)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        heap.insert(15)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 15)
        heap.insert(22)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 15)
        assert_equal(heap.array[3], 22)
        heap.insert(40)
        assert_equal(heap.array[0], 5)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 15)
        assert_equal(heap.array[3], 22)
        assert_equal(heap.array[4], 40)
        heap.insert(3)
        assert_equal(heap.array[0], 3)
        assert_equal(heap.array[1], 20)
        assert_equal(heap.array[2], 5)
        assert_equal(heap.array[3], 22)
        assert_equal(heap.array[4], 40)
        assert_equal(heap.array[5], 15)
        mins = []
        while heap:
            mins.append(heap.extract_min())
        assert_equal(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')

        
def main():
    test = TestMinHeap()
    test.test_min_heap()

    
if __name__ == '__main__':
    main()