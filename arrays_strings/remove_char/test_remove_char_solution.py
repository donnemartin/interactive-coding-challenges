from nose.tools import assert_equal

class TestRemoveChar (object):
    def test_remove_char (self, func):
        assert_equal(func("", 'n'), None)
        assert_equal(func("panda", 'a'), "pnd")
        assert_equal(func("zOokeeper", 'o'), "zOkeeper")
        assert_equal(func("Susan", 's'), "Suan")
        print("Success: test_remove_char")
        
    def test_remove_char_recur (self, func):
        assert_equal(func("", 'n'), "")
        assert_equal(func("char", 'z'), "char")
        assert_equal(func("panda", 'A'), "panda")
        assert_equal(func("the moon", " "), "themoon")
        print("Success: test_remove_char_recur")
        
def main():
    test = TestRemoveChar()
    test.test_remove_char(remove_char)
    test.test_remove_char_recur(remove_char_recur)

if __name__=='__main__':
    main()