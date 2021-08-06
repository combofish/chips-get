import unittest


class Testme(unittest.TestCase):
    def setUp(self):
        self.list = [1,2,3]

    def test_length(self):
        self.list.append(4)
        self.assertEqual(len(self.list), 4)

    def test_has_one(self):
        self.assertEqual(len(self.list), 3)
        self.assertIn(1, self.list)


