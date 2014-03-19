from .packages.colorama import init, Fore, Back, Style
from .packages.colorama.initialise import deinit, reinit

class ColoramaDisabled(object):
    def __init__(self):
        pass
    
    def __enter__(self):
        deinit()
    
    def __exit__(self, t, v, tb):
        reinit()

foreground_colors = {
    'red'    : Fore.RED + Style.BRIGHT,
    'blue'   : Fore.BLUE + Style.BRIGHT,
    'green'  : Fore.GREEN + Style.BRIGHT,
    'cyan'   : Fore.CYAN + Style.BRIGHT,
    'yellow' : Fore.YELLOW + Style.BRIGHT,
    'magenta': Fore.MAGENTA + Style.BRIGHT,
    'white'  : Fore.WHITE + Style.BRIGHT,
    'gray'   : Fore.BLACK + Style.BRIGHT,
    'black'  : Fore.BLACK + Style.DIM,
    'dark red'     : Fore.RED + Style.DIM,
    'dark blue'    : Fore.BLUE + Style.DIM,
    'dark green'   : Fore.GREEN + Style.DIM,
    'dark cyan'    : Fore.CYAN + Style.DIM,
    'dark yellow'  : Fore.YELLOW + Style.DIM,
    'dark magenta' : Fore.MAGENTA + Style.DIM,
    'default': Fore.RESET + Style.NORMAL,
}
    
background_colors = {
    'red'    : Back.RED,
    'blue'   : Back.BLUE,
    'green'  : Back.GREEN,
    'cyan'   : Back.CYAN,
    'yellow' : Back.YELLOW,
    'white'  : Back.WHITE,
    'black'  : Back.BLACK,
    'magenta': Back.MAGENTA,
    'default': Back.RESET,
}
match_code = 'match'
reset_code = Style.RESET_ALL
init()
no_colorama = ColoramaDisabled()