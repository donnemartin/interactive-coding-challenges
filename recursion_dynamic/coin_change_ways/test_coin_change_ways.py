import unittest


class Challenge(unittest.TestCase):

    def test_coin_change_ways(self,solution):
        self.assertEqual(solution(0, [1, 2]), 0)
        self.assertEqual(solution(100, [1, 2, 3]), 884)
        self.assertEqual(solution(1000, range(1, 101)), 
                     15658181104580771094597751280645)
        print('Success: test_coin_change_ways')


def main():
    test = Challenge()
    test.test_coin_change_ways(change_ways)


if __name__ == '__main__':
    main()
