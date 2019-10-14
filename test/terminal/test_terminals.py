import pytest

from lilies.style.colors import Color
from lilies.style.styles import StyleDiff, Style
from lilies.style.palette import get_color, rgb, hsl
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
from lilies.terminal.ansi8open import Ansi8OpenTerminal
from lilies.terminal.ansi16 import Ansi16Terminal
from lilies.terminal.aixterm import AixTerminal
from lilies.terminal.ansi256 import Ansi256Terminal
from lilies.terminal.truecolor import TrueColorTerminal
from lilies.terminal.nocolor import NoColorTerminal
from lilies.terminal.exceptions import (
    UnsupportedColorException,
    UnsupportedAttributeException,
)


# Terminals
NOCOLOR = NoColorTerminal()
ANSI8 = Ansi8Terminal()
ANSI8OPEN = Ansi8OpenTerminal()
ANSI16 = Ansi16Terminal()
ANSI256 = Ansi256Terminal()
AIXTERM = AixTerminal()
TRUECOLOR = TrueColorTerminal()


# Colors
CORAL = get_color("lightcoral")
NEARCORAL = rgb(255, 130, 140)
MAROON = get_color("maroon")
BRIGHT_MAROON = get_color("red")
GRAY62 = get_color("grey62")
GRAY63 = hsl(0, 0, 63)
WHITE = get_color("white")
DEFAULT_COLOR = Color()


@pytest.mark.parametrize(
    "term,incolor,outcolor",
    [
        (NOCOLOR, MAROON, DEFAULT_COLOR),
        (NOCOLOR, CORAL, DEFAULT_COLOR),
        (ANSI8, CORAL, MAROON),
        (ANSI8, hsl(240, 40, 40), BLUE),
        (ANSI8, hsl(300, 40, 40), PURPLE),
        (ANSI8, hsl(120, 40, 40), GREEN),
        (ANSI8, hsl(50, 40, 40), YELLOW),
        (ANSI8, hsl(50, 5, 40), GRAY),
        (ANSI8, hsl(50, 5, 10), BLACK),
        (ANSI8OPEN, CORAL, MAROON),
        (ANSI16, CORAL, BRIGHT_MAROON),
        (ANSI16, hsl(20, 5, 20), BLACK),
        (ANSI16, hsl(20, 5, 50), get_color("grey")),
        (ANSI16, hsl(20, 5, 80), GRAY),
        (ANSI16, hsl(20, 5, 90), WHITE),
        (ANSI16, BRIGHT_MAROON, BRIGHT_MAROON),
        (AIXTERM, CORAL, BRIGHT_MAROON),
        (AIXTERM, hsl(20, 5, 20), BLACK),
        (AIXTERM, hsl(20, 5, 50), get_color("grey")),
        (AIXTERM, hsl(20, 5, 80), GRAY),
        (AIXTERM, hsl(20, 5, 90), WHITE),
        (AIXTERM, BRIGHT_MAROON, BRIGHT_MAROON),
        (ANSI256, CORAL, CORAL),
        (ANSI256, NEARCORAL, CORAL),
        (ANSI256, rgb(3, 3, 3), BLACK),
        (ANSI256, rgb(250, 250, 250), WHITE),
        (ANSI256, rgb(215, 30, 50), get_color("deeppink3a")),
        (ANSI256, GRAY63, GRAY62),
        (TRUECOLOR, NEARCORAL, NEARCORAL),
    ],
)
def test_fg_colors_are_configured(term, incolor, outcolor):
    style = Style(incolor)
    result = term.configure_style(style)
    assert outcolor == result.fg


@pytest.mark.parametrize(
    "term,incolor,outcolor",
    [
        (NOCOLOR, MAROON, DEFAULT_COLOR),
        (NOCOLOR, CORAL, DEFAULT_COLOR),
        (ANSI8, CORAL, MAROON),
        (ANSI8, hsl(240, 40, 40), BLUE),
        (ANSI8, hsl(300, 40, 40), PURPLE),
        (ANSI8, hsl(120, 40, 40), GREEN),
        (ANSI8, hsl(50, 40, 40), YELLOW),
        (ANSI8, hsl(50, 5, 40), GRAY),
        (ANSI8, hsl(50, 5, 10), BLACK),
        (ANSI8OPEN, CORAL, MAROON),
        (ANSI16, CORAL, MAROON),
        (ANSI16, hsl(20, 5, 10), BLACK),
        (ANSI16, hsl(20, 5, 20), GRAY),
        (ANSI16, hsl(20, 5, 50), GRAY),
        (ANSI16, hsl(20, 5, 80), GRAY),
        (ANSI16, hsl(20, 5, 90), GRAY),
        (ANSI16, BRIGHT_MAROON, MAROON),
        (AIXTERM, CORAL, BRIGHT_MAROON),
        (AIXTERM, hsl(20, 5, 20), BLACK),
        (AIXTERM, hsl(20, 5, 50), get_color("grey")),
        (AIXTERM, hsl(20, 5, 80), GRAY),
        (AIXTERM, hsl(20, 5, 90), WHITE),
        (AIXTERM, BRIGHT_MAROON, BRIGHT_MAROON),
        (ANSI256, CORAL, CORAL),
        (ANSI256, NEARCORAL, CORAL),
        (ANSI256, rgb(3, 3, 3), BLACK),
        (ANSI256, rgb(250, 250, 250), WHITE),
        (ANSI256, rgb(215, 30, 50), get_color("deeppink3a")),
        (ANSI256, GRAY63, GRAY62),
        (TRUECOLOR, NEARCORAL, NEARCORAL),
    ],
)
def test_bg_colors_are_configured(term, incolor, outcolor):
    style = Style(bg=incolor)
    result = term.configure_style(style)
    assert outcolor == result.bg


