################################################################################
# Lilies
# By: Matt Zychowski (copyright 2014-2019)
#
# A library wrapped around colorama for using colored strings in the terminal
# window.  Provides advanced manipulation of colored strings, including accurate
# slicing.
#
################################################################################

from __future__ import print_function
from sys import argv, exit
from builtins import str
from builtins import input
from . import grow, __version__
from .test import test_all

if len(argv) > 1 and argv[1] == 'test':
    if not (test_all()):
        exit(1)
    else:
        exit()


print(grow('Lilies!', 'green'))
print(grow('A colored text formatting tool for the command line',
           'yellow'))
print('Version: ' + str(__version__))
print('Author: Matt Zychowski')
print()
print('=' * 50)
print()
input("Press [ENTER] to run tests.")

print(test_all())
