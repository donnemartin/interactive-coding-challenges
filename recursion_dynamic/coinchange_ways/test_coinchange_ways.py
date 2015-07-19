from nose.tools import assert_equal


class Challenge(object):

    def test_coinchange_ways(self,solution):
        assert_equal(solution(0,2,[1,2]), 0)
        assert_equal(solution(100,3,[1,2,3]), 884)
        assert_equal(solution(1000,100,range(1,101)), 15658181104580771094597751280645)
        print('Success: test_coinchange_ways')


def main():
    test = Challenge()
    test.test_coinchange_ways(change_ways)


if __name__ == '__main__':
    main()