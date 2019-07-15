import os
import sys
import platform
import subprocess
from builtins import object


# Note: The order, names, and numbers
# on these may change at any time.
# Do not rely on them long-term.
NO_COLOR = 1
ANSI8 = 2
ANSI8_OPEN = 3
ANSI16 = 4
AIXTERM = 5
ANSI256 = 6
FULL_RGB = 7
WIN32 = 8


def _get_system():
    plat = platform.system()
    env = os.environ
    stdout = sys.stdout
    version = platform.release().split(".")
    try:
        result = subprocess.check_output(["tput", "colors"])
        tput_colors = int(result.strip())
    except Exception:
        tput_colors = None

    return SystemProperties(plat, env, stdout, version, tput_colors)


class SystemProperties(object):
    def __init__(
        self,
        pltform="",
        env={},
        stdout=None,
        version=["0", "0", "0"],
        tput_colors=None,
    ):
        self.platform = pltform
        self.env = env
        self.stdout = stdout
        self.ver = version
        self.tput_colors = tput_colors


def detect(system=_get_system()):
    if not system.stdout.isatty():
        return NO_COLOR

    # Check colorterm env for modern
    # terminal settings
    colorterm = system.env.get("COLORTERM")
    if colorterm:
        if colorterm in {"truecolor", "24bit"}:
            return FULL_RGB
        if colorterm in {"8bit"}:
            return ANSI256

    termprogram = system.env.get("TERM_PROGRAM")
    if termprogram:
        if termprogram in {"iTerm.app", "Hyper"}:
            return FULL_RGB
        if termprogram in {"Apple_Terminal"}:
            return ANSI256

    term = system.env.get("TERM")
    if term:
        if "screen-256" in term or "xterm-256" in term:
            return ANSI256
        if "vt100" in term:
            return ANSI16
        if term in {"screen", "xterm", "color", "ansi", "cygwin", "linux"}:
            return ANSI8_OPEN

    if "Windows" in system.platform:
        return _get_windows_color(system)

    if term:
        if "aixterm" in term or "xterm-16" in term:
            return AIXTERM

        if term in {"dumb"}:
            return NO_COLOR

    termcolors = _get_termcolors(system.tput_colors)
    if termcolors:
        return termcolors

    # fuck it, most terms should be 8 color...
    return ANSI8


def _get_windows_color(system):
    # TODO: detect cygwin/conemu?

    # FIXME
    # Chalk uses something like this,
    # but this fails badly if we are in
    # CMD, or presumably also in PowerShell...
    # release = system.version
    # if release[0] == "10":
    #    # Windows10 started to add real color support.
    #    # Detect if this version is up to date
    #    micro_ver = int(release[2])
    #    if micro_ver > 10586:
    #        return FULL_RGB if micro_ver > 14931 else ANSI256

    return WIN32


def _get_termcolors(tput_colors):
    if tput_colors is None:
        return None
    if tput_colors >= 256:
        # Honestly, if this is more than 256,
        # we can't be sure if it's truecolor.
        # There are some weird terminals out there,
        # including 4352 color support?
        return ANSI256
    if tput_colors >= 16:
        # sadly I can't be certain that this will
        # properly support bright colors?
        return ANSI8_OPEN
    if tput_colors >= 8:
        return ANSI8
    return NO_COLOR
