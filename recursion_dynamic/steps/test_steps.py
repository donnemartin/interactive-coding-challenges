from nose.tools import assert_equal, assert_raises


class TestSteps(object):

    def test_steps(self):
        steps = Steps()
        assert_raises(TypeError, steps.count_ways, None)
        assert_raises(TypeError, steps.count_ways, -1)
        assert_equal(steps.count_ways(0), 1)
        assert_equal(steps.count_ways(1), 1)
        assert_equal(steps.count_ways(2), 2)
        assert_equal(steps.count_ways(3), 4)
        assert_equal(steps.count_ways(4), 7)
        assert_equal(steps.count_ways(10), 274)
        print('Success: test_steps')


def main():
    test = TestSteps()
    test.test_steps()


if __name__ == '__main__':
    main()