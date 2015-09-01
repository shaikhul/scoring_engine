import unittest
from events import WebEvent, EmailEvent

class TestWebEvent(unittest.TestCase):

    def setUp(self):
        self.event = WebEvent(15.5)

    def test_get_weighted_score(self):
        weighted_score = self.event.score * self.event.weight
        self.assertEqual(self.event.get_weighted_score(), weighted_score)

    def test_get_event_type(self):
        self.assertEqual(self.event.get_event_type(), WebEvent.event_type)

if __name__ == '__main__':
    unittest.main()