@pytest.mark.parametrize(
    "term,inattrs,outattrs",
    [
        (NOCOLOR, ["bold", "underline"], []),
        (ANSI8, ["bold", "underline"], []),
        (ANSI8OPEN, ["bold", "underline"], ["bold", "underline"]),
        (ANSI256, ["bold", "underline"], ["bold", "underline"]),
    ],
)
def test_attrs_are_configured(term, inattrs, outattrs):
    style = Style(attrs=inattrs)
    result = term.configure_style(style)
    assert outattrs == result.attrs


@pytest.mark.parametrize(
    "term,color",
    [
        (NOCOLOR, MAROON),
        (NOCOLOR, CORAL),
        (ANSI8, CORAL),
        (ANSI256, GRAY63),
        (ANSI256, NEARCORAL),
        (TRUECOLOR, Color(rgb=(1, 2.3, 3))),
    ],
)
def test_bad_fgcolors_are_incompatible(term, color):
    diff = StyleDiff(color)
    with pytest.raises(UnsupportedColorException):
        term.assert_compatible_stylediff(diff)


@pytest.mark.parametrize(
    "term,color",
    [
        (ANSI8, RED),
        (ANSI256, RED),
        (ANSI256, CORAL),
        (ANSI256, BLACK),
        (ANSI256, GRAY62),
    ],
)
def test_good_fgcolors_are_compatible(term, color):
    diff = StyleDiff(color)
    term.assert_compatible_stylediff(diff)


@pytest.mark.parametrize(
    "term,color",
    [
        (NOCOLOR, MAROON),
        (NOCOLOR, CORAL),
        (ANSI8, CORAL),
        (ANSI256, GRAY63),
        (ANSI256, NEARCORAL),
    ],
)
def test_bad_bgcolors_are_incompatible(term, color):
    diff = StyleDiff(bg=color)
    with pytest.raises(UnsupportedColorException):
        term.assert_compatible_stylediff(diff)


@pytest.mark.parametrize(
    "term,color",
    [
        (ANSI8, RED),
        (ANSI256, RED),
        (ANSI256, CORAL),
        (ANSI256, BLACK),
        (ANSI256, GRAY62),
    ],
)
def test_good_bgcolors_are_compatible(term, color):
    diff = StyleDiff(bg=color)
    term.assert_compatible_stylediff(diff)


@pytest.mark.parametrize("term,attr", [(ANSI8, "bold"), (NOCOLOR, "bold")])
def test_bad_true_attrs_are_incompatible(term, attr):
    diff = StyleDiff(attrs={attr: True})
    with pytest.raises(UnsupportedAttributeException):
        term.assert_compatible_stylediff(diff)


@pytest.mark.parametrize("term,attr", [(ANSI8, "bold"), (NOCOLOR, "bold")])
def test_bad_false_attrs_are_incompatible(term, attr):
    diff = StyleDiff(attrs={attr: False})
    with pytest.raises(UnsupportedAttributeException):
        term.assert_compatible_stylediff(diff)


@pytest.mark.parametrize(
    "term,color",
    [
        (NOCOLOR, MAROON),
        (NOCOLOR, CORAL),
        (ANSI8, CORAL),
        (ANSI256, NEARCORAL),
    ],
)
def test_encode_sequence_fails_on_bad_colors(term, color):
    diff = StyleDiff(color)
    with pytest.raises(UnsupportedColorException):
        term.encode_sequence(diff)


@pytest.mark.parametrize("term,attr", [(ANSI8, "bold"), (NOCOLOR, "bold")])
def test_encode_sequence_fails_on_bad_attrs(term, attr):
    diff = StyleDiff(attrs={attr: False})
    with pytest.raises(UnsupportedAttributeException):
        term.encode_sequence(diff)


