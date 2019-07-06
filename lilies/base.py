from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass


class LilyBase(with_metaclass(ABCMeta, object)):
    @abstractmethod
    def wilt(self):
        raise NotImplementedError('wilt')

    @abstractmethod
    def _isstringish(self):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        required = ['wilt', '_isstringish']
        for r in required:
            if not any(r in c.__dict__ for c in subclass.__mro__):
                return NotImplemented
        return True