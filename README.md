# Lilies

[![Build Status](https://travis-ci.org/mrz1988/lilies.svg?branch=master)](https://travis-ci.org/mrz1988/lilies)
[![Code Coverage](https://codecov.io/gh/mrz1988/lilies/branch/master/graphs/badge.svg)](https://codecov.io/gh/mrz1988/lilies/branch/master)

Lilies is currently in alpha, and being updated from an old 2014 code base. A fresh README is in the works. Parts of the API are highly subject to change.

Lilies is a cross-platform colored CLI text formatting tool for python. It strives to provide maximum, seamless compatibility between different terminals on different operating systems, including older Windows support powered by popular coloring library [colorama](https://pypi.org/project/colorama/). It helps to hide weirdness from ANSI color characters, and adds powerful tools to interact with colored text. Lilies is supported on python 2.7, 3.4, 3.5, 3.6, and 3.7. It probably works in some other releases, too. No promises.

![Sup, world?](https://raw.githubusercontent.com/mrz1988/lilies/master/screenshots/screenshot01.png)

## Why not use alternatives?
There are [many options](https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python) to help you build colored text in terminal output. ANSI character sequences are the primary coloring tool for the command line, and many choose to directly use the characters with their own lookup table. Since this usage is not friendly for anything complex, [termcolor](https://pypi.org/project/termcolor/) provides a very convenient API for these characters. However, termcolor does not work on windows, and is nothing more than a convenient API to add these characters to your strings. This makes it very hard to arrange text once it has already been colored, since the `len()` function will provide unreliable output after coloring. Lilies provides more powerful string types, and 2D text manipulation. These tools help to build beautiful, complex CLI output, without compromising on terminal compatibility.

## Description
In addition to a very simple API, Lilies provides colored strings and associated tools that work very similarly to Python strings. Strings can be indexed, sliced, added, multiplied, and `len()`ed seamlessly, as if their colors were not even there. Lilies also contains tools to arrange your strings in your terminal to create neat columns, sort your output, and arrange sections of text on the screen.

## Getting started
Install us via [pip](https://pypi.org/project/lilies/)!
```
pip install lilies
```

## Contributing
You can find information about contributing [here](https://github.com/mrz1988/lilies/blob/master/docs/contributing.rst)

## License
[MIT](https://github.com/mrz1988/lilies/blob/master/LICENSE)
