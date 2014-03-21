#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lilies.lilystring import grow, wilt
from lilies.lilystring import PrettyPrinterError, InvalidInputError
import unittest
import math
import sys

if sys.version_info > (3, 0):
    long = int

class TestLilyString(unittest.TestCase):
    def setUp(self):
        self.integers = [0, 10, -4, 4325324, 32, -23412]
        self.floats = [1.234, math.pi, -32.4325, math.sqrt(2), 0.0]
        self.strings = ['', 'hello', '@#@!dsf%%', '3@\432', 'dfDfEEFdfaC', 'Mister John', 'mr. jOhn', "iSn't it", u'☃']
        self.longs = [long(123456754382390234),
                      long(3482713498573234),
                      long(-234897123123497999000)]
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
            self.assertEqual(lg, long(grow(lg)))
            self.assertEqual(lg, long(grow(lg, 'red')))
            
            as_string = str(lg)
            if len(as_string) > 1:
                multicolor = grow(as_string[0], 'cyan') + grow(as_string[1:], 'white')
                self.assertEqual(lg, long(multicolor))
                
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
            self.assertEqual(s * long(5), wilt(p * long(5)))
            
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
        with self.assertRaises(PrettyPrinterError):
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
    
    def test_get_set_color(self):
        for s in self.strings:
            p = grow(s)
            for c in self.colors:
                if len(s) > 0 and not c == '':
                    self.assertEqual(c, p.color(c).get_color())
                else:
                    self.assertEqual('default',
                                     p.color(c).get_color())
                
if __name__ == '__main__':
    unittest.main()
