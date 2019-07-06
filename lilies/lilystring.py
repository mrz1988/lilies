# -*- coding: utf-8 -*-
from __future__ import print_function
from builtins import map
from builtins import str
from builtins import range
from builtins import object
from future.utils import string_types
from copy import deepcopy
import os
import re

from .base import LilyBase
from .colorama_shim import match_code as MATCH
from .colorama_shim import reset_code as RESET
from .colors import TextColor


# Mapping dictionary for unicode -> ascii.
UNI_TO_ASCII = {
    u"\u00c7": "C",
    u"\u00fc": "u",
    u"\u00e9": "e",
    u"\u00e2": "a",
    u"\u00e4": "a",
    u"\u00e0": "a",
    u"\u00e5": "a",
    u"\u00e7": "c",
    u"\u00ea": "e",
    u"\u00eb": "e",
    u"\u00e8": "e",
    u"\u00ef": "i",
    u"\u00ee": "i",
    u"\u00ec": "i",
    u"\u00c4": "A",
    u"\u00c5": "A",
    u"\u00c9": "E",
    u"\u00e6": "a",
    u"\u00c6": "A",
    u"\u00f4": "o",
    u"\u00f6": "o",
    u"\u00f2": "o",
    u"\u00fb": "u",
    u"\u00f9": "u",
    u"\u00ff": "y",
    u"\u00d6": "O",
    u"\u00dc": "U",
    u"\u00a2": "c",
    u"\u00a3": "p",
    u"\u00a5": "Y",
    u"\u20a7": "P",
    u"\u0192": "f",
    u"\u00e1": "a",
    u"\u00ed": "i",
    u"\u00f3": "o",
    u"\u00fa": "u",
    u"\u00f1": "n",
    u"\u00d1": "N",
    u"\u00aa": "*",
    u"\u00ba": "*",
    u"\u00bf": "?",
    u"\u2310": "~",
    u"\u00ac": "~",
    u"\u00a1": "i",
    u"\u00ab": "<",
    u"\u00bb": ">",
    u"\u2591": " ",
    u"\u2592": "#",
    u"\u2593": "#",
    u"\u2502": "|",
    u"\u2524": "|",
    u"\u2561": "|",
    u"\u2562": "|",
    u"\u2556": " ",
    u"\u2555": " ",
    u"\u2563": "|",
    u"\u2551": "|",
    u"\u2557": " ",
    u"\u255d": " ",
    u"\u255c": " ",
    u"\u255b": " ",
    u"\u2510": " ",
    u"\u2514": " ",
    u"\u2534": "-",
    u"\u252c": "-",
    u"\u251c": "|",
    u"\u2500": "-",
    u"\u253c": "+",
    u"\u255e": "|",
    u"\u255f": "|",
    u"\u255a": " ",
    u"\u2554": " ",
    u"\u2569": "=",
    u"\u2566": "=",
    u"\u2560": "|",
    u"\u2550": "=",
    u"\u256c": "=",
    u"\u2567": "=",
    u"\u2568": "-",
    u"\u2564": "=",
    u"\u2565": "-",
    u"\u2559": " ",
    u"\u2558": " ",
    u"\u2552": " ",
    u"\u2553": " ",
    u"\u256b": "+",
    u"\u256a": "=",
    u"\u2518": " ",
    u"\u250c": " ",
    u"\u2588": "*",
    u"\u2584": "*",
    u"\u258c": "*",
    u"\u2590": "*",
    u"\u2580": "*",
    u"\u25a0": "*",
}


def lstr(s, *args, **kwargs):
    if isinstance(s, LilyString):
        return s
    else:
        return LilyString(s, *args, **kwargs)


def _wlt(s):
    """
    For internal wilting.
    Used for better organization and avoiding circular imports
    """
    if isinstance(s, LilyBase):
        return s.wilt()
    return str(s)


def isstringish(obj):
    if issubclass(type(obj), LilyBase):
        # This is a hack, since for whatever reason
        # python considers LilyBase and LilyString to
        # both be instances of one another.
        return obj._isstringish()
    return isinstance(obj, (string_types,))


def assert_stringish(obj):
    if not isstringish(obj):
        raise TypeError("Expected something string-like: " + repr(obj))


