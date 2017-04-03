from nose.tools import assert_equal


class Challenge(object):

    def test_coin_change(self):
        coin_changer = CoinChanger()
        assert_equal(coin_changer.make_change([1, 2], 0), 0)
        assert_equal(coin_changer.make_change([1, 2, 3], 5), 5)
        assert_equal(coin_changer.make_change([1, 5, 25, 50], 10), 3)
        print('Success: test_coin_change')


def main():
    test = Challenge()
    test.test_coin_change()


if __name__ == '__main__':
    main()