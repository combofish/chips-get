import unittest


class TestFail(unittest.TestCase):
    def test_range(self):
        for x in range(5):
            if x > 4 :
                self.fail("Range returned a too big value: %d" % x)

