from contact import Contact
from quartiles import Quartile
from custom_exceptions import NormalizationError, ParseError

def get_normalized_value(val, min, max):
    try:
        return int(round((val - min) * 100 / (max - min)))
    except ZeroDivisionError as e:
        raise NormalizationError('Normalization error: ' + str(e))


class ScoringEngine(object):
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.contacts = []
        self.scores = []

    def group_events_by_contact(self):
        contacts = {}
        for row in self.raw_data:
            try:
                contact_id = int(row[0].strip())
            except ValueError as e:
                raise ParseError('Parse Error: ' + str(e))

            event = row[1].strip()

            try:
                score = float(row[2].strip())
            except ValueError as e:
                raise ParseError('Parse Error: ' + str(e))

            contact = contacts.setdefault(contact_id, Contact(contact_id))
            contact.add_event(event, score)

        self.contacts = contacts

    def list_total_weighted_scores(self):
        if not self.contacts:
            self.group_events_by_contact()

        scores = []
        for _, contact in self.contacts.iteritems():
            scores.append(contact.get_total_weighted_score())
        self.scores = scores

    def normalize_scores(self):
        if not self.scores:
            self.list_total_weighted_scores()

        min_score = min(self.scores)
        max_score = max(self.scores)
        for _, contact in self.contacts.iteritems():
            contact.normalized_score = get_normalized_value(contact.get_total_weighted_score(), min_score, max_score)
            contact.quartile_label = Quartile.get_quartile(contact.normalized_score)

    def print_contacts(self):
        for _, contact in self.contacts.iteritems():
            print contact

    def process(self):
        self.group_events_by_contact()
        self.normalize_scores()
        self.print_contacts()


if __name__ == '__main__':
    print 'To run the scoring engine, please use main.py! <python main.py csv_file_path>'
