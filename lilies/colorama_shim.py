from builtins import object
import platform
from colorama import init, Fore, Back, Style
from colorama.initialise import deinit, reinit


bright = Style.BRIGHT if "Windows" in platform.system() else ""


def on_start():
    init()


def on_exit():
    deinit()


class ColoramaDisabled(object):
    def __init__(self):
        pass

    def __enter__(self):
        deinit()

    def __exit__(self, t, v, tb):
        reinit()


foreground_colors = {
    "bright red": Fore.RED + Style.BRIGHT,
    "bright blue": Fore.BLUE + Style.BRIGHT,
    "bright green": Fore.GREEN + Style.BRIGHT,
    "bright cyan": Fore.CYAN + Style.BRIGHT,
    "bright yellow": Fore.YELLOW + Style.BRIGHT,
    "bright magenta": Fore.MAGENTA + Style.BRIGHT,
    "red": Fore.RED + bright,
    "blue": Fore.BLUE + bright,
    "green": Fore.GREEN + bright,
    "cyan": Fore.CYAN + bright,
    "yellow": Fore.YELLOW + bright,
    "magenta": Fore.MAGENTA + bright,
    "white": Fore.WHITE + bright,
    "gray": Fore.BLACK + bright,
    "black": Fore.BLACK + Style.DIM,
    "dark red": Fore.RED + Style.DIM,
    "dark blue": Fore.BLUE + Style.DIM,
    "dark green": Fore.GREEN + Style.DIM,
    "dark cyan": Fore.CYAN + Style.DIM,
    "dark yellow": Fore.YELLOW + Style.DIM,
    "dark magenta": Fore.MAGENTA + Style.DIM,
    "default": Fore.RESET + Style.NORMAL,
}

background_colors = {
    "red": Back.RED,
    "blue": Back.BLUE,
    "green": Back.GREEN,
    "cyan": Back.CYAN,
    "yellow": Back.YELLOW,
    "white": Back.WHITE,
    "black": Back.BLACK,
    "magenta": Back.MAGENTA,
    "default": Back.RESET,
}
match_code = "match"
reset_code = Style.RESET_ALL
no_colorama = ColoramaDisabled()
