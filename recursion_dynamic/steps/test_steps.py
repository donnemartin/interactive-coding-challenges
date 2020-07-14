import unittest


class TestSteps(unittest.TestCase):

    def test_steps(self):
        steps = Steps()
        self.assertRaises(TypeError, steps.count_ways, None)
        self.assertRaises(TypeError, steps.count_ways, -1)
        self.assertEqual(steps.count_ways(0), 1)
        self.assertEqual(steps.count_ways(1), 1)
        self.assertEqual(steps.count_ways(2), 2)
        self.assertEqual(steps.count_ways(3), 4)
        self.assertEqual(steps.count_ways(4), 7)
        self.assertEqual(steps.count_ways(10), 274)
        print('Success: test_steps')


def main():
    test = TestSteps()
    test.test_steps()


if __name__ == '__main__':
    main()
