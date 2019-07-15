import unittest
from lilies.style.colors import get, Color
from lilies.style.styles import StyleDiff, Style
from lilies.terminal.ansi8 import (
    Ansi8Terminal,
    BLACK,
    RED,
    YELLOW,
    GREEN,
    CYAN,
    BLUE,
    PURPLE,
    GRAY,
)
from lilies.terminal.exceptions import (
    UnsupportedColorException,
    UnsupportedAttributeException,
)


class TestDefaultTerminal(unittest.TestCase):
    def setUp(self):
        self.term = Ansi8Terminal()

    def test_fg_colors_are_configured(self):
        style = Style(get("lightcoral"))
        result = self.term.configure_style(style)
        self.assertEqual(get("maroon"), result.fg)

    def test_bg_colors_are_configured(self):
        style = Style(bg=get("lightcoral"))
        result = self.term.configure_style(style)
        print(result.bg.rgb)
        self.assertEqual(get("maroon"), result.bg)

    def test_attrs_are_configured_out(self):
        style = Style(attrs=["bold", "underline"])
        result = self.term.configure_style(style)
        self.assertEqual([], result.attrs)

    def test_bad_fgcolors_are_incompatible(self):
        diff = StyleDiff(get("lightcoral"))
        with self.assertRaises(UnsupportedColorException):
            self.term.assert_compatible_stylediff(diff)

    def test_bad_bgcolors_are_incompatible(self):
        diff = StyleDiff(bg=get("lime"))
        with self.assertRaises(UnsupportedColorException):
            self.term.assert_compatible_stylediff(diff)

    def test_bad_true_attrs_are_incompatible(self):
        diff = StyleDiff(attrs={"bold": True})
        with self.assertRaises(UnsupportedAttributeException):
            self.term.assert_compatible_stylediff(diff)

    def test_bad_false_attrs_are_incompatible(self):
        diff = StyleDiff(attrs={"bold": False})
        with self.assertRaises(UnsupportedAttributeException):
            self.term.assert_compatible_stylediff(diff)

    def test_encode_sequence_fails_on_bad_colors(self):
        diff = StyleDiff(get("lime"))
        with self.assertRaises(UnsupportedColorException):
            self.term.encode_sequence(diff)

    def test_encode_sequence_fails_on_bad_attrs(self):
        diff = StyleDiff(attrs={"bold": False})
        with self.assertRaises(UnsupportedAttributeException):
            self.term.encode_sequence(diff)

    def test_encode_sequence_properly_encodes_fg(self):
        diff = StyleDiff(get("maroon"))
        result = self.term.encode_sequence(diff)
        expected = "\033[31m"
        self.assertEqual(expected, result)

    def test_encode_sequence_properly_encodes_bg(self):
        diff = StyleDiff(bg=get("maroon"))
        result = self.term.encode_sequence(diff)
        expected = "\033[41m"
        self.assertEqual(expected, result)

    def test_encode_sequence_properly_encodes_fgreset(self):
        diff = StyleDiff(Color())
        result = self.term.encode_sequence(diff)
        expected = "\033[39m"
        self.assertEqual(expected, result)

    def test_encode_sequence_properly_encodes_bgreset(self):
        diff = StyleDiff(bg=Color())
        result = self.term.encode_sequence(diff)
        expected = "\033[49m"
        self.assertEqual(expected, result)

    def test_encode_sequence_properly_encodes_multi(self):
        diff = StyleDiff(get("green"), bg=Color())
        result = self.term.encode_sequence(diff)
        expected = "\033[32m\033[49m"
        self.assertEqual(expected, result)

    def test_encode_sequence_encodes_all_fgcolors(self):
        colors = {
            BLACK: "\033[30m",
            RED: "\033[31m",
            YELLOW: "\033[33m",
            GREEN: "\033[32m",
            CYAN: "\033[36m",
            BLUE: "\033[34m",
            PURPLE: "\033[35m",
            GRAY: "\033[37m",
        }
        for color in colors:
            diff = StyleDiff(color)
            result = self.term.encode_sequence(diff)
            expected = colors[color]
            self.assertEqual(expected, result)

    def test_encode_sequence_encodes_all_bgcolors(self):
        colors = {
            BLACK: "\033[40m",
            RED: "\033[41m",
            YELLOW: "\033[43m",
            GREEN: "\033[42m",
            CYAN: "\033[46m",
            BLUE: "\033[44m",
            PURPLE: "\033[45m",
            GRAY: "\033[47m",
        }
        for color in colors:
            diff = StyleDiff(bg=color)
            result = self.term.encode_sequence(diff)
            expected = colors[color]
            self.assertEqual(expected, result)
