# Lilies

[![Build Status](https://travis-ci.org/mrz1988/lilies.svg?branch=master)](https://travis-ci.org/mrz1988/lilies)
[![Code Coverage](https://codecov.io/gh/mrz1988/lilies/branch/master/graphs/badge.svg)](https://codecov.io/gh/mrz1988/lilies/branch/master)

Lilies is currently in alpha. Parts of the API are highly subject to change. A fresh README is in the works.

Lilies is a cross-platform, colored CLI text-formatting tool for python. It provides lots of text coloring and formatting tools, bridged across almost any console. This includes older Windows support powered by popular coloring library [colorama](https://pypi.org/project/colorama/). Lilies will attempt to reproduce the original colors as close as possible, regardless of the current terminal's capabilities.

Lilies is supported on python 2.7, 3.4, 3.5, 3.6, and 3.7. It probably works in some other releases, too. No promises.

![Sup, world?](https://raw.githubusercontent.com/mrz1988/lilies/master/screenshots/screenshot01.png)

## Why not use alternatives?
There are [many options](https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python) to help you build colored text in terminal output. Many developers prefer to directly add their own ANSI sequences. Since this isn't great for complex things, [termcolor](https://pypi.org/project/termcolor/) provides a convenient abstraction. However, termcolor does not work on windows, and doesn't respect compatibility of other terminals. Formatting text once it has already been colored is also hard, since the `len()` function will include ANSI characters.

Lilies provides more powerful string tools, 2D text manipulation, and comfort that your coloring will respect the wishes of others' terminals.

## Getting started
Install us via [pip](https://pypi.org/project/lilies/)!
```
pip install lilies
```

## Contributing
You can find information about contributing [here](https://github.com/mrz1988/lilies/blob/master/docs/contributing.rst)

## License
[MIT](https://github.com/mrz1988/lilies/blob/master/LICENSE)
