import sys
import os

from scoring_engine import ScoringEngine
from parsers import CSVParser
from custom_exceptions import ParseError, ScoringEngineError

def run(csv_file_path):
    if not os.path.exists(csv_file_path) or os.path.isdir(csv_file_path):
        print 'Invalid file path given, please provide a valid csv file path'
        return

    parser = CSVParser(csv_file_path)
    try:
        raw_data = parser.parse()
    except ParseError as e:
        print 'Parse Error: ' + e
        return

    scoring_engine = ScoringEngine(raw_data)
    try:
        scoring_engine.process()
    except ScoringEngineError as e:
        print 'Exception occurred: ' + str(e)
        return
    except Exception as e:
        print 'Unknown Error: ' + str(e)
        return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'CSV file path required!'
        print 'Suggested pattern: <python main.py csv_file_path>'
        sys.exit(0)

    csv_file_path = sys.argv[1]
    run(csv_file_path)
