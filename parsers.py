import csv
from custom_exceptions import ParseError

class Parser(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        raise NotImplementedError('Parse method does not implemented')


class CSVParser(Parser):
    def parse(self):
        with open(self.file_path, 'rb') as f:
            reader = csv.reader(f)
            rows = []
            try:
                for row in reader:
                    if len(row) != 3:
                        raise ParseError('No of column mismatch, expected 3 got %d' % len(row))
                    rows.append(row)
                return rows
            except csv.Error as e:
                raise ParseError(str(e))