@pytest.mark.parametrize(
    "term,color,ansi",
    [
        # TODO: These should get loaded by a json file or something.
        (ANSI8, BLACK, "\033[30m"),
        (ANSI8, RED, "\033[31m"),
        (ANSI8, YELLOW, "\033[33m"),
        (ANSI8, GREEN, "\033[32m"),
        (ANSI8, CYAN, "\033[36m"),
        (ANSI8, BLUE, "\033[34m"),
        (ANSI8, PURPLE, "\033[35m"),
        (ANSI8, GRAY, "\033[37m"),
        (ANSI8OPEN, BLACK, "\033[30m"),
        (ANSI8OPEN, RED, "\033[31m"),
        (ANSI8OPEN, YELLOW, "\033[33m"),
        (ANSI8OPEN, GREEN, "\033[32m"),
        (ANSI8OPEN, CYAN, "\033[36m"),
        (ANSI8OPEN, BLUE, "\033[34m"),
        (ANSI8OPEN, PURPLE, "\033[35m"),
        (ANSI8OPEN, GRAY, "\033[37m"),
        (ANSI16, BLACK, "\033[30m"),
        (ANSI16, RED, "\033[31m"),
        (ANSI16, YELLOW, "\033[33m"),
        (ANSI16, GREEN, "\033[32m"),
        (ANSI16, CYAN, "\033[36m"),
        (ANSI16, BLUE, "\033[34m"),
        (ANSI16, PURPLE, "\033[35m"),
        (ANSI16, GRAY, "\033[37m"),
        (ANSI16, BRIGHT_MAROON, "\033[31m\033[1m"),
        (AIXTERM, BLACK, "\033[30m"),
        (AIXTERM, RED, "\033[31m"),
        (AIXTERM, YELLOW, "\033[33m"),
        (AIXTERM, GREEN, "\033[32m"),
        (AIXTERM, CYAN, "\033[36m"),
        (AIXTERM, BLUE, "\033[34m"),
        (AIXTERM, PURPLE, "\033[35m"),
        (AIXTERM, GRAY, "\033[37m"),
        (AIXTERM, BRIGHT_MAROON, "\033[91m"),
        (ANSI256, BLACK, "\033[38;5;0m"),
        (ANSI256, RED, "\033[38;5;1m"),
        (ANSI256, GREEN, "\033[38;5;2m"),
        (ANSI256, YELLOW, "\033[38;5;3m"),
        (ANSI256, CYAN, "\033[38;5;6m"),
        (ANSI256, BLUE, "\033[38;5;4m"),
        (ANSI256, PURPLE, "\033[38;5;5m"),
        (ANSI256, GRAY, "\033[38;5;7m"),
        (ANSI256, GRAY62, "\033[38;5;247m"),
        (ANSI256, CORAL, "\033[38;5;210m"),
        (TRUECOLOR, BLACK, "\033[38;2;0;0;0m"),
        (TRUECOLOR, RED, "\033[38;2;128;0;0m"),
        (TRUECOLOR, GREEN, "\033[38;2;0;128;0m"),
        (TRUECOLOR, YELLOW, "\033[38;2;128;128;0m"),
        (TRUECOLOR, CYAN, "\033[38;2;0;128;128m"),
        (TRUECOLOR, BLUE, "\033[38;2;0;0;128m"),
        (TRUECOLOR, PURPLE, "\033[38;2;128;0;128m"),
        (TRUECOLOR, GRAY, "\033[38;2;192;192;192m"),
        (TRUECOLOR, GRAY62, "\033[38;2;158;158;158m"),
        (TRUECOLOR, CORAL, "\033[38;2;255;135;135m"),
        (TRUECOLOR, NEARCORAL, "\033[38;2;255;130;140m"),
    ],
)
def test_encode_sequence_properly_encodes_fg(term, color, ansi):
    diff = StyleDiff(color)
    result = term.encode_sequence(diff)
    assert ansi == result


