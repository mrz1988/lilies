import os
from future.utils import string_types
from .base import LilyBase
from .lilyblock import LilyBlock
from .lilystring import LilyString


def grow(s, *args, **kwargs):
    if isinstance(s, LilyBase):
        return s
    elif isinstance(s, (string_types,)):
        if os.linesep in s:
            return LilyBlock(s, *args, **kwargs)
        return LilyString(s, *args, **kwargs)
    elif hasattr(s, "__iter__"):
        return LilyBlock(s, *args, **kwargs)
    else:
        return LilyString(s, *args, **kwargs)
