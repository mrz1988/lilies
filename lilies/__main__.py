##########################################################################
# Lilies
# By: Matt Zychowski (copyright 2014-2019)
#
# A library wrapped around colorama for using colored strings in the terminal
# window.  Provides advanced manipulation of colored strings, including
# accurate slicing.
#
##########################################################################

from __future__ import print_function
from sys import exit
import argparse
from builtins import str
from builtins import input
from . import grow, __version__
from .test import run_tests

description = "A colored text formatting tool for the command line"
argp = argparse.ArgumentParser(description=description)
argp.add_argument('-t', '--test', action='store_true', help="Only run tests.")
argp.add_argument('-c', '--contains', default='',
                  help="Search for tests to run by substring")
argp.add_argument('-g', '--grep', default='.*',
                  help="Grep for a subset of test cases to run")
args = argp.parse_args()

if not args.test:
    print(grow('Lilies!', 'green'))
    print(grow(description, 'yellow'))
    print('Version: ' + str(__version__))
    print('Author: Matt Zychowski')
    print()
    print('=' * 50)
    print()
    input("Press [ENTER] to run tests.")

all_passed = run_tests(pattern=args.grep, contains=args.contains, verbosity=1)
if (all_passed):
    exit(0)
else:
    exit(1)
