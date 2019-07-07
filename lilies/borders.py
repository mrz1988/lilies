# -*- coding: utf-8 -*-
from builtins import range
from builtins import object
from .lilystring import grow

SINGLE_LINE = {
    "horiz": u"─",
    "vert": u"│",
    "top left": u"┌",
    "top right": u"┐",
    "bottom left": u"└",
    "bottom right": u"┘",
    "left x single": u"├",
    "right x single": u"┤",
    "top x single": u"┬",
    "bottom x single": u"┴",
    "horiz x single": u"┼",
    "vert x single": u"",
}


class ComplexBorderStyle(object):
    def __init__(
        self,
        left_style=1,
        right_style=1,
        top_style=1,
        bottom_style=1,
        left_color="",
        right_color="",
        top_color="",
        bottom_color="",
        left_padding=1,
        right_padding=1,
        top_padding=0,
        bottom_padding=0,
    ):
        self.left_style = left_style
        self.right_style = right_style
        self.top_style = top_style
        self.bottom_style = bottom_style
        self.left_padding = left_padding
        self.right_padding = right_padding
        self.bottom_padding = bottom_padding
        self.top_padding = top_padding
        self.top_color = top_color
        self.right_color = right_color
        self.bottom_color = bottom_color
        self.left_color = left_color

    def set_color(self, color):
        self.top_color = color
        self.right_color = color
        self.left_color = color
        self.bottom_color = color

    def set_style(self, style):
        self.left_style = style
        self.right_style = style
        self.top_style = style
        self.bottom_style = style

    def get_top_height(self):
        return self.top_padding + (self.top_style is not None)

    def get_bottom_height(self):
        return self.bottom_padding + (self.bottom_style is not None)

    def get_left_width(self):
        return self.left_padding + (self.left_style is not None)

    def get_right_width(self):
        return self.right_padding + (self.right_style is not None)

    def get_total_width(self):
        return self.get_left_width() + self.get_right_width()

    def get_total_height(self):
        return self.get_top_height() + self.get_bottom_height()

    def render_top_left(self):
        return grow(SINGLE_LINE["top left"], self.top_color) + grow(
            SINGLE_LINE["horiz"] * self.left_padding, self.top_color
        )

    def render_top_right(self):
        return grow(
            SINGLE_LINE["horiz"] * self.right_padding, self.top_color
        ) + grow(SINGLE_LINE["top right"], self.top_color)

    def render_bottom_left(self):
        return grow(SINGLE_LINE["bottom left"], self.bottom_color) + grow(
            SINGLE_LINE["horiz"] * self.left_padding, self.bottom_color
        )

    def render_bottom_right(self):
        return grow(
            SINGLE_LINE["horiz"] * self.right_padding, self.bottom_color
        ) + grow(SINGLE_LINE["bottom right"], self.bottom_color)

    def render_top(self, width):
        ctrwidth = width - self.get_total_width()
        border = [
            self.render_top_left()
            + grow(SINGLE_LINE["horiz"] * ctrwidth, self.top_color)
            + self.render_top_right()
        ]
        padding = [
            grow(" " * ctrwidth, self.top_color)
            for _ in range(self.top_padding)
        ]
        return border + self.wrap_lines(padding, ctrwidth)

    def render_bottom(self, width):
        ctrwidth = width - self.get_total_width()
        border = [
            self.render_bottom_left()
            + grow(SINGLE_LINE["horiz"] * ctrwidth, self.bottom_color)
            + self.render_bottom_right()
        ]
        padding = [
            grow(" " * ctrwidth, self.bottom_color)
            for _ in range(self.bottom_padding)
        ]
        return border + self.wrap_lines(padding, ctrwidth)

    def wrap_lines(self, lines, width, justify="left"):
        return list([self.wrap_line(l, width, justify) for l in lines])

    def wrap_line(self, line, width, justify="left"):
        cwidth = width - self.get_total_width()
        return (
            grow(SINGLE_LINE["vert"], self.left_color)
            + grow(" " * self.left_padding, self.left_color)
            + grow(line).resize(cwidth, justify=justify)
            + grow(" " * self.right_padding, self.right_color)
            + grow(SINGLE_LINE["vert"], self.right_color)
        )


class BorderStyle(ComplexBorderStyle):
    def __init__(self, style=None, color="", horiz_padding=0, vert_padding=0):
        super(BorderStyle, self).__init__(
            style,
            style,
            style,
            style,
            color,
            color,
            color,
            color,
            horiz_padding,
            horiz_padding,
            vert_padding,
            vert_padding,
        )
