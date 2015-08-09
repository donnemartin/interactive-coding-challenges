from nose.tools import assert_equal


class Challenge(object):

    def test_coin_change_ways(self,solution):
        assert_equal(solution(0, [1, 2]), 0)
        assert_equal(solution(100, [1, 2, 3]), 884)
        assert_equal(solution(1000, range(1, 101)), 15658181104580771094597751280645)
        print('Success: test_coin_change_ways')


def main():
    test = Challenge()
    test.test_coin_change_ways(change_ways)


if __name__ == '__main__':
    main()