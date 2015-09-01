import unittest
from quartiles import Quartile

class TestQuartile(unittest.TestCase):

    def test_get_quartile(self):
        self.assertEqual(Quartile.get_quartile(0), Quartile.BRONZE)
        self.assertEqual(Quartile.get_quartile(24), Quartile.BRONZE)
        self.assertEqual(Quartile.get_quartile(49), Quartile.SILVER)
        self.assertEqual(Quartile.get_quartile(74), Quartile.GOLD)
        self.assertEqual(Quartile.get_quartile(99), Quartile.PLATINUM)
        self.assertEqual(Quartile.get_quartile(100), Quartile.PLATINUM)


if __name__ == '__main__':
    unittest.main()