@pytest.mark.parametrize(
    "term,color,ansi",
    [
        # TODO: These should get loaded by a json file or something.
        (ANSI8, BLACK, "\033[40m"),
        (ANSI8, RED, "\033[41m"),
        (ANSI8, YELLOW, "\033[43m"),
        (ANSI8, GREEN, "\033[42m"),
        (ANSI8, CYAN, "\033[46m"),
        (ANSI8, BLUE, "\033[44m"),
        (ANSI8, PURPLE, "\033[45m"),
        (ANSI8, GRAY, "\033[47m"),
        (ANSI8OPEN, BLACK, "\033[40m"),
        (ANSI8OPEN, RED, "\033[41m"),
        (ANSI8OPEN, YELLOW, "\033[43m"),
        (ANSI8OPEN, GREEN, "\033[42m"),
        (ANSI8OPEN, CYAN, "\033[46m"),
        (ANSI8OPEN, BLUE, "\033[44m"),
        (ANSI8OPEN, PURPLE, "\033[45m"),
        (ANSI8OPEN, GRAY, "\033[47m"),
        (ANSI16, BLACK, "\033[40m"),
        (ANSI16, RED, "\033[41m"),
        (ANSI16, YELLOW, "\033[43m"),
        (ANSI16, GREEN, "\033[42m"),
        (ANSI16, CYAN, "\033[46m"),
        (ANSI16, BLUE, "\033[44m"),
        (ANSI16, PURPLE, "\033[45m"),
        (ANSI16, GRAY, "\033[47m"),
        (ANSI256, BLACK, "\033[48;5;0m"),
        (ANSI256, RED, "\033[48;5;1m"),
        (ANSI256, GREEN, "\033[48;5;2m"),
        (ANSI256, YELLOW, "\033[48;5;3m"),
        (ANSI256, CYAN, "\033[48;5;6m"),
        (ANSI256, BLUE, "\033[48;5;4m"),
        (ANSI256, PURPLE, "\033[48;5;5m"),
        (ANSI256, GRAY, "\033[48;5;7m"),
        (ANSI256, GRAY62, "\033[48;5;247m"),
        (ANSI256, CORAL, "\033[48;5;210m"),
        (ANSI256, WHITE, "\033[48;5;231m"),
        (TRUECOLOR, BLACK, "\033[48;2;0;0;0m"),
        (TRUECOLOR, RED, "\033[48;2;128;0;0m"),
        (TRUECOLOR, GREEN, "\033[48;2;0;128;0m"),
        (TRUECOLOR, YELLOW, "\033[48;2;128;128;0m"),
        (TRUECOLOR, CYAN, "\033[48;2;0;128;128m"),
        (TRUECOLOR, BLUE, "\033[48;2;0;0;128m"),
        (TRUECOLOR, PURPLE, "\033[48;2;128;0;128m"),
        (TRUECOLOR, GRAY, "\033[48;2;192;192;192m"),
        (TRUECOLOR, GRAY62, "\033[48;2;158;158;158m"),
        (TRUECOLOR, CORAL, "\033[48;2;255;135;135m"),
        (TRUECOLOR, NEARCORAL, "\033[48;2;255;130;140m"),
    ],
)
def test_encode_sequence_properly_encodes_bg(term, color, ansi):
    diff = StyleDiff(bg=color)
    result = term.encode_sequence(diff)
    assert ansi == result


@pytest.mark.parametrize(
    "term,resetcode",
    [
        (NOCOLOR, ""),
        (ANSI8, "\033[39m"),
        (ANSI8OPEN, "\033[39m"),
        (ANSI256, "\033[39m"),
        (TRUECOLOR, "\033[39m"),
    ],
)
def test_encode_sequence_properly_encodes_fgreset(term, resetcode):
    diff = StyleDiff(Color())
    result = term.encode_sequence(diff)
    assert resetcode == result


@pytest.mark.parametrize(
    "term,resetcode",
    [
        (NOCOLOR, ""),
        (ANSI8, "\033[49m"),
        (ANSI8OPEN, "\033[49m"),
        (ANSI256, "\033[49m"),
        (TRUECOLOR, "\033[49m"),
    ],
)
def test_encode_sequence_properly_encodes_bgreset(term, resetcode):
    diff = StyleDiff(bg=Color())
    result = term.encode_sequence(diff)
    assert resetcode == result


@pytest.mark.parametrize(
    "term,stylediff,ansi",
    [
        (NOCOLOR, StyleDiff(), ""),
        (ANSI8, StyleDiff(get_color("green"), bg=Color()), "\033[32m\033[49m"),
        (
            ANSI8OPEN,
            StyleDiff(get_color("green"), bg=Color()),
            "\033[32m\033[49m",
        ),
        (ANSI256, StyleDiff(attrs={"italic": False}), "\033[23m"),
        (ANSI256, StyleDiff(attrs={"bold": False}), "\033[22m"),
        (ANSI256, StyleDiff(attrs={"bold": False, "dim": False}), "\033[22m"),
    ],
)
def test_encode_sequence_properly_encodes_multi(term, stylediff, ansi):
    result = term.encode_sequence(stylediff)
    assert ansi == result


@pytest.mark.parametrize(
    "term", [NOCOLOR, ANSI256, ANSI8, ANSI8OPEN, ANSI16, AIXTERM, TRUECOLOR]
)
def test_terminal_print_test_does_not_throw(term):
    term.test()