class LilyString(LilyBase):
    def __init__(self, s="", color=""):
        self._pieces = []
        self._append(s, color)
        self.add = self._append

    def __str__(self):
        sb = ""
        for piece in self._pieces:
            sb += str(piece)
        return sb

    def __unicode__(self):
        sb = u""
        for piece in self._pieces:
            sb += str(piece)
        return sb

    def __repr__(self):
        return "c'" + self.__str__() + "'"

    def __len__(self):
        return sum(map(len, self._pieces))

    def __int__(self):
        return int(self.wilt())

    def __long__(self):
        return int(self.wilt())

    def __float__(self):
        return float(self.wilt())

    def __getitem__(self, key):
        if isinstance(key, slice):
            slice_obj = key
        elif isinstance(key, int):
            slice_obj = slice(key, key + 1, None)
        else:
            raise TypeError("Invalid argument type, looking for int or slice")

        return self._getslice(slice_obj)

    def __iter__(self):
        for p in self._pieces:
            color = p.get_color()
            for c in p.text:
                yield LilyString(c, color)

    def __add__(self, other):
        new_pretty = LilyString()
        try:
            newpieces = self._pieces + other._pieces
            new_pretty._pieces = newpieces
        except AttributeError:
            new_pretty._pieces = deepcopy(self._pieces)
            new_pretty._append(other)
        new_pretty._flatten()
        return new_pretty

    def __radd__(self, other):
        try:
            return other.__add__(self)
        except TypeError:
            return LilyString(other).__add__(self)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("can't multiply sequence by non-int")
        if other < 1:
            return LilyString()
        newpieces = self._pieces * other
        new_pretty = LilyString()
        new_pretty._pieces = newpieces
        new_pretty._flatten()
        return new_pretty

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        return self.wilt() > other

    def __lt__(self, other):
        return self.wilt() < other

    def __ge__(self, other):
        return self.wilt() >= other

    def __le__(self, other):
        return self.wilt() <= other

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())

    def __contains__(self, other):
        if not isstringish(other):
            other = repr(other)
            msg = other + " is not a required stringish object"
            raise TypeError(msg)
        if not isinstance(other, LilyString):
            return other in self.wilt()
        len_self = len(self)
        len_other = len(other)
        if len_other == 0:
            return True
        if len_other > len_self:
            return False
        if len_other == len_self:
            return other == self

        # basic substring search
        for i in range(len_self - len_other):
            for j in range(len_other):
                if self[i + j] != other[j]:
                    break
                if j == len_other - 1:
                    return True
        return False

    def __reversed__(self):
        revd = self[::-1]
        revd._flatten()
        return revd

    def wilt(self):
        sb = u""
        for piece in self._pieces:
            sb += piece.text
        return sb

    def _isstringish(self):
        return True

    def _isblockish(self):
        return False

    def is_text(self, text):
        return self.wilt() == _wlt(text)

    def isnt_text(self, text):
        return self.wilt() != _wlt(text)

    def resize(
        self,
        size,
        justify="left",
        fillchar=" ",
        l_fill_clr=MATCH,
        r_fill_clr=MATCH,
        add_elipsis=False,
        elipsis="..",
        elipsis_clr="",
    ):
        if self.__len__() <= size:
            return self._expand(
                size, justify, fillchar, l_fill_clr, r_fill_clr
            )
        else:
            return self._truncate(size, add_elipsis, elipsis, elipsis_clr)

    def _expand(
        self, width, justify, fillchar, l_fill_clr=MATCH, r_fill_clr=MATCH
    ):
        fillchar = self._check_fillchar(fillchar)
        left_color = self._match_and_validate_color(
            l_fill_clr, 0
        )  # 0 is leftmost char
        right_color = self._match_and_validate_color(
            r_fill_clr, -1
        )  # -1 is rightmost char
        cur_len = self.__len__()
        if cur_len == width:
            return deepcopy(self)

        padding = width - cur_len
        if justify == "left":
            return self._justify_left(padding, fillchar, right_color)
        elif justify == "right":
            return self._justify_right(padding, fillchar, left_color)
        elif justify == "center":
            return self._justify_center(
                padding, fillchar, left_color, right_color
            )
        else:
            raise InvalidInputError("unexpected value for justify")

    def _justify_left(self, width, fillchar, color):
        padding = LilyString(fillchar * width, color)
        return deepcopy(self) + padding

    def _justify_right(self, width, fillchar, color):
        padding = LilyString(fillchar * width, color)
        return padding + deepcopy(self)

    def _justify_center(self, width, fillchar, left_color, right_color):
        left_spaces = width // 2
        right_spaces = left_spaces + (width % 2)
        left = LilyString(fillchar * left_spaces, left_color)
        right = LilyString(fillchar * right_spaces, right_color)
        return left + deepcopy(self) + right

    @staticmethod
    def _check_fillchar(fillchar):
        if len(fillchar) > 1:
            raise TypeError("fillchar must be char, not str")
        if isinstance(fillchar, LilyString):
            return fillchar.wilt()
        return fillchar

    def _match_and_validate_color(self, color, index=None):
        if color == MATCH:
            if index is None:
                raise KeyError("color match attempted at invalid location")
            return self.get_color_at(index)
        return TextColor(color).name

    def ljust(self, width, fillchar=" ", fill_clr=MATCH):
        return self._expand(width, "left", fillchar, r_fill_clr=fill_clr)

    def rjust(self, width, fillchar=" ", fill_clr=MATCH):
        return self._expand(width, "right", fillchar, l_fill_clr=fill_clr)

    def center(self, width, fillchar=" ", l_fill_clr=MATCH, r_fill_clr=MATCH):
        return self._expand(width, "center", fillchar, l_fill_clr, r_fill_clr)

    def _truncate(self, length, add_elipsis, elipsis, elipsis_clr):
        new = deepcopy(self)
        trim_to_length = length - len(elipsis) if add_elipsis else length
        if trim_to_length < 1:
            raise LilyStringError(
                "Truncating string would " + "make it too short"
            )

        total = 0
        for i in range(len(new._pieces)):
            total += len(new._pieces[i].text)
            if total >= trim_to_length:
                new._pieces = new._pieces[: i + 1]
                break

        if total > trim_to_length:
            chars_to_cut = total - trim_to_length
            new._pieces[-1].text = new._pieces[-1].text[:-chars_to_cut]
        if not add_elipsis:
            return new

        # add elipsis, same color as last char
        color = self._match_and_validate_color(elipsis_clr, -1)
        return new + LilyString(elipsis, color)

    def _flatten(self):
        piece_length = len(self._pieces)
        if piece_length == 0:
            return
        newpieces = []
        for i in range(piece_length):
            if len(self._pieces[i]) == 0:
                continue
            if len(newpieces) == 0:
                newpieces.append(deepcopy(self._pieces[i]))
                continue
            if self._pieces[i].color == newpieces[-1].color:
                newpieces[-1].text += self._pieces[i].text
            else:
                newpieces.append(deepcopy(self._pieces[i]))
        self._pieces = newpieces

    def _getslice(self, sliceobj):
        chars = self.wilt()
        ixs = list(range(*sliceobj.indices(len(chars))))
        _new = LilyString()
        for i in ixs:
            _new += LilyString(chars[i], self.get_color_at(i))
        _new._flatten()
        return _new

    def color_char(self, index, *args, **kwargs):
        return self.color_chars([index], *args, **kwargs)

    def color_chars(self, indices, color_str=""):
        chars = self.wilt()
        ixs = sorted(indices)
        _new = LilyString()
        last_index = 0
        for i in ixs:
            if i >= len(chars):
                break
            _new += self[last_index:i]
            _new += LilyString(chars[i], color_str)
            last_index = i + 1
        _new += self[last_index:]
        _new._flatten()
        return _new

    def color_regex(self, pattern, color_str="", flags=0, num=0):
        chars = self.wilt()
        if num == 1:
            m = [re.match(pattern, chars, flags)]
        else:
            m = re.finditer(pattern, chars, flags)
            if num > 0:
                m = list(m)[:num]
        ixs = []
        for group in m:
            ixs += list(range(group.start(), group.end()))
        return self.color_chars(ixs, color_str)

    def _append(self, s, color_str=""):
        if s == "":
            return
        self._pieces.append(LilyStringPiece(s, TextColor(color_str)))

    def join(self, components):
        if not hasattr(components, "__iter__"):
            raise TypeError("can only join an iterable")
        if len(components) == 0:
            return LilyString()
        if len(components) == 1:
            s = components[0]
            if isinstance(s, LilyString):
                return s
            if isinstance(s, (string_types,)):
                return LilyString(s)
            raise TypeError("Was not a stringish type: " + repr(s))
        new_comps = components[0]
        copy = deepcopy(self)
        for i in range(1, len(components)):
            new_comps += copy + components[i]
        return new_comps

    def split(self, sep=None, maxsplit=-1):
        if isinstance(sep, LilyString):
            sep = sep.wilt()
        split_pieces = []
        # Split each string piece individually, storing resulting LilyString
        #   sets in split_pieces
        for piece in self._pieces:
            split_piece = piece.text.split(sep)
            piece_color = piece.get_color()
            if maxsplit != -1:
                # FIXME: bail earlier on this rather than re-splitting
                # everything
                prev_splits = sum([len(p) - 1 for p in split_pieces])
                tot_splits = len(split_piece) + prev_splits - 1
                if tot_splits > maxsplit:
                    split_times = maxsplit - prev_splits
                    split_piece = piece.text.split(sep, split_times)

            split_piece = [LilyString(p, piece_color) for p in split_piece]
            split_pieces.append(split_piece)

        if len(split_pieces) == 0:
            return [] if sep is None else [LilyString("")]

        output = split_pieces[0]
        for i in range(1, len(split_pieces)):
            # join together outside components (for output components that span
            #   multiple pieces)
            output[-1] += split_pieces[i][0]
            # add the rest of the pieces
            output += split_pieces[i][1:]
        return output

    def find(self, s, start=None, end=None):
        s = _wlt(s)
        return self.wilt().find(s, start, end)

    def rfind(self, s, start=None, end=None):
        s = _wlt(s)
        return self.wilt().rfind(s, start, end)

    def lower(self):
        _new = deepcopy(self)
        for i in range(len(self._pieces)):
            _new._pieces[i].text = _new._pieces[i].text.lower()
        return _new

    def upper(self):
        _new = deepcopy(self)
        for i in range(len(self._pieces)):
            _new._pieces[i].text = _new._pieces[i].text.upper()
        return _new

    def swapcase(self):
        new = deepcopy(self)
        for i in range(len(self._pieces)):
            new._pieces[i].text = new._pieces[i].text.swapcase()
        return new

    def lstrip(self, chars=None):
        new = deepcopy(self)
        if len(new._pieces) == 0:
            return new
        for i in range(len(new._pieces)):
            new._pieces[i].text = new._pieces[i].text.lstrip(chars)
            if len(new._pieces[i]) > 0:
                break
        new._flatten()
        return new

    def rstrip(self, chars=None):
        new = deepcopy(self)
        if len(new._pieces) == 0:
            return new
        for i in reversed(list(range(len(new._pieces)))):
            new._pieces[i].text = new._pieces[i].text.rstrip(chars)
            if len(new._pieces[i]) > 0:
                break
        new._flatten()
        return new

    def strip(self, chars=None):
        return self.lstrip(chars).rstrip(chars)

    def count(self, sub, *args, **kwargs):
        return self.wilt().count(_wlt(sub), *args, **kwargs)

    def startswith(self, prefix, *args, **kwargs):
        return self.wilt().startswith(_wlt(prefix), *args, **kwargs)

    def endswith(self, suffix, *args, **kwargs):
        return self.wilt().endswith(_wlt(suffix), *args, **kwargs)

    def isalnum(self):
        return self.wilt().isalnum()

    def isalpha(self):
        return self.wilt().isalpha()

    def isdigit(self):
        return self.wilt().isdigit()

    def islower(self):
        return self.wilt().islower()

    def isspace(self):
        return self.wilt().isspace()

    def istitle(self):
        return self.wilt().istitle()

    def isupper(self):
        return self.wilt().isupper()

    def get_color(self):
        if len(self._pieces) == 0:
            return TextColor().name
        return self._pieces[0].get_color()

    def get_color_at(self, index):
        if index < 0:
            index += self.__len__()
        if index >= self.__len__() or index < 0:
            return TextColor().name
        total = 0
        for p in self._pieces:
            total += len(p)
            if total > index:
                return p.get_color()

    def color(self, color_str):
        new = deepcopy(self)
        if len(self._pieces) == 0:
            return new
        text = self.wilt()
        new._pieces = [LilyStringPiece(text, TextColor(color_str))]
        return new


class LilyStringPiece(object):
    def __init__(self, s, color):
        try:
            self.text = str(s)
        except UnicodeDecodeError:
            self.text = s.decode("utf-8")
        self.color = color

    def __len__(self):
        return len(self.text)

    def __str__(self):
        return self.color_wrapped(self.text)

    def __unicode__(self):
        return self.color_wrapped(self.text)

    def color_wrapped(self, s):
        return self.color.ansi + str(s) + RESET

    def get_color(self):
        return self.color.name


class LilyStringError(Exception):
    pass


class InvalidInputError(Exception):
    pass


endl = LilyString(os.linesep)
