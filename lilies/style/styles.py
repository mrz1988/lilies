from .colors import Color


class StyleDiff(object):
    def __init__(self, fg=None, bg=None, attrs={}):
        self.fg = fg
        self.bg = bg
        self.attrs = attrs


class Style(object):
    def __init__(self, fg=Color(), bg=Color(), attrs=[]):
        self.fg = fg
        self.bg = bg
        self.attrs = list(attrs)

    def diff(self, previous):
        fg_diff = None
        bg_diff = None
        if self.fg != previous.fg:
            fg_diff = self.fg
        if self.bg != previous.bg:
            bg_diff = self.bg
        these_attrs = set(self.attrs)
        those_attrs = set(previous.attrs)
        new_attrs = these_attrs - those_attrs
        removed_attrs = those_attrs - these_attrs
        attrs_diff = {}
        for attr in new_attrs:
            attrs_diff[attr] = True
        for attr in removed_attrs:
            attrs_diff[attr] = False
        return StyleDiff(fg_diff, bg_diff, attrs_diff)
