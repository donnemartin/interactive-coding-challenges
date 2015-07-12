
class TestSorted (object):

	def test_sorted(self):

		try:
			list_test1 = MyLinkedList()
			list_test1.append(1)
			list_test1.append(5)
			list_test1.append(8)
			list_test1.append(10)
			assert list_test1.is_sorted() == True

			list_test2 = MyLinkedList()
			list_test2.append(100)
			list_test2.append(21)
			list_test2.append(55)
			list_test2.append(82)
			assert list_test2.is_sorted() == False

			list_test3 = MyLinkedList()
			assert list_test3.is_sorted() == None

			print('success: is_sorted')
		except:
			print('failed test')


def Main():
	test = TestSorted()
	test.test_sorted()

if __name__ == '__main__':
	Main()