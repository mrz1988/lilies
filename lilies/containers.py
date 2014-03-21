import os
from .abstractions import Drawable, test_is_lily_obj
from .lilystring import grow
from .borders import ComplexBorderStyle

# BorderedContainer cannot be instantiated by itself, it's just an extension
# on top of the Drawable interface
class BorderedContainer(Drawable):
    def __init__(self, components=[], border=ComplexBorderStyle()):
        self._border = border
        self._components = []
        for comp in components:
            self.add(comp)

    def __str__(self):
        return os.linesep.join(map(str, self.render()))

    def __unicode__(self):
        return os.linesep.join(map(unicode, self.render()))

    def add_before(self, container):
        test_is_lily_obj(container)
        self._components = [container] + self._components

    def add(self, container):
        test_is_lily_obj(container)
        self._components += [container]

    def set_border(self, border):
        self._border = border

    def set_border_style(self, style):
        self._border.set_style(style)

    def set_border_color(self, color):
        self._border.set_color(color)

class HorizBox(BorderedContainer):
    def __init__(self, *args, **kwargs):
        super(HorizBox, self).__init__(*args, **kwargs)

    def get_min_height(self):
        return max(c.get_min_height() for c in self._components) +\
               self._border.get_top_height() +\
               self._border.get_bottom_height()

    def get_min_width(self):
        return sum(c.get_min_width() for c in self._components) +\
               self._border.get_left_width() +\
               self._border.get_right_width()

    def _mkline(self, stringset):
        #alternatively, self._separator.vert.join(stringset)
        #but! you'll have to figure out how to join those separators with the
        #top and bottom borders :(
        return grow('').concat(stringset)

    def render(self):
        width = self.get_min_width()
        output = self._border.render_top(width)
        comp_lines = []
        for c in self._components:
            comp_lines.append(c.render())
        inner_height = max(map(len, comp_lines))
        for i in range(len(comp_lines)):
            ln_width = len(comp_lines[i][0])
            extra_lines = [grow(' ' * ln_width)\
                           for _ in range(inner_height - len(comp_lines[i]))]
            comp_lines[i] += extra_lines

        for ln in comp_lines:
            assert(len(ln) == inner_height)

        rows = list(map(self._mkline, zip(*comp_lines)))
        rows = self._border.wrap_lines(rows, width)
        output += rows
        output += self._border.render_bottom(width)

        return output

class VertBox(BorderedContainer):
    def __init__(self, *args, **kwargs):
        super(VertBox, self).__init__(*args, **kwargs)

    def get_min_height(self):
        return sum(c.get_min_height() for c in self._components) +\
               self._border.get_top_height() +\
               self._border.get_bottom_height()

    def get_min_width(self):
        return max(c.get_min_width() for c in self._components) +\
               self._border.get_left_width() +\
               self._border.get_right_width()

    def render(self):
        width = self.get_min_width()
        output = self._border.render_top(width)
        for c in self._components:
            output += self._border.wrap_lines(c.render(), width)
            #output += self._separator.horiz(_border)
        output += self._border.render_bottom(width)
        return output
