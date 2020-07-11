import unittest


class TestMinHeap(unittest.TestCase):

    def test_min_heap(self):
        heap = MinHeap()
        self.assertEqual(heap.peek_min(), None)
        self.assertEqual(heap.extract_min(), None)
        heap.insert(20)
        self.assertEqual(heap.array[0], 20)
        heap.insert(5)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        heap.insert(15)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        heap.insert(22)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        self.assertEqual(heap.array[3], 22)
        heap.insert(40)
        self.assertEqual(heap.array[0], 5)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 15)
        self.assertEqual(heap.array[3], 22)
        self.assertEqual(heap.array[4], 40)
        heap.insert(3)
        self.assertEqual(heap.array[0], 3)
        self.assertEqual(heap.array[1], 20)
        self.assertEqual(heap.array[2], 5)
        self.assertEqual(heap.array[3], 22)
        self.assertEqual(heap.array[4], 40)
        self.assertEqual(heap.array[5], 15)
        mins = []
        while heap:
            mins.append(heap.extract_min())
        self.assertEqual(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')

        
def main():
    test = TestMinHeap()
    test.test_min_heap()

    
if __name__ == '__main__':
    main()
