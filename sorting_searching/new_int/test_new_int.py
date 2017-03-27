from nose.tools import assert_equal, assert_raises


class TestBits(object):

    def test_new_int(self):
        bits = Bits()
        max_size = 32
        assert_raises(TypeError, bits.new_int, None, max_size)
        assert_raises(TypeError, bits.new_int, [], max_size)
        data = [item for item in range(30)]
        data.append(31)
        assert_equal(bits.new_int(data, max_size), 30)
        data = [item for item in range(32)]
        assert_equal(bits.new_int(data, max_size), None)
        print('Success: test_find_int_excluded_from_input')


def main():
    test = TestBits()
    test.test_new_int()


if __name__ == '__main__':
    main()