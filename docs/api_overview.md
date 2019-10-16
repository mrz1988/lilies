Grow and Wilt
--------------
Lilies uses two helper functions to add or remove color and style to text output. The `grow()` function is a convenient way to quickly add color to a string, or other text-like object:

```python
grow('hello', 'red') #returns 'hello' red text
grow(2000, 'blue')   #returns '2000' in blue text
```

To convert any lily-based object back into plain text, the `wilt()` function is used:

```python
colored = grow('hello', 'red')
uncolored = wilt(colored)
```

Sometimes it's useful to think of groups of strings as a single, two-dimensional text block. This may help in conceptualizing layouts on the screen, or building custom columns. The `grow()` function does this automatically when a set of input is iterable:

```python
block = grow(['lilies', 'works' 'vertically'], 'green')
```

Or, you can pass in some newline-delimited strings to arrive at the same behavior:

```python
block = grow('lilies\nis\nfun!', 'yellow')
```

When wilting a block, instead of returning the strings in a set, the block is coalesced into a single string, delimited by newline characters.

```python
strings = ['lilies', 'works', 'vertically']
block = grow(strings, 'green')
assert "\n".join(strings) == wilt(block)
```

Specifying Color and Style
--------------------------
The second parameter passed into `grow()` is interpreted as a "style string". This is a human-readable representation of the foreground color, background color, and style attributes that lilies should apply to the string.

Style attributes always come first, separated by commas:

```python
# yes
grow('hello', 'bold, underlined')
grow('hello', 'bold red')
grow('hello', 'underlined on white')

# no
grow('hello', 'red underlined')
```

Lilies will ignore all whitespace added between style attributes, only the commas are significant. Lilies recognizes the following words to refer to attributes:

- Bold
  - `'bold'`
  - `'strong'`
  - `'bright'` This exists because some consoles use 'bold' to mean 'highlighted text'.
- Dim
  - `'dim'`
- Italic
  - `'italic'`
- Strikethrough
  - `'strike'`
  - `'strikethrough'`
  - `'struck'`
  - `'struckthrough'`
- Underline
  - `'underlined'`
  - `'underline'`
  - `'underscore'`
  - `'underscored'`
- Blink
  - `'blink'`
  - `'flash'`

Lilies supports all standard XTerm color names in the [256 color table](https://jonasjacek.github.io/colors/). Lilies strives to be very lenient with how it accepts color names to allow your team some flexibility with conventions. Colors are not case-sensitive, and both whitespace and underscores are ignored when added in a color name. Foreground colors should always come first:

```python
# all of these are valid
grow('hello', 'dark_green')
grow('hello', 'darkGreen')
grow('hello', 'dark green')
grow('hello', 'bold dark green')
grow('hello', 'DARK_GREEN')
```

Background colors are denoted by the `on` keyword. A color that immediately follows the word `'on'` will be applied to the background:

```python
# all valid
grow('hello', 'red on green')
grow('hello', 'bold on green')
grow('hello', 'on green')
```

The LilyString Object
---------------------
Most of the time, you probably only want to deal with normal strings that have added color. Lilies' string-like object is called `LilyString`, and in most cases behaves similarly to other string objects. Try these out for yourself:

```python
# concatenate them
combined = grow('hello,', 'red') + grow(' world!', 'blue')

# multiply them
lotsa_commas = grow('h,', 'yellow') * 10

# index them
combined[-1]

# slice them
combined[4:8]

# and dice them
lotsa_commas.split(',') #not sensitive to color
```

You may note that LilyString objects are represented similarly to other strings in the console:

```python
>>> grow('hello')
c'hello'
```

This is to maximize readability when using the python REPL, and avoid having to look at unhelpful `<LilyString object...` markers. Strings are printed normally otherwise:

```python
>>> print(grow('hello'))
hello
```

LilyStrings also are hashable, equatable, and comparable. Two LilyStrings are equal (and therefore hash the same) if they contain the same text, and are colored in the exact same way:

```python
assert grow('hello', 'red') == grow('hello', 'red')
assert grow('hello', 'blue') != grow('hello', 'red')
```

of course, if color isn't important to you, you can always check like this:

```python
# use is_text or isnt_text:
assert grow('hello', 'red').is_text('hello')
assert grow('hello', 'red').is_text(grow('hello', 'blue'))

# or just do it with wilt:
assert 'hello' == wilt(grow('hello', 'red'))
```

One annoying part of dealing with colors, is that they are usually represented as non-printable characters designed to mark up the text. Once these characters are added to normal python strings, it throws off then `len()` function, making it harder to properly shape output. Lilies fixes this by always returning the exact number of printable characters, as if the colors were not there:

```python
assert len('hello') == len(grow('hello', 'red'))
```

LilyStrings are also comparable as if they were regular strings. Color has no effect.

In some cases, you may want to see if a string is contained in another string. That's also possible:

```python
# not color sensitive with normal strings:
assert 'ello' in grow('hello', 'red')

# color sensitive when LilyStrings are used:
assert grow('ello', 'blue') not in grow('hello', 'red')
```

There are also plenty more string functions that behave exactly as you would expect on LilyStrings, completely ignoring color unless it's important to be preserved:

- `upper`
- `lower`
- `swapcase`
- `strip`
- `lstrip`
- `rstrip`
- `count`
- `startswith`
- `endswith`
- `isalnum`
- `isalpha`
- `isdigit`
- `isspace`
- `istitle`
- `isupper`



The LilyBlock Object
--------------------
Sometimes you aren't just coloring a few strings, you're organizing information on the screen. This is where the `LilyBlock` object comes in, and is effectively a two-dimensional string:

```python
strings = ['hello', 'world']
block = grow(strings)
assert block.width() == max([len(s) for s in strings])
assert block.height() == len(strings)
```

Maybe you didn't really want that, and want a way to go back to a `LilyString`:

```python
# to LilyString
lily = block.to_lilystring()

# and back!
block = grow(lily)
```

A `LilyBlock` has a number of operations that help you shape it in two dimensions:

```python
strings = ['a', 'set of', 'off lengths']
block = grow(strings, 'on green')

# make the green extend for the entire bounding rectangle!
block.normalize()
```
