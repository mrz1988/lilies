import unittest
from lilies.style.colors import Color, get
from lilies.style.parse import parse_style, InvalidStyleException


class TestStyleParsing(unittest.TestCase):
    def test_fails_on_nonetype(self):
        with self.assertRaises(InvalidStyleException):
            parse_style(None)

    def test_fails_on_nonstrings(self):
        with self.assertRaises(InvalidStyleException):
            parse_style(10)
        with self.assertRaises(InvalidStyleException):
            parse_style(["list"])

    def test_fails_on_invalid_fgcolor(self):
        with self.assertRaises(InvalidStyleException):
            parse_style("invalid")

    def test_fails_on_invalid_bgcolor(self):
        with self.assertRaises(InvalidStyleException):
            parse_style("on invalid")

    def test_fails_on_invalid_only_attribute(self):
        with self.assertRaises(InvalidStyleException):
            parse_style("invalid red")

    def test_fails_on_invalid_middle_attribute(self):
        with self.assertRaises(InvalidStyleException):
            parse_style("bold, invalid red on blue")

    def test_fails_on_empty_middle_attribute(self):
        with self.assertRaises(InvalidStyleException):
            parse_style("bold, ,italic red on blue")

    def test_can_parse_fg_color(self):
        style = parse_style("red")
        self.assertEqual(get("red"), style.fg)
        self.assertEqual(Color(), style.bg)
        self.assertEqual([], style.attrs)

    def test_can_parse_bg_color(self):
        style = parse_style("on lime")
        self.assertEqual(Color(), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual([], style.attrs)

    def test_can_parse_single_attr(self):
        style = parse_style("bold")
        self.assertEqual(Color(), style.fg)
        self.assertEqual(Color(), style.bg)
        self.assertEqual(["bold"], style.attrs)

    def test_can_parse_multiple_attrs(self):
        style = parse_style("bold, italic")
        self.assertEqual(Color(), style.fg)
        self.assertEqual(Color(), style.bg)
        self.assertEqual(["bold", "italic"], style.attrs)

    def test_can_parse_fgbg_color(self):
        style = parse_style("rosybrown on lime")
        self.assertEqual(get("rosybrown"), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual([], style.attrs)

    def test_can_parse_fgbgattr(self):
        style = parse_style("underline rosybrown on lime")
        self.assertEqual(get("rosybrown"), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual(["underline"], style.attrs)

    def test_can_parse_multi_fgbgattr(self):
        style = parse_style("blink, underline rosybrown on lime")
        self.assertEqual(get("rosybrown"), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_can_parse_no_fg_color(self):
        style = parse_style("blink, underline on lime")
        self.assertEqual(Color(), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_clears_whitespace_in_fgcolors(self):
        style = parse_style("blink, underline deep sky blue1 on lime")
        self.assertEqual(get("deepskyblue1"), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_works_with_camelcase_fgcolors(self):
        style = parse_style("blink, underline deepSkyBlue1 on lime")
        self.assertEqual(get("deepskyblue1"), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_works_with_snakecase_fgcolors(self):
        style = parse_style("blink, underline deep_sky_blue1 on lime")
        self.assertEqual(get("deepskyblue1"), style.fg)
        self.assertEqual(get("lime"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_clears_whitespace_in_bgcolors(self):
        style = parse_style("blink, underline lime on deep sky blue1")
        self.assertEqual(get("lime"), style.fg)
        self.assertEqual(get("deepskyblue1"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_works_with_camelcase_bgcolors(self):
        style = parse_style("blink, underline lime on deepSkyBlue1")
        self.assertEqual(get("lime"), style.fg)
        self.assertEqual(get("deepskyblue1"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_works_with_snakecase_bgcolors(self):
        style = parse_style("blink, underline lime on deep_sky_blue1")
        self.assertEqual(get("lime"), style.fg)
        self.assertEqual(get("deepskyblue1"), style.bg)
        self.assertEqual(["blink", "underline"], style.attrs)

    def test_can_alias_attrs(self):
        style = parse_style("underlined, bright red on black")
        self.assertEqual(get("red"), style.fg)
        self.assertEqual(get("black"), style.bg)
        self.assertEqual(["underline", "bold"], style.attrs)
