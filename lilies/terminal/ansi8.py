from .base import DefaultTerminal
from . import ansicodes
from .exceptions import UnsupportedColorException
from ..style.colors import get, Color
from ..style.styles import Style

BLACK = get("black")
RED = get("maroon")
GREEN = get("green")
YELLOW = get("olive")
BLUE = get("navy")
PURPLE = get("purple")
CYAN = get("teal")
GRAY = get("silver")


class Ansi8Terminal(DefaultTerminal):
    """
    An 8-color ansi terminal
    """

    def __init__(self):
        self.supported_colors = [
            Color(),
            BLACK,
            RED,
            GREEN,
            YELLOW,
            BLUE,
            PURPLE,
            CYAN,
            GRAY,
        ]
        self.supported_attrs = []

    def configure_style(self, style):
        """
        Configure the style for this terminal
        """
        if style.fg.isreset():
            fg = Color()
        else:
            fg = self._hsl_to_color(*style.fg.hsl)
        if style.bg.isreset():
            bg = Color()
        else:
            bg = self._hsl_to_color(*style.bg.hsl)

        def issupported(style):
            return style in self.supported_attrs

        attrs = filter(issupported, style.attrs)
        return Style(fg, bg, attrs)

    def encode_sequence(self, style_diff):
        self.assert_compatible_stylediff(style_diff)
        fg_code = self._fg_code(style_diff.fg)
        bg_code = self._bg_code(style_diff.bg)
        attr_code = self._attr_code(style_diff.attrs)
        fg_char = ansicodes.esc(fg_code)
        bg_char = ansicodes.esc(bg_code)
        attr_char = ansicodes.esc(attr_code)
        return attr_char + fg_char + bg_char

    def _fg_code(self, fg_color):
        if fg_color is None:
            return None

        if fg_color.isreset():
            return ansicodes.NOCOLOR

        if fg_color == BLACK:
            return ansicodes.BLACK
        elif fg_color == RED:
            return ansicodes.RED
        elif fg_color == GREEN:
            return ansicodes.GREEN
        elif fg_color == YELLOW:
            return ansicodes.YELLOW
        elif fg_color == BLUE:
            return ansicodes.BLUE
        elif fg_color == PURPLE:
            return ansicodes.MAGENTA
        elif fg_color == CYAN:
            return ansicodes.CYAN
        elif fg_color == GRAY:
            return ansicodes.LIGHTGRAY
        else:
            raise UnsupportedColorException()

    def _bg_code(self, bg_color):
        return ansicodes.fg_to_bg(self._fg_code(bg_color))

    def _attr_code(self, attrs):
        return None

    def _hsl_to_color(self, h, s, l):
        # grayscale, low saturation
        if s < 10:
            return BLACK if l < 20 else GRAY

        # higher saturation, go by hue
        if h < 30 or h > 345:
            return RED
        if h < 65:
            return YELLOW
        if h < 145:
            return GREEN
        if h < 215:
            return CYAN
        if h < 260:
            return BLUE
        return PURPLE
