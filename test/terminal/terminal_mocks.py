from builtins import object
from lilies.terminal.detect import SystemProperties

# This file attempts to recreate shitty terminal
# representations. Ideally, this will eventually
# contain a ton of different terminal variants
# with their appropriate sys/env vars. Unfortunately,
# for the time being I cannot adequately generate
# these mocks from terminal output, so they are
# largely guesses as to rough shapes that we
# expect different environments will return.


class MockStdout(object):
    def __init__(self, istty=True):
        self.istty = istty

    def isatty(self):
        return self.istty


MOCK_NOCOLOR_TERM = SystemProperties(
    stdout=MockStdout(True), env={"NO_COLOR": "TRUE"}
)


MOCK_NOTTY = SystemProperties(stdout=MockStdout(False))


MOCK_TRUECOLOR_TERM = SystemProperties(
    env={"COLORTERM": "truecolor"}, stdout=MockStdout()
)


MOCK_24BIT_TERM = SystemProperties(
    env={"COLORTERM": "24bit"}, stdout=MockStdout()
)


MOCK_8BIT_TERM = SystemProperties(
    env={"COLORTERM": "8bit"}, stdout=MockStdout()
)


MOCK_ITERM = SystemProperties(
    env={"TERM_PROGRAM": "iTerm.app"}, stdout=MockStdout()
)


MOCK_HYPER_TERM = SystemProperties(
    env={"TERM_PROGRAM": "Hyper"}, stdout=MockStdout()
)


MOCK_APPLE_TERM = SystemProperties(
    env={"TERM_PROGRAM": "Apple_Terminal"}, stdout=MockStdout()
)


MOCK_SCREEN256_TERM = SystemProperties(
    env={"TERM": "screen-256"}, stdout=MockStdout()
)


MOCK_XTERM256 = SystemProperties(
    env={"TERM": "xterm-256"}, stdout=MockStdout()
)


MOCK_VT100 = SystemProperties(env={"TERM": "vt100"}, stdout=MockStdout())


MOCK_SIMPLE = SystemProperties(env={"TERM": "xterm"}, stdout=MockStdout())


MOCK_WINDOWS10_256 = SystemProperties(
    pltform="Windows", stdout=MockStdout(), version=["10", "0", "10600"]
)


MOCK_WINDOWS10_24BIT = SystemProperties(
    pltform="Windows", stdout=MockStdout(), version=["10", "0", "15000"]
)


MOCK_CYGWIN_NEW = SystemProperties(
    pltform="CYGWIN_NT-10.0-15000",
    stdout=MockStdout(),
    version=["3", "0", "7-338", "x86_64"],
)


MOCK_CYGWIN_OLD = SystemProperties(
    pltform="CYGWIN_NT-10.0-15000",
    stdout=MockStdout(),
    version=["2", "0", "7-338", "x86_64"],
)


MOCK_GIT_BASH = SystemProperties(
    env={"TERM": "cygwin", "MINGW64": "MSYSTEM"},
    pltform="Windows",
    stdout=MockStdout(),
)


MOCK_WINDOWS = SystemProperties(pltform="Windows", stdout=MockStdout())


MOCK_AIXTERM = SystemProperties(env={"TERM": "aixterm"}, stdout=MockStdout())


MOCK_DUMB = SystemProperties(env={"TERM": "dumb"}, stdout=MockStdout())


MOCK_256_TPUT = SystemProperties(tput_colors=256, stdout=MockStdout())


MOCK_16_TPUT = SystemProperties(tput_colors=16, stdout=MockStdout())


MOCK_8_TPUT = SystemProperties(tput_colors=8, stdout=MockStdout())


MOCK_DEFAULT = SystemProperties(stdout=MockStdout())
