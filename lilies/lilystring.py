# -*- coding: utf-8 -*-

################################################################################
# pretty.py (v0.0.1)
# By: Matt Zychowski (copyright 2014)
# License: MIT
# 
# A library wrapped around colorama for using colored strings in the terminal
# window.  Provides advanced manipulation of colored strings, including accurate
# slicing.
#
# Compatible with Python 2.7 (and probably 3.1?)
################################################################################

from __future__ import print_function
from copy import deepcopy
import os
import sys
import re

from .abstractions import Drawable
from .colorama_shim import match_code as MATCH
from .colorama_shim import reset_code as RESET
from .colors import TextColor

#Python 3 compatibility
if sys.version_info >= (3, 0):
    unicode = str
    IS_PY3 = True
else:
    IS_PY3 = False


SAMPLE1 = u'hello there! ☃?☃'
SAMPLE2 = 'hello there! ☃?☃'
SAMPLE3 = u'┌────q─────h☃ello───────────ds───┐'
TOTS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one',
        'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five',
        'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty',
        'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four',
        'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight',
        'thirty-nine', 'forty', 'forty-one', 'forty-two', 'forty-three',
        'forty-four', 'forty-five', 'forty-six', 'forty-seven', 'forty-eight',
        'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three']

# Mapping dictionary for unicode -> cp437.
# This can all be found at: http://en.wikipedia.org/wiki/Code_page_437
# We map chars 128-254 (255 is nbsp which we don't currently care about.)
# Some of the other control codes might be mapped eventually, since some of them
# are actually used to print cool characters in the windows DOS console.
UNI_TO_ASCII = {
    u'\u00c7' : 'C', u'\u00fc' : 'u', u'\u00e9' : 'e', u'\u00e2' : 'a',
    u'\u00e4' : 'a', u'\u00e0' : 'a', u'\u00e5' : 'a', u'\u00e7' : 'c',
    u'\u00ea' : 'e', u'\u00eb' : 'e', u'\u00e8' : 'e', u'\u00ef' : 'i',
    u'\u00ee' : 'i', u'\u00ec' : 'i', u'\u00c4' : 'A', u'\u00c5' : 'A',
    u'\u00c9' : 'E', u'\u00e6' : 'a', u'\u00c6' : 'A', u'\u00f4' : 'o',
    u'\u00f6' : 'o', u'\u00f2' : 'o', u'\u00fb' : 'u', u'\u00f9' : 'u',
    u'\u00ff' : 'y', u'\u00d6' : 'O', u'\u00dc' : 'U', u'\u00a2' : 'c',
    u'\u00a3' : 'p', u'\u00a5' : 'Y', u'\u20a7' : 'P', u'\u0192' : 'f',
    u'\u00e1' : 'a', u'\u00ed' : 'i', u'\u00f3' : 'o', u'\u00fa' : 'u',
    u'\u00f1' : 'n', u'\u00d1' : 'N', u'\u00aa' : '*', u'\u00ba' : '*',
    u'\u00bf' : '?', u'\u2310' : '~', u'\u00ac' : '~', u'\u00a1' : 'i',
    u'\u00ab' : '<', u'\u00bb' : '>', u'\u2591' : ' ', u'\u2592' : '#',
    u'\u2593' : '#', u'\u2502' : '|', u'\u2524' : '|', u'\u2561' : '|',
    u'\u2562' : '|', u'\u2556' : ' ', u'\u2555' : ' ', u'\u2563' : '|',
    u'\u2551' : '|', u'\u2557' : ' ', u'\u255d' : ' ', u'\u255c' : ' ',
    u'\u255b' : ' ', u'\u2510' : ' ', u'\u2514' : ' ', u'\u2534' : '-',
    u'\u252c' : '-', u'\u251c' : '|', u'\u2500' : '-', u'\u253c' : '+',
    u'\u255e' : '|', u'\u255f' : '|', u'\u255a' : ' ', u'\u2554' : ' ',
    u'\u2569' : '=', u'\u2566' : '=', u'\u2560' : '|', u'\u2550' : '=',
    u'\u256c' : '=', u'\u2567' : '=', u'\u2568' : '-', u'\u2564' : '=',
    u'\u2565' : '-', u'\u2559' : ' ', u'\u2558' : ' ', u'\u2552' : ' ',
    u'\u2553' : ' ', u'\u256b' : '+', u'\u256a' : '=', u'\u2518' : ' ',
    u'\u250c' : ' ', u'\u2588' : "*", u'\u2584' : "*", u'\u258c' : "*",
    u'\u2590' : "*", u'\u2580' : "*", u'\u25a0' : "*",
}

