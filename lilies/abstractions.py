from builtins import object
import os
from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass

class Drawable(with_metaclass(ABCMeta, object)):
    @abstractmethod
    def get_min_height(self):
        raise NotImplementedError()

    @abstractmethod
    def get_min_width(self):
        raise NotImplementedError()

    @abstractmethod
    def render(self):
        raise NotImplementedError()

    @classmethod
    def __subclasshook__(cls, subclass):
        required = ["render", "get_min_height", "get_min_width"]
        for r in required:
            if not any(r in c.__dict__ for c in subclass.__mro__):
                return NotImplemented
        return True

def test_is_lily_obj(thing):
    if not issubclass(thing.__class__, Drawable):
        raise ValueError("Expected a lily object")