from __future__ import print_function
import atexit
from .colorama_shim import on_start, on_exit


def lilies_init():
    on_start()
    atexit.register(on_exit)
