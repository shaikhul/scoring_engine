import unittest
from scoring_engine import get_normalized_value, ScoringEngine
from custom_exceptions import NormalizationError
from quartiles import Quartile

class TestNormalization(unittest.TestCase):

    def test_get_normalized_value(self):
        min_val = 44.3
        max_val = 123.5

        self.assertEqual(get_normalized_value(44.3, min_val, max_val), 0)
        self.assertEqual(get_normalized_value(123.5, min_val, max_val), 100)
        self.assertEqual(get_normalized_value(0, -10.5, 135.5), int(round((0 + 10.5) * 100 / (135.5 + 10.5))))

        with self.assertRaises(NormalizationError):
            get_normalized_value(min_val, min_val, min_val)

class TestScoringEngine(unittest.TestCase):

    def setUp(self):
        self.raw_data = [
            ['1', 'web', '22.5'],
            ['1', 'social', '35.8'],
            ['2', 'web', '-10.5'],
            ['2', 'email', '55.2'],
            ['2', 'social', '88.5']
        ]

        self.scoring_engine = ScoringEngine(self.raw_data)

    def test_group_events_by_contact(self):
        self.scoring_engine.group_events_by_contact()

        self.assertEqual(len(self.scoring_engine.contacts), 2)
        self.assertEqual(len(self.scoring_engine.contacts[1].events), 2)
        self.assertEqual(len(self.scoring_engine.contacts[2].events), 3)

    def test_list_total_weighted_scores(self):
        self.scoring_engine.list_total_weighted_scores()

        self.assertEqual(len(self.scoring_engine.scores), 2)

    def test_normalize_scores(self):
        self.scoring_engine.normalize_scores()

        for _, contact in self.scoring_engine.contacts.iteritems():
            self.assertTrue(contact.normalized_score is not None)
            self.assertTrue(contact.quartile_label in Quartile.quartile_list)


if __name__ == '__main__':
    unittest.main()
