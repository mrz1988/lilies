from __future__ import absolute_import
from .colorama_shim import foreground_colors, background_colors

class TextColor(object):
    def __init__(self, colorstring=''):
        if colorstring == '':
            self.name = 'default'
        else:
            self.name = colorstring
        self.ansi = self.parse_color(colorstring)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.ansi)

    @staticmethod
    def parse_color(colorstring):
        fore = ''
        back = ''
        parts = colorstring.lower().split(' ')
        index_of_on = -1
        for i in range(len(parts)):
            if parts[i] == 'on':
                index_of_on = i
                break
        if index_of_on == -1:
            fore = ' '.join(parts)
        elif index_of_on == 0:
            back = ' '.join(parts)
        else:
            fore = ' '.join(parts[:index_of_on])
            back = ' '.join(parts[index_of_on + 1:])

        if fore == '':
            fore = 'default'
        if back == '':
            back = 'default'

        if not fore in foreground_colors:
            raise KeyError("foreground color %s was invalid" % fore)
        if not back in background_colors:
            raise KeyError("background color %s was invalid" % back)

        return foreground_colors[fore] + background_colors[back]