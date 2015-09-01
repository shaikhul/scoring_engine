import unittest
from factories import EventFactory

class TestEventFactory(unittest.TestCase):

    def test_create(self):
        event = EventFactory.create('web', 35)
        self.assertEqual(event.get_event_type(), 'web')
        self.assertEqual(event.score, 35)

    def test_exception(self):
        with self.assertRaises(Exception):
            EventFactory.create('unknown', 10)

if __name__ == '__main__':
    unittest.main()
