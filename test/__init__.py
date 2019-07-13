from __future__ import print_function
import unittest
import re
import argparse
from sys import exit
from lilies import grow


def run_tests(pattern=".*", contains="", verbosity=1):
    full_suite = unittest.TestLoader().discover(".")
    suite = _filter_tests(full_suite, pattern, contains)
    runner = unittest.TextTestRunner(verbosity=verbosity)
    all_passed = runner.run(suite).wasSuccessful()
    if all_passed:
        print(grow("Testing passed!", "green"))
    else:
        print(grow("Testing failed. See the output above.", "red"))
    print()
    return all_passed


def _filter_tests(suite, pattern, contains):
    regex = re.compile(pattern)
    new_suite = unittest.TestSuite()
    for test in _list_of_tests(suite):
        id = test.id()
        matches = regex.match(id) and contains in id
        if matches:
            new_suite.addTest(test)
    return new_suite


def _list_of_tests(suite):
    for test in suite:
        if unittest.suite._isnotsuite(test):
            yield test
        else:
            for t in _list_of_tests(test):
                yield t


if __name__ == "__main__":
    description = "Lilies unit tests"
    argp = argparse.ArgumentParser(description=description)
    argp.add_argument(
        "-c",
        "--contains",
        default="",
        help="Search for tests to run by substring",
    )
    argp.add_argument(
        "-g",
        "--grep",
        default=".*",
        help="Grep for a subset of test cases to run",
    )
    args = argp.parse_args()

    all_passed = run_tests(
        pattern=args.grep, contains=args.contains, verbosity=1
    )
    if all_passed:
        exit(0)
    else:
        exit(1)
