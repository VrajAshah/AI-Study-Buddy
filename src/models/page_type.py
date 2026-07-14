from enum import Enum 

class PageType(Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"
    MIXED = "MIXED"
    BLANK = "BLANK"
    UNKNOWN = "UNKNOWN"

class AnalysisStatus(Enum):
    NOT_ANALYZED = 1
    ANALYZED = 2
    FAILED = 3