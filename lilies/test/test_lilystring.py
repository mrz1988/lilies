#!/usr/bin/env python
# -*- coding: utf-8 -*-
from builtins import str
from builtins import range
import unittest
import math
import sys
from ..helpers import grow, wilt
from ..lilystring import LilyStringError, InvalidInputError, LilyStringPiece

class TestLilyString(unittest.TestCase):
    def setUp(self):
        self.integers = [0, 10, -4, 4325324, 32, -23412]
        self.floats = [1.234, math.pi, -32.4325, math.sqrt(2), 0.0]
        self.strings = ['',
                        'hello',
                        '@#@!dsf%%',
                        '3@\432',
                        'dfDfEEFdfaC',
                        'Mister John',
                        'mr. jOhn',
                        "iSn't it",
                        u'☃',
                        'comma,separated,values'
                        'trailing,comma,'
                        ',']
        self.longs = [int(123456754382390234),
                      int(3482713498573234),
                      int(-234897123123497999000)]
        self.colors = ['red', 'red on white', 'black on red', 'cyan on blue', 'yellow on yellow',
                       'default on default', 'default', 'gray on black', 'magenta on cyan',
                       'green on green', 'cyan on magenta', '', 'dark red', 'dark blue on black',
                       'dark yellow on green', 'dark cyan', 'dark magenta', 'dark green',
                       'bright magenta', 'bright red', 'bright blue', 'bright green', 'bright cyan',
                       'bright yellow']

    def test_integer_casting(self):
        for i in self.integers:
            self.assertEqual(i, int(grow(i)))
            self.assertEqual(i, int(grow(i, 'red')))

            as_string = str(i)
            if len(as_string) > 1:
                multicolor = grow(as_string[0], 'cyan') + grow(as_string[1:], 'white')
                self.assertEqual(i, int(multicolor))

    def test_float_casting(self):
        for i in self.floats:
            #python reduces float precision on string casting.
            #this makes sure we're the same as str()
            as_string = str(i)
            original = float(as_string)

            self.assertEqual(original, float(grow(i)))
            self.assertEqual(original, float(grow(i, 'red')))

            if len(as_string) > 1:
                multicolor = grow(as_string[0], 'cyan') + grow(as_string[1:], 'white')
                self.assertEqual(original, float(multicolor))

    def test_string_casting(self):
        for s in self.strings:
            self.assertEqual(s, wilt(grow(s)))
            self.assertEqual(s, wilt(grow(s, 'red')))

            if len(s) > 1:
                multicolor = grow(s[0], 'cyan') + grow(s[1:], 'white')
                self.assertEqual(s, wilt(multicolor))

    def test_long_casting(self):
        for lg in self.longs:
            self.assertEqual(lg, int(grow(lg)))
            self.assertEqual(lg, int(grow(lg, 'red')))

            as_string = str(lg)
            if len(as_string) > 1:
                multicolor = grow(as_string[0], 'cyan') + grow(as_string[1:], 'white')
                self.assertEqual(lg, int(multicolor))

    def test_length(self):
        for s in self.strings:
            self.assertEqual(len(s), len(grow(s)))
            self.assertEqual(len(s), len(grow(s, 'red')))

            if len(s) > 1:
                multicolor = grow(s[0], 'cyan') + grow(s[1:], 'white')
                self.assertEqual(len(s), len(multicolor))

    def test_addition(self):
        for s1 in self.strings:
            for s2 in self.strings:
                ps1 = grow(s1, 'red')
                ps2 = grow(s2, 'blue')

                original = s1 + s2
                both = ps1 + ps2
                right = s1 + ps2
                left = ps1 + s2

                self.assertEqual(original, wilt(both))
                self.assertEqual(original, wilt(right))
                self.assertEqual(original, wilt(left))

                self.assertEqual(str(ps1) + str(ps2), str(both))

    def test_multiplication(self):
        for s in self.strings:
            p = grow(s, 'blue')
            self.assertEqual(s * 0, wilt(p * 0))
            self.assertEqual(s * 3, wilt(p * 3))
            self.assertEqual(s * int(5), wilt(p * int(5)))

            with self.assertRaises(TypeError):
                p *= 1.4
            with self.assertRaises(TypeError):
                p = p * None
            with self.assertRaises(TypeError):
                p *= '3'

    def test_ljust(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s.ljust(2),
                             wilt(p.ljust(2)))

            self.assertEqual(s.ljust(40),
                             wilt(p.ljust(40)))

            self.assertEqual(s.ljust(40, 'a'),
                             wilt(p.ljust(40, 'a')))

            self.assertEqual(s.ljust(40, 'a'),
                             wilt(p.ljust(40, grow('a', 'blue'))))

            # Test that multi-char fill strings are not allowed
            with self.assertRaises(TypeError):
                p.ljust(40, 'multi')
            with self.assertRaises(TypeError):
                p.ljust(40, grow('multi', 'blue'))

    def test_rjust(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s.rjust(2),
                             wilt(p.rjust(2)))

            self.assertEqual(s.rjust(40),
                             wilt(p.rjust(40)))

            self.assertEqual(s.rjust(40, 'a'),
                             wilt(p.rjust(40, 'a')))

            self.assertEqual(s.rjust(40, 'a'),
                             wilt(p.rjust(40, grow('a', 'blue'))))

            # Test that multi-char fill strings are not allowed
            with self.assertRaises(TypeError):
                p.rjust(40, 'multi')
            with self.assertRaises(TypeError):
                p.rjust(40, grow('multi', 'blue'))

    def test_center(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s.center(2),
                             wilt(p.center(2)))

            self.assertEqual(s.center(40),
                             wilt(p.center(40)))

            self.assertEqual(s.center(40, 'a'),
                             wilt(p.center(40, 'a')))

            self.assertEqual(s.center(40, 'a'),
                             wilt(p.center(40, grow('a', 'blue'))))

            # Test that multi-char fill strings are not allowed
            with self.assertRaises(TypeError):
                p.center(40, 'multi')
            with self.assertRaises(TypeError):
                p.center(40, grow('multi', 'blue'))

    def test_resize(self):
        one = '12345678901234567890'
        one_at_10chars_no_elipsis = one[:10]
        one_at_10chars_w_elipsis = one[:8] + '..'
        one_at_40chars_left = one + (' ' * 20)
        one_at_40chars_right = (' ' * 20) + one
        one_at_40chars_center = (' ' * 10) + one + (' ' * 10)

        p_one = grow(one, 'red')
        self.assertEqual(one, wilt(p_one.resize(20)))
        self.assertEqual(one, wilt(p_one.resize(20, justify='center')))
        self.assertEqual(one, wilt(p_one.resize(20, add_elipsis=True)))
        self.assertEqual(one_at_10chars_no_elipsis,
                         wilt(p_one.resize(10)))
        self.assertEqual(one_at_10chars_w_elipsis,
                         wilt(p_one.resize(10, add_elipsis=True)))
        self.assertEqual(one_at_40chars_left,
                         wilt(p_one.resize(40, justify='left')))
        self.assertEqual(one_at_40chars_right,
                         wilt(p_one.resize(40, justify='right')))
        self.assertEqual(one_at_40chars_center,
                         wilt(p_one.resize(40, justify='center')))

        # test garbage justification throws error
        with self.assertRaises(InvalidInputError):
            p_one.resize(40, justify='garbage')

        # test garbage left fill color throws error
        with self.assertRaises(KeyError):
            p_one.resize(40, justify='center', l_fill_clr='garbage')

        # test garbage right fill color throws error
        with self.assertRaises(KeyError):
            p_one.resize(40, justify='center', r_fill_clr='garbage')

        # test garbage elipsis color throws error
        with self.assertRaises(KeyError):
            p_one.resize(10, elipsis_clr='garbage', add_elipsis=True)

        # test making too short causes error
        with self.assertRaises(LilyStringError):
            p_one.resize(1, add_elipsis=True)

    def test_iter(self):
        for s in self.strings:
            p = grow(s, 'red')
            index = 0
            for ch in p:
                self.assertEqual(s[index], wilt(ch))
                self.assertEqual('red', ch.get_color())
                index += 1

    def test_slicing(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s[0:5], wilt(p[0:5]))
            self.assertEqual(s[::-1], wilt(p[::-1]))
            self.assertEqual(s[2:7], wilt(p[2:7]))
            self.assertEqual(s[:-2], wilt(p[:-2]))
            self.assertEqual(s[3:], wilt(p[3:]))
            self.assertEqual(s[456:], wilt(p[456:]))
            self.assertEqual(s[1:5:2], wilt(p[1:5:2]))

    def test_strip(self):
        for s in self.strings:
            test_str = "    " + s + "  "
            test_grow = grow(test_str, 'red')

            self.assertEqual(test_str.lstrip(), wilt(test_grow.lstrip()))
            self.assertEqual(test_str.rstrip(), wilt(test_grow.rstrip()))
            self.assertEqual(test_str.strip(), wilt(test_grow.strip()))

    def test_strip_with_chars(self):
        test_input = '  xyyabcdxyyy'
        control1 = '  xyyabcd'
        control2 = 'abcd'
        test1 = grow(test_input, 'red').strip('xy')
        test2 = grow(test_input, 'red').strip('xy ')
        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))

    def test_wilt(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s, wilt(p))
            self.assertEqual(wilt(s), wilt(p))

    def test_upper(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s.upper(), wilt(p.upper()))

    def test_lower(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s.lower(), wilt(p.lower()))

    def test_swapcase(self):
        for s in self.strings:
            p = grow(s, 'red')
            self.assertEqual(s.swapcase(), wilt(p.swapcase()))

    def test_get_set_color(self):
        for s in self.strings:
            p = grow(s)
            for c in self.colors:
                if len(s) > 0 and not c == '':
                    self.assertEqual(c, p.color(c).get_color())
                else:
                    self.assertEqual('default',
                                     p.color(c).get_color())

    def test_flatten_combines_empty_strings(self):
        s = grow('', 'red')
        s._pieces.append(LilyStringPiece('', 'blue'))
        s._pieces.append(LilyStringPiece('', 'green'))
        self.assertEqual(2, len(s._pieces))
        s._flatten()
        self.assertEqual(0, len(s._pieces))

    def test_flatten_combines_colors(self):
        s = grow('hello', 'blue')
        s._append('world', 'blue')
        s._append('!', 'blue')
        self.assertEqual(3, len(s._pieces))
        len_before = len(s)
        s._flatten()
        self.assertEqual(1, len(s._pieces))
        self.assertEqual(len_before, len(s))

    def test_flatten_does_not_combine_unlike_colors(self):
        s = grow('hello', 'green')
        s._append('world', 'blue')
        s._append('!', 'green')
        self.assertEqual(3, len(s._pieces))
        len_before = len(s)
        s._flatten()
        self.assertEqual(3, len(s._pieces))
        self.assertEqual(len_before, len(s))

    def test_split_comma(self):
        for s in self.strings:
            p = grow(s, 'red')
            control = s.split(',')
            test = p.split(',')
            self.assertEqual(len(control), len(test))
            for i in range(len(control)):
                self.assertEqual(control[i], wilt(test[i]))

    def test_split(self):
        for s in self.strings:
            p = grow(s, 'red')
            control = s.split()
            test = p.split()
            self.assertEqual(len(control), len(test))
            for i in range(len(control)):
                self.assertEqual(control[i], wilt(test[i]))

    def test_join_on_bad_input(self):
        with self.assertRaises(TypeError):
            grow(',').join(5)

    def test_join_on_empty_str(self):
        control = ''.join(self.strings)
        test = wilt(grow('').join(self.strings))
        self.assertEqual(control, test)

    def test_join_on_commas(self):
        control = ','.join(self.strings)
        test = wilt(grow(',').join(self.strings))
        self.assertEqual(control, test)

    def test_join_nothing(self):
        control = ','.join([])
        test = wilt(grow(',').join([]))
        self.assertEqual(control, test)

    def test_join_single_str(self):
        control = ','.join(["hey"])
        test = wilt(grow(',').join(["hey"]))
        self.assertEqual(control, test)

    def test_join_single_lily(self):
        control = ','.join(["hey"])
        test = wilt(grow(',').join([grow("hey")]))
        self.assertEqual(control, test)

    def test_iadd(self):
        # checking that this behaves almost like
        # strings assign by value
        control1 = 'a'
        control2 = 'b'
        control1 = control2

        test1 = grow('a')
        test2 = grow('b')
        test1 = test2

        control1 += 'hey'
        test1 += grow('hey')

        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))

    def test_imul(self):
        # checking that this behaves almost like
        # strings assign by value
        control1 = 'a'
        control2 = 'b'
        control1 = control2

        test1 = grow('a')
        test2 = grow('b')
        test1 = test2

        control1 *= 3
        test1 *= 3

        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))

    def test_reverse(self):
        for s in self.strings:
            p = grow(s, 'green')
            control = "".join(reversed(s))
            test = grow('').join(reversed(p))
            self.assertEqual(control, wilt(test))

    def test_contains_handles_bad_input(self):
        p = grow("hello, world!", 'red')
        with self.assertRaises(TypeError):
            temp = 0 in p
        with self.assertRaises(TypeError):
            temp = 1.2 in p
        with self.assertRaises(TypeError):
            temp = [] in p
        with self.assertRaises(TypeError):
            temp = None in p
        with self.assertRaises(TypeError):
            temp = {} in p

    def test_contains_works_with_python_strings(self):
        p = grow("hello, world!", 'red')
        self.assertTrue('e' in p)
        self.assertTrue('llo' in p)
        self.assertFalse('p' in p)
        self.assertFalse('llo ' in p)

    def test_contains_works_with_lilystrings(self):
        p = grow("hello, ", 'red') + grow("world!", 'blue')
        self.assertTrue(grow('e', 'red') in p)
        self.assertTrue(grow('llo', 'red') in p)

    def test_contains_with_lilystrings_fails_on_wrong_color(self):
        p = grow("hello, ", 'red') + grow("world!", 'blue')
        self.assertFalse(grow('e', 'blue') in p)
        self.assertFalse(grow('llo', 'blue') in p)

    def test_contains_with_lilystrings_works_with_mixed_colors(self):
        p = grow("hello, ", 'red') + grow("world!", 'blue')
        should_match = grow('o, ', 'red') + grow('wo', 'blue')
        shouldnt_match = grow('o, wo', 'red')
        self.assertTrue(should_match in p)
        self.assertFalse(shouldnt_match in p)

    def test_contains_works_with_full_string(self):
        p1 = grow("hello, ", 'red') + grow("world!", 'blue')
        p2 = grow("hello, ", 'red') + grow("world!", 'blue')
        self.assertTrue(p1 in p2)
        self.assertTrue(wilt(p1) in p2)

    def test_contains_works_with_empty_string(self):
        p = grow("hello, ", 'red') + grow("world!", 'blue')
        self.assertTrue(grow('') in p)
        self.assertTrue('' in p)

def main():
    unittest.main()


if __name__ == '__main__':
    main()