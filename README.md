# Lilies

[![Build Status](https://travis-ci.org/mrz1988/lilies.svg?branch=master)](https://travis-ci.org/mrz1988/lilies)
[![Code Coverage](https://codecov.io/gh/mrz1988/lilies/branch/master/graphs/badge.svg)](https://codecov.io/gh/mrz1988/lilies/branch/master)

Lilies is a cross-platform text formatting tool for python on the command line, powered by popular coloring library [colorama](https://pypi.org/project/colorama/). It helps to hide weirdness from ANSI color characters, and adds powerful tools to interact with colored text. Lilies supports both python2 and python3.

# Description
In addition to a very simple API, Lilies provides colored strings and associated tools that work very similarly to Python strings. Strings can be indexed, sliced, added, multiplied, and `len()`ed seamlessly, as if their colors were not even there. Lilies also contains tools to arrange your strings in your terminal to create neat columns and more!

# Getting started
For now, Lilies is not on PIP, as it is still in alpha and working on some cleanup and new features. To install on your native python:
```
git clone https://github.com/mrz1988/lilies.git
easy_install ./lilies
```

It's also common to have a python 3.7 (or similar) install on your machine. If you've installed `python3` via homebrew, give this a go:
```
git clone https://github.com/mrz1988/lilies.git
easy_install-3.7 ./lilies
```
Alternatively, you may need to do some digging to find what your python install has done with your setuptools to install it.

Lilies provides a single basic function convert your standard Python strings into colored `LilyString` objects: `grow()`. This can be used like this:

```
>>> from lilies import grow
>>> lily = grow('Hello, world!', 'red')
>>> lily
>>> c'Hello, world!' // this will be colored red!
```
`LilyString` objects appear prefixed with a "c" in the REPL to avoid confusing them with a conventional string. If you need to convert back, you can do so with `wilt()`:

```
>>> from lilies import wilt
>>> wilt(lily)
>>> u'Hello, world!'
```
Strings can be sliced and diced while preserving their colors:
```
>>> lily[::2]
>>> c'Hlo ol!'
>>> lily[3:]
>>> c'lo, world!'
>>> lily[:5]
>>> c'Hello'
```
And work as expected for most string-based functions:
```
>>> lily * 3
>>> c'Hello, world!Hello, world!Hello, world!'
>>> lily.split(',')
>>> [c'Hello', c' world!']
>>> grow('This is red! ', 'red') + grow('And this is green!', 'green')
>>> c'This is red! And this is green!'
```
There are even neat helper functions, like `columnify` that can arrange sets of strings in console for you:
```
>>> from lilies import columnify
>>> strings = ['from there', 'to here', 'from here', 'to there',
... 'lily strings', 'are everywhere.',
... 'one fish', 'two fish',
... grow('red fish', 'red'),
... grow('blue fish', 'blue')]
>>> print(columnify(strings, sort=False))
from there          to there            one fish            blue fish        
to here             lily strings        two fish         
from here           are everywhere.     red fish 
```

# Demo
WIP...

# API Documentation
WIP...

# Contributing
WIP...

# License
MIT
