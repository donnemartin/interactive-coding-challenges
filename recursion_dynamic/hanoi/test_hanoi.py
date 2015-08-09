from nose.tools import assert_equal


class TestHanoi(object):

    def test_hanoi(self):
        num_disks = 3
        src = Stack()
        buff = Stack()
        dest = Stack()

        print('Test: None towers')
        hanoi(num_disks, None, None, None)

        print('Test: 0 disks')
        hanoi(num_disks, src, dest, buff)
        assert_equal(dest.pop(), None)

        print('Test: 1 disk')
        src.push(5)
        hanoi(num_disks, src, dest, buff)
        assert_equal(dest.pop(), 5)

        print('Test: 2 or more disks')
        for i in range(num_disks, -1, -1):
            src.push(i)
        hanoi(num_disks, src, dest, buff)
        for i in range(0, num_disks):
            assert_equal(dest.pop(), i)

        print('Success: test_hanoi')


def main():
    test = TestHanoi()
    test.test_hanoi()


if __name__ == '__main__':
    main()