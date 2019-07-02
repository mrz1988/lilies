# Lilies

Lilies is a cross-platform text formatting tool for the command line, powered by popular coloring library [colorama](https://pypi.org/project/colorama/). It helps to hide weirdness from ANSI color characters, and adds powerful tools to interact with colored text.

# Description
In addition to a very simple API, Lilies provides colored strings and associated tools that work very similarly to Python strings. Strings can be indexed, sliced, added, multiplied, and `len()`ed seamlessly, as if their colors were not even there. Lilies also contains tools to arrange your strings in your terminal to create neat columns and more!

# Getting started
For now, Lilies is not on PIP, as it is still in beta and working on some cleanup. It may be unreliable in Python 3.x, and is poorly unit tested. To install locally:
```
git clone https://github.com/mrz1988/lilies.git
cd lilies
python setup.py install
```
Lilies provides a single basic function convert your standard Python strings into colored `LilyString` objects: `grow()`. This can be used like this:

```
>>> lily = grow('Hello, world!', 'red')
>>> lily
>>> c'Hello, world!' // this will be colored red!
```
`LilyString` objects appear prefixed with a "c" in the REPL to avoid confusing them with a conventional string. If you need to convert back, you can do so with `wilt()`:

```
>>> wilt(lily)
>>> u'Hello, world!'
```
Lilies will always return unicode strings to help with Python 3.x compatibility.

# Demo
WIP...

# API Documentation
WIP...

# Contributing
WIP...

# License
MIT
