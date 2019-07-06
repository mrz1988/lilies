from __future__ import print_function
import os
from builtins import str
from future.utils import string_types
from .base import LilyBase
from .lilyblock import LilyBlock
from .lilystring import LilyString


def wilt(s):
    if isinstance(s, LilyBase):
        return s.wilt()
    else:
        return str(s)


def grow(s, *args, **kwargs):
    if isinstance(s, LilyBase):
        return s
    elif isinstance(s, (string_types,)):
        if os.linesep in s:
            return LilyBlock(s, *args, **kwargs)
        return LilyString(s, *args, **kwargs)
    elif hasattr(s, '__iter__'):
        return LilyBlock(s, *args, **kwargs)
    else:
        return LilyString(s, *args, **kwargs)
