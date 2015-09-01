import unittest
from contact import Contact

class TestContact(unittest.TestCase):

    def setUp(self):
        self.contact = Contact(1)
        self.contact.add_event('web', 20)
        self.contact.add_event('email', 25)

    def test_get_total_weighted_score(self):
        total_score = (20 * 1) + (25 * 1.2)
        self.assertEqual(self.contact.get_total_weighted_score(), total_score)

    def test_normalized_score_property(self):
        self.contact.normalized_score = 10
        self.assertEqual(self.contact.normalized_score, 10)

    def test_quartile_label_property(self):
        self.contact.quartile_label = 'gold'
        self.assertEqual(self.contact.quartile_label, 'gold')


if __name__ == '__main__':
    unittest.main()
