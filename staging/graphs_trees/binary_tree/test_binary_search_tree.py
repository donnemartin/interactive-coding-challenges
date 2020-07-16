import unittest

class TestBinaryTree(unittest.TestCase):

	def test_insert_traversals (self):
		myTree = BinaryTree()
		myTree2 = BinaryTree()
		for num in [50, 30, 70, 10, 40, 60, 80, 7, 25, 38]:
			myTree.insert(num)
		[myTree2.insert(num) for num in range (1, 100, 10)]

		print("Test: insert checking with in order traversal")
		expectVal = [7, 10, 25, 30, 38, 40, 50, 60, 70, 80]
		self.assertEqual(myTree.printInOrder(), expectVal)
		expectVal = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
		self.assertEqual(myTree2.printInOrder(), expectVal)

		print("Test: insert checking with post order traversal")
		expectVal = [7, 25, 10, 38, 40, 30, 60, 80, 70, 50]
		self.assertEqual(myTree.printPostOrder(), expectVal)
		expectVal = [91, 81, 71, 61, 51, 41, 31, 21, 11, 1]
		self.assertEqual(myTree2.printPostOrder(), expectVal)


		print("Test: insert checking with pre order traversal")
		expectVal = [50, 30, 10, 7, 25, 40, 38, 70, 60, 80]
		self.assertEqual(myTree.printPreOrder(), expectVal)
		expectVal = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
		self.assertEqual(myTree2.printPreOrder(), expectVal)


		print("Success: test_insert_traversals")

	def test_max_min_nodes (self):
		myTree = BinaryTree()
		myTree.insert(5)
		myTree.insert(1)
		myTree.insert(21)

		print("Test: max node")
		self.assertEqual(myTree.maxNode(), 21)
		myTree.insert(32)
		self.assertEqual(myTree.maxNode(), 32)

		print("Test: min node")
		self.assertEqual(myTree.minNode(), 1)

		print("Test: min node inserting negative number")
		myTree.insert(-10)
		self.assertEqual(myTree.minNode(), -10)

		print("Success: test_max_min_nodes")

	def test_delete (self):
		myTree = BinaryTree()
		myTree.insert(5)

		print("Test: delete")
		myTree.delete(5)
		self.assertEqual(myTree.treeIsEmpty(), True)
		
		print("Test: more complex deletions")
		[myTree.insert(x) for x in range(1, 5)]
		myTree.delete(2)
		self.assertEqual(myTree.root.rightChild.data, 3)
        
		print("Test: delete invalid value")
		self.assertEqual(myTree.delete(100), False)


		print("Success: test_delete")

def main():
    testing = TestBinaryTree()
    testing.test_insert_traversals()
    testing.test_max_min_nodes()
    testing.test_delete()
    
if __name__=='__main__':
    main()