def wilt(s):
    if isinstance(s, LilyString):
        return s.u_plain()
    else:
        return unicode(s)

def grow(s, *args, **kwargs):
    if isinstance(s, LilyString):
        return s
    else:
        return LilyString(s, *args, **kwargs)

class LilyString(Drawable):
    def __init__(self, s='', color_str=''):
        self._pieces = []
        self.append(s, color_str)
        self.add = self.append

    def __str__(self):
        if IS_PY3:
            return self.__unicode__()
        sb = ''
        for piece in self._pieces:
            sb += str(piece)
        return sb

    def __unicode__(self):
        sb = u''
        for piece in self._pieces:
            sb += unicode(piece)
        return sb

    def __repr__(self):
        return "'" + self.__str__() + "'"

    def __len__(self):
        return sum(map(len, self._pieces))

    def __int__(self):
        return int(self.u_plain())

    def __long__(self):
        return long(self.u_plain())

    def __float__(self):
        return float(self.u_plain())

    def __getitem__(self, key):
        if isinstance(key, slice):
            slice_obj = key
        elif isinstance(key, int):
            slice_obj = slice(key, key+1, None)
        else:
            raise TypeError("Invalid argument type")

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
            new_pretty.append(other)

        return new_pretty

    def __radd__(self, other):
        try:
            return other.__add__(self)
        except TypeError:
            return LilyString(other).__add__(self)

    def __mul__(self, other):
        newpieces = self._pieces * other
        new_pretty = LilyString()
        new_pretty._pieces = newpieces
        return new_pretty

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iadd__(self, other):
        try:
            self._pieces += other._pieces
        except AttributeError:
            self.append(other)

        return self

    def __imul__(self, other):
        self._pieces *= other
        return self

    def u_plain(self):
        sb = u''
        for piece in self._pieces:
            sb += piece.text
        return sb

    def plain(self):
        sb = ''
        for piece in self._pieces:
            sb += piece.decoded()
        return sb

    def is_text(self, text):
        return self.u_plain() == text

    def isnt_text(self, text):
        return self.u_plain() != text

    def resize(self, size, justify='left', fillchar=' ',
               l_fill_clr=MATCH, r_fill_clr=MATCH, add_elipsis=False,
               elipsis='..', elipsis_clr=''):
        if self.__len__() <= size:
            return self._expand(size, justify, fillchar,
                                l_fill_clr, r_fill_clr)
        else:
            return self._truncate(size, add_elipsis, elipsis, elipsis_clr)

    def _expand(self, width, justify, fillchar, l_fill_clr=MATCH,
                r_fill_clr=MATCH):
        fillchar = self._check_fillchar(fillchar)
        left_color = self._match_and_validate_color(l_fill_clr, 0)   #0 is leftmost char
        right_color = self._match_and_validate_color(r_fill_clr, -1) #-1 is rightmost char
        cur_len = self.__len__()
        if cur_len == width:
            return deepcopy(self)

        padding = width - cur_len
        if justify == 'left':
            return self._justify_left(padding, fillchar, right_color)
        elif justify == 'right':
            return self._justify_right(padding, fillchar, left_color)
        elif justify == 'center':
            return self._justify_center(padding, fillchar,
                                        left_color, right_color)
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
            return fillchar.u_plain()
        return fillchar

    def _match_and_validate_color(self, color, index=None):
        if color == MATCH:
            if index is None:
                raise KeyError("color match attempted at invalid location")
            return self.get_color_at(index)
        return TextColor(color).name

    def ljust(self, width, fillchar=' ', fill_clr=MATCH):
        return self._expand(width, 'left', fillchar, r_fill_clr=fill_clr)

    def rjust(self, width, fillchar=' ', fill_clr=MATCH):
        return self._expand(width, 'right', fillchar, l_fill_clr=fill_clr)

    def center(self, width, fillchar=' ', l_fill_clr=MATCH, r_fill_clr=MATCH):
        return self._expand(width, 'center', fillchar, l_fill_clr, r_fill_clr)

    def _truncate(self, length, add_elipsis, elipsis, elipsis_clr):
        _new = deepcopy(self)
        trim_to_length = length - len(elipsis) if add_elipsis else length
        if trim_to_length < 1:
            raise PrettyPrinterError("Truncating string would " +\
                                     "make it too short")

        total = 0
        for i in range(len(_new._pieces)):
            total += len(_new._pieces[i].text)
            if total >= trim_to_length:
                _new._pieces = _new._pieces[:i+1]
                break

        if total > trim_to_length:
            chars_to_cut = total - trim_to_length
            _new._pieces[-1].text = _new._pieces[-1].text[: -chars_to_cut]
        if not add_elipsis:
            return _new

        # add elipsis
        color = self._match_and_validate_color(elipsis_clr, -1) #-1 is rightmost char
        return _new + LilyString(elipsis, color)

    def _flatten(self):
        if len(self._pieces) == 0:
            return
        _newpieces = [self._pieces[0]]
        for i in range(1, len(self._pieces)):
            if len(self._pieces[i]) == 0:
                continue
            if self._pieces[i].color == _newpieces[-1].color:
                _newpieces[-1].text += self._pieces[i].text
            else:
                _newpieces.append(self._pieces[i])
        self._pieces = _newpieces

    def _getslice(self, sliceobj):
        chars = self.u_plain()
        ixs = range(*sliceobj.indices(len(chars)))
        _new = LilyString()
        for i in ixs:
            _new += LilyString(chars[i], self.get_color_at(i))
        _new._flatten()
        return _new

    def color_chars(self, indices, color_str=''):
        chars = self.u_plain()
        ixs = sorted(indices)
        _new = LilyString()
        last_index = 0
        for i in ixs:
            if i >= len(chars):
                break
            _new += self[last_index:i]
            _new += LilyString(chars[i], color_str)
            last_index = i+1
        _new += self[last_index:]
        _new._flatten()
        return _new

    def color_regex(self, pattern, color_str='', flags=0, num=0):
        chars = self.u_plain()
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

    def append(self, s, color_str=''):
        if s == '':
            return
        self._pieces.append(LilyStringPiece(s, TextColor(color_str)))

    def concat(self, components):
        new_str = deepcopy(self)
        for component in components:
            new_str += component
        return new_str

    def join(self, components):
        if len(components) <= 1:
            return components
        new_comps = components[0]
        _copy = deepcopy(self)
        for i in range(1, len(components)):
            new_comps += _copy + components[i]
        return new_comps

    def find(self, s, start=None, end=None):
        s = wilt(s)
        return self.u_plain().find(s, start, end)

    def rfind(self, s, start=None, end=None):
        s = wilt(s)
        return self.u_plain().rfind(s, start, end)

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

    def lstrip(self, chars=None):
        _new = deepcopy(self)
        if len(_new._pieces) == 0:
            return _new
        for i in range(len(_new._pieces)):
            _new._pieces[i].text = _new._pieces[i].text.lstrip(chars)
            if len(_new._pieces[i]) > 0:
                break
        _new._flatten()
        return _new

    def rstrip(self, chars=None):
        _new = deepcopy(self)
        if len(_new._pieces) == 0:
            return _new
        for i in reversed(range(len(_new._pieces))):
            _new._pieces[i].text = _new._pieces[i].text.rstrip(chars)
            if len(_new._pieces[i]) > 0:
                break
        return _new

    def strip(self, chars=None):
        return self.lstrip(chars).rstrip(chars)

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
        _new = deepcopy(self)
        if len(self._pieces) == 0:
            return _new
        text = self.u_plain()
        _new._pieces = [LilyStringPiece(text, TextColor(color_str))]
        return _new

    #overrides for Drawable
    #TODO: enforce compatibility when newline characters are added
    def get_min_height(self):
        return 1

    def get_min_width(self):
        return len(self)

    def render(self):
        return [self]

