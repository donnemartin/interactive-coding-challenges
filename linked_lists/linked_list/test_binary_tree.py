
class TestTree(object):
    
    def testAllTree (self):
        myTree = BinaryTree()
        myTree2 = BinaryTree()
        for num in [50, 30, 70, 10, 40, 60, 80, 7, 25, 38]:
            myTree.insert(num)
        for i in range (1, 100, 10):
            myTree2.insert(i)

        try:
            print("Test: insert with the inOrder, postOrder, and preOrder function")
            assert myTree.printInOrder() == [7, 10, 25, 30, 38, 40, 50, 60, 70, 80]
            assert myTree2.printInOrder() == [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
            assert myTree.printPreOrder() == [50, 30, 10, 7, 25, 40, 38, 70, 60, 80]
            assert myTree2.printPreOrder() == [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
            assert myTree.printPostOrder() == [7, 25, 10, 38, 40, 30, 60, 80, 70, 50]
            assert myTree2.printPostOrder() == [91, 81, 71, 61, 51, 41, 31, 21, 11, 1]
            print("Success: insert, inOrder, postOrder, and preOrder")
        except:
            print("Test failed")
            
        try:
            print("Test: max and min nodes")
            assert myTree.maxNode() == 80
            assert myTree.minNode() == 7
            assert myTree2.maxNode() == 91
            assert myTree2.minNode() == 1
            print("Success: max and min nodes")
        except:
            print("Test failed")
            
        try:
            print("Test: delete")
            myTree.delete(7)
            assert myTree.printPreOrder() == [50, 30, 10, 25, 40, 38, 70, 60, 80]
            myTree.delete(25)
            assert myTree.printPostOrder() == [10, 38, 40, 30, 60, 80, 70, 50]
            myTree2.delete(31)
            assert myTree2.printInOrder() == [1, 11, 21, 41, 51, 61, 71, 81, 91]
            myTree2.delete(91)
            assert myTree2.printPostOrder() == [81, 71, 61, 51, 41, 21, 11, 1]
            print("Success: insert")
        except:
            print("Test failed")
            
def main():
    testing = TestTree()
    testing.testAllTree()
    
if __name__=='__main__':
    main()