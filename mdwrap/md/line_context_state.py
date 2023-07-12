from enum import Enum, auto


class LineContextState(Enum):
    """Enum for the possible states of a LineContext."""

    AT_ROOT = auto()
    IN_MULTI_LINE_CODE_BLOCK = auto()
    IN_FONT_MATTER = auto()
    IN_TABLE = auto()