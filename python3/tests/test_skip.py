import unittest


try:
    import mylib
except ImportError:
    mylib = None

class TestSkipped(unittest.TestCase):
    @unittest.skip("Don't run this")
    def test_fail(self):
        self.fail("This should not be run")

    @unittest.skipIf(mylib is None, "Mylib is not avaliable")
    def test_mylib(self):
        self.assertEqual(mylib.foobar(), 42)

    def test_skip_at_runtime(self):
        if True:
            self.skipTest("Finally I don't want to run it")
