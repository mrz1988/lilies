from .exceptions import UnsupportedAttributeException
from .exceptions import UnsupportedColorException
from ..style.styles import Style
from ..style.colors import Color


class DefaultTerminal(object):
    """
    Default terminal with no colors at all
    """

    def __init__(self):
        self.supported_attrs = []
        self.supported_colors = [Color()]

    def configure_style(self, style):
        # "any color you like"
        return Style()

    def assert_compatible_stylediff(self, style_diff):
        if style_diff.fg is not None:
            self.assert_compatible_color(style_diff.fg)
        if style_diff.bg is not None:
            self.assert_compatible_color(style_diff.bg)
        self.assert_compatible_attrs(style_diff.attrs.keys())

    def assert_compatible_style(self, style):
        self.assert_compatible_color(style.fg)
        self.assert_compatible_color(style.bg)
        self.assert_compatible_attrs(style.attrs)

    def assert_compatible_color(self, color):
        if color not in self.supported_colors:
            msg = "color unsupported in this terminal: rgb{clr}".format(
                clr=color.rgb
            )
            raise UnsupportedColorException(msg)

    def assert_compatible_attrs(self, attrs):
        for attr in attrs:
            if attr not in self.supported_attrs:
                msg = "attr unsupported in this terminal: '{attr}'".format(
                    attr=attr
                )
                raise UnsupportedAttributeException(msg)

    def encode_sequence(self, style_diff):
        self.assert_compatible_stylediff(style_diff)
        return ""
