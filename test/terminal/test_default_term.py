import unittest
from lilies.style.colors import get, Color
from lilies.style.styles import StyleDiff, Style
from lilies.terminal.base import DefaultTerminal
from lilies.terminal.exceptions import (
    UnsupportedColorException,
    UnsupportedAttributeException,
)


class TestDefaultTerminal(unittest.TestCase):
    def setUp(self):
        self.term = DefaultTerminal()

    def test_fgcolors_are_configured_out(self):
        style = Style(get("red"))
        result = self.term.configure_style(style)
        self.assertEqual(Color(), result.fg)

    def test_bgcolors_are_configured_out(self):
        style = Style(bg=get("red"))
        result = self.term.configure_style(style)
        self.assertEqual(Color(), result.bg)

    def test_attrs_are_configured_out(self):
        style = Style(attrs=["bold", "underline"])
        result = self.term.configure_style(style)
        self.assertEqual([], result.attrs)

    def test_fgcolors_are_not_compatible_diffs(self):
        diff = StyleDiff(get("red"))
        with self.assertRaises(UnsupportedColorException):
            self.term.assert_compatible_stylediff(diff)

    def test_bgcolors_are_not_compatible_diffs(self):
        diff = StyleDiff(bg=get("red"))
        with self.assertRaises(UnsupportedColorException):
            self.term.assert_compatible_stylediff(diff)

    def test_true_attrs_are_not_compatible_diffs(self):
        diff = StyleDiff(attrs={"bold": True})
        with self.assertRaises(UnsupportedAttributeException):
            self.term.assert_compatible_stylediff(diff)

    def test_false_attrs_are_not_compatible_diffs(self):
        diff = StyleDiff(attrs={"bold": False})
        with self.assertRaises(UnsupportedAttributeException):
            self.term.assert_compatible_stylediff(diff)

    def test_fgcolors_are_not_compatible_styles(self):
        style = Style(get("red"))
        with self.assertRaises(UnsupportedColorException):
            self.term.assert_compatible_style(style)

    def test_bgcolors_are_not_compatible_styles(self):
        style = Style(bg=get("red"))
        with self.assertRaises(UnsupportedColorException):
            self.term.assert_compatible_style(style)

    def test_attrs_are_not_compatible_styles(self):
        style = Style(attrs=["bold"])
        with self.assertRaises(UnsupportedAttributeException):
            self.term.assert_compatible_style(style)

    def test_encode_sequence_fails_on_nonempty_diffs(self):
        diff = StyleDiff(attrs={"bold": False})
        with self.assertRaises(UnsupportedAttributeException):
            self.term.encode_sequence(diff)

    def test_encode_sequence_properly_returns_empty(self):
        self.assertEqual("", self.term.encode_sequence(StyleDiff()))
