import pytest

from lilies.terminal.detect import (
    print_features,
    _get_system,
    _detect,
    NO_COLOR,
    ANSI8,
    ANSI8_OPEN,
    ANSI16,
    AIXTERM,
    ANSI256,
    FULL_RGB,
    WIN10_24BIT,
    WIN10_256,
    WIN32,
)

from terminal_mocks import (
    MOCK_NOCOLOR_TERM,
    MOCK_NOTTY,
    MOCK_TRUECOLOR_TERM,
    MOCK_24BIT_TERM,
    MOCK_8BIT_TERM,
    MOCK_ITERM,
    MOCK_HYPER_TERM,
    MOCK_APPLE_TERM,
    MOCK_SCREEN256_TERM,
    MOCK_XTERM256,
    MOCK_VT100,
    MOCK_SIMPLE,
    MOCK_CYGWIN_NEW,
    MOCK_CYGWIN_OLD,
    MOCK_GIT_BASH,
    MOCK_WINDOWS,
    MOCK_WINDOWS10_256,
    MOCK_WINDOWS10_24BIT,
    MOCK_AIXTERM,
    MOCK_DUMB,
    MOCK_256_TPUT,
    MOCK_16_TPUT,
    MOCK_8_TPUT,
    MOCK_DEFAULT,
)


def test_get_system_does_not_throw():
    _get_system()


@pytest.mark.parametrize(
    "system,output",
    [
        (MOCK_NOCOLOR_TERM, NO_COLOR),
        (MOCK_NOTTY, NO_COLOR),
        (MOCK_TRUECOLOR_TERM, FULL_RGB),
        (MOCK_24BIT_TERM, FULL_RGB),
        (MOCK_8BIT_TERM, ANSI256),
        (MOCK_ITERM, FULL_RGB),
        (MOCK_HYPER_TERM, FULL_RGB),
        (MOCK_APPLE_TERM, ANSI256),
        (MOCK_SCREEN256_TERM, ANSI256),
        (MOCK_XTERM256, ANSI256),
        (MOCK_VT100, ANSI16),
        (MOCK_SIMPLE, ANSI8_OPEN),
        (MOCK_CYGWIN_NEW, FULL_RGB),
        (MOCK_CYGWIN_OLD, AIXTERM),
        (MOCK_GIT_BASH, WIN32),
        (MOCK_WINDOWS, WIN32),
        (MOCK_WINDOWS10_24BIT, WIN10_24BIT),
        (MOCK_WINDOWS10_256, WIN10_256),
        (MOCK_AIXTERM, AIXTERM),
        (MOCK_DUMB, NO_COLOR),
        (MOCK_256_TPUT, ANSI256),
        (MOCK_16_TPUT, ANSI8_OPEN),
        (MOCK_8_TPUT, ANSI8),
        (MOCK_DEFAULT, ANSI8),
    ],
)
def test_detect_can_properly_detect_systems(system, output):
    expected = _detect(system)
    assert expected == output


def test_print_feature_helper():
    print_features(MOCK_WINDOWS10_24BIT)
