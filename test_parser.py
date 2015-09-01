import unittest
from parsers import CSVParser

class TestCSVParser(unittest.TestCase):

    def test_parse(self):
        parser = CSVParser('sample_data.csv')
        rows = parser.parse()
        self.assertTrue(len(rows) > 0)


if __name__ == '__main__':
    unittest.main()
