class Event(object):
    def __init__(self, score=0):
        self.score = score

    def get_weighted_score(self):
        return self.weight * self.score

    def get_event_type(self):
        return self.event_type


class WebEvent(Event):
    weight = 1.0
    event_type = 'web'


class EmailEvent(Event):
    weight = 1.2
    event_type = 'email'


class SocialEvent(Event):
    weight = 1.5
    event_type = 'social'


class WebinarEvent(Event):
    weight = 2.0
    event_type = 'webinar'
