class ScoringEngineError(Exception):
    pass

class ParseError(ScoringEngineError):
    pass

class EventTypeError(ScoringEngineError):
    pass

class NormalizationError(ScoringEngineError):
    pass
