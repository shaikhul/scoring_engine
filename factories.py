from events import WebEvent, EmailEvent, SocialEvent, WebinarEvent
from custom_exceptions import EventTypeError

event_map = {
    WebEvent.event_type: WebEvent,
    EmailEvent.event_type: EmailEvent,
    SocialEvent.event_type: SocialEvent,
    WebinarEvent.event_type: WebinarEvent
}

class EventFactory(object):

    @classmethod
    def create(cls, event_type, score):
        try:
            return event_map[event_type](score)
        except KeyError as e:
            raise EventTypeError('No Event found of type %s' % event_type)
