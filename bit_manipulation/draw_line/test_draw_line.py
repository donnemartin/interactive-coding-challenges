from nose.tools import assert_equal


class TestBitsScreen(object):

    def test_draw_line(self):
        bits_screen = BitsScreen()
        screen = []
        for _ in range(20):
            screen.append(int('00000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=68, x2=80)
        assert_equal(screen[8], int('00001111', base=2))
        assert_equal(screen[9], int('11111111', base=2))
        assert_equal(screen[10], int('10000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=2, x2=6)
        assert_equal(screen[0], int('00111110', base=2))
        bits_screen.draw_line(screen, width=32, x1=10, x2=13)
        assert_equal(screen[1], int('00111100', base=2))
        print('Success: test_draw_line')


def main():
    test = TestBitsScreen()
    test.test_draw_line()


if __name__ == '__main__':
    main()