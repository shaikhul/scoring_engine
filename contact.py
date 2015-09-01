from collections import defaultdict
from factories import EventFactory

class Contact(object):

    def __init__(self, contact_id):
        self._id = contact_id
        self.events = defaultdict(dict)
        self._normalized_score = None
        self._quartile_label = None

    def add_event(self, event_type, score):
        self.events[event_type] = EventFactory.create(event_type, score)

    def get_total_weighted_score(self):
        total = 0
        for _, event in self.events.iteritems():
            total += event.get_weighted_score()
        return total

    @property
    def normalized_score(self):
        return self._normalized_score

    @normalized_score.setter
    def normalized_score(self, score):
        self._normalized_score = score

    @property
    def quartile_label(self):
        return self._quartile_label

    @quartile_label.setter
    def quartile_label(self, label):
        self._quartile_label = label

    def __repr__(self):
        return '{id}, {label}, {score}'.format(id=self._id, label=self.quartile_label, score=self.normalized_score)