class LilyStringPiece(object):
    def __init__(self, s, color):
        try:
            self.text = unicode(s)
        except UnicodeDecodeError:
            self.text = s.decode('utf-8')
        self.color = color

    def __len__(self):
        return len(self.text)

    def __str__(self):
        if IS_PY3:
            return self.__unicode__()
        return self.color_wrapped(self.decoded())

    def __unicode__(self):
        return self.color_wrapped(self.text)

    def color_wrapped(self, s):
        return self.color.ansi + s + RESET

    def get_color(self):
        return self.color.name

    def decoded(self):
        enc = sys.stdout.encoding
        if enc == 'cp65001':
            enc = 'utf-8'
        if enc == 'utf-8':
            return self.text.encode('utf-8')
        elif enc == 'ascii':
            fulls = ''
            last_bad = 0
            for i in range(len(self.text)):
                if self.text[i] in UNI_TO_ASCII:
                    if last_bad != i:
                        s = self.text[last_bad: i].encode('ascii', 'replace')
                        fulls += s
                    fulls += UNI_TO_ASCII[self.text[i]]
                    last_bad = i + 1
            if last_bad != len(self.text):
                fulls += self.text[last_bad : len(self.text)].encode('ascii',
                                                                     'replace')
            return fulls
        else:
            return self.text.encode(sys.stdout.encoding, 'replace')

class PrettyPrinterError(Exception):
    pass

class InvalidInputError(Exception):
    pass

endl = LilyString(os.linesep)
