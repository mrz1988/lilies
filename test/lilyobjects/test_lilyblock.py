#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import unittest
import os
from lilies import grow, wilt, LilyBlock
from lilies.style.parse import parse_style


class TestLilyBlock(unittest.TestCase):
    def setUp(self):
        self.strings = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
        ]
        self.padded_strings = [
            "",
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
            "   xxxx",
            "    ",
        ]
        self.small_block = LilyBlock(["a", "b", "c"])
        self.padded_block = LilyBlock(os.linesep.join(self.padded_strings))
        self.single_str = os.linesep.join(self.strings)
        self.single_lily = grow(self.single_str)

    def test_print(self):
        print(LilyBlock("☃"))

    def test_lilyblock_creation_list(self):
        control = self.single_str
        test = wilt(LilyBlock(self.strings))
        self.assertEqual(control, test)

    def test_lilyblock_creation_string(self):
        control = self.single_str
        test = wilt(LilyBlock(control))
        self.assertEqual(control, test)

    def test_lilyblock_creation_lilystring(self):
        control = self.single_str
        test = wilt(LilyBlock(self.single_lily))
        self.assertEqual(control, test)

    def test_lilyblock_creation_with_whitespace(self):
        control = os.linesep.join(self.padded_strings)
        self.assertEqual(
            len(self.padded_strings), len(control.split(os.linesep))
        )
        self.assertEqual(control, wilt(self.padded_block))

    def test_resize_x_larger(self):
        control_group = [
            "hello                  ",
            "dfDfEEFdfaC            ",
            "Mister John            ",
            "mr. jOhn               ",
            "iSn't it               ",
            "comma,separated,values ",
            "trailing,comma,        ",
            ",                      ",
        ]
        control = os.linesep.join(control_group)
        test = LilyBlock(self.single_str).resize_x(23)
        self.assertEqual(control, wilt(test))

    def test_resize_y_top_larger(self):
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
            " ",
            " ",
            " ",
        ]
        control = os.linesep.join(control_group)
        test = LilyBlock(self.single_str).resize_y(11, "top")
        self.assertEqual(control, wilt(test))

    def test_resize_y_bottom_larger(self):
        control_group = [
            " ",
            " ",
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
        ]
        control = os.linesep.join(control_group)
        test = LilyBlock(self.single_str).resize_y(10, "bottom")
        self.assertEqual(control, wilt(test))

    def test_resize_y_center_larger(self):
        control_group = [
            " ",
            " ",
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
            " ",
            " ",
            " ",
        ]
        control = os.linesep.join(control_group)
        test = LilyBlock(self.single_str).resize_y(13, "center")
        self.assertEqual(control, wilt(test))

    def test_resize_y_top_smaller(self):
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
        ]
        control = os.linesep.join(control_group)
        test = LilyBlock(self.single_str).resize_y(6, "top")
        self.assertEqual(control, wilt(test))

    def test_resize_y_bottom_smaller(self):
        control_group = [
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
        ]
        control = os.linesep.join(control_group)
        test = LilyBlock(self.single_str).resize_y(7, "bottom")
        self.assertEqual(control, wilt(test))

    def test_resize_y_center_smaller(self):
        control_group = [
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
        ]
        control = os.linesep.join(control_group)
        test = LilyBlock(self.single_str).resize_y(5, "center")
        self.assertEqual(control, wilt(test))

    def test_indexing(self):
        control1 = "hello"
        control2 = "comma,separated,values"
        block = LilyBlock(self.single_str)
        test1 = wilt(block[0])
        test2 = wilt(block[-3])
        self.assertEqual(control1, test1)
        self.assertEqual(control2, test2)

    def test_slicing_subset1(self):
        control_group = ["hello", "dfDfEEFdfaC", "Mister John", "mr. jOhn"]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block[:4])
        self.assertEqual(control, test)

    def test_slicing_subset2(self):
        control_group = ["dfDfEEFdfaC", "Mister John"]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block[1:3])
        self.assertEqual(control, test)

    def test_slicing_stepwise(self):
        control_group = ["hello", "Mister John", "iSn't it", "trailing,comma,"]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block[::2])
        self.assertEqual(control, test)

    def test_slicing_reverse(self):
        control_group = [
            ",",
            "trailing,comma,",
            "comma,separated,values",
            "iSn't it",
            "mr. jOhn",
            "Mister John",
            "dfDfEEFdfaC",
            "hello",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block[::-1])
        self.assertEqual(control, test)

    def test_length(self):
        block = LilyBlock(self.single_str)
        self.assertEqual(81, len(block))

    def test_width(self):
        block = LilyBlock(self.single_str)
        self.assertEqual(22, block.width())

    def test_height(self):
        block = LilyBlock(self.single_str)
        self.assertEqual(8, block.height())

    def test_normalize(self):
        control_group = [
            "hello                 ",
            "dfDfEEFdfaC           ",
            "Mister John           ",
            "mr. jOhn              ",
            "iSn't it              ",
            "comma,separated,values",
            "trailing,comma,       ",
            ",                     ",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block.normalize())
        self.assertEqual(control, test)

    def test_concat_without_squash(self):
        control_group = [
            "hello                 hello",
            "dfDfEEFdfaC           dfDfEEFdfaC",
            "Mister John           Mister John",
            "mr. jOhn              mr. jOhn",
            "iSn't it              iSn't it",
            "comma,separated,valuescomma,separated,values",
            "trailing,comma,       trailing,comma,",
            ",                     ,",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block.concat(block))
        self.assertEqual(control, test)

    def test_concat_with_squash(self):
        control_group = [
            "hellohello",
            "dfDfEEFdfaCdfDfEEFdfaC",
            "Mister JohnMister John",
            "mr. jOhnmr. jOhn",
            "iSn't itiSn't it",
            "comma,separated,valuescomma,separated,values",
            "trailing,comma,trailing,comma,",
            ",,",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block.concat(block, squash=True))
        self.assertEqual(control, test)

    def test_append_string_default(self):
        new_row = "new row!"
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
            new_row,
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block.append(new_row))
        self.assertEqual(control, test)

    def test_append_block_default(self):
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
            "a",
            "b",
            "c",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block.append(self.small_block))
        self.assertEqual(control, test)

    def test_append_lilystring_default(self):
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
            "a lilystring",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block.append(grow("a lilystring", "red")))
        self.assertEqual(control, test)

    def test_append_string_justify(self):
        new_row = "new row!"
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
            "              " + new_row,
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block.append(new_row, justify="right"))
        self.assertEqual(control, test)

    def test_append_block_justify(self):
        control_group = [
            "          a           ",
            "          b           ",
            "          c           ",
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(self.small_block.append(block, justify="center"))
        self.assertEqual(control, test)

    def test_append_lilystring_justify(self):
        new_row = "new row!"
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
            "              " + new_row,
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        lily = grow(new_row, "red")
        test = wilt(block.append(lily, justify="right"))
        self.assertEqual(control, test)

    def test_addition(self):
        control_group = [
            "hello                 hello",
            "dfDfEEFdfaC           dfDfEEFdfaC",
            "Mister John           Mister John",
            "mr. jOhn              mr. jOhn",
            "iSn't it              iSn't it",
            "comma,separated,valuescomma,separated,values",
            "trailing,comma,       trailing,comma,",
            ",                     ,",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block + block)
        self.assertEqual(control, test)

    def test_multiplication(self):
        control_group = [
            "hello                 hello                 hello",
            "dfDfEEFdfaC           dfDfEEFdfaC           dfDfEEFdfaC",
            "Mister John           Mister John           Mister John",
            "mr. jOhn              mr. jOhn              mr. jOhn",
            "iSn't it              iSn't it              iSn't it",
            "comma,separated,valuescomma,separated,values"
            + "comma,separated,values",
            "trailing,comma,       trailing,comma,       trailing,comma,",
            ",                     ,                     ,",
        ]
        control = os.linesep.join(control_group)
        block = LilyBlock(self.single_str)
        test = wilt(block * 3)
        self.assertEqual(control, test)

    def test_wilt(self):
        control_group = [
            "hello",
            "dfDfEEFdfaC",
            "Mister John",
            "mr. jOhn",
            "iSn't it",
            "comma,separated,values",
            "trailing,comma,",
            ",",
        ]
        control = os.linesep.join(control_group)
        style = parse_style("red")
        block = LilyBlock(self.single_str, style)
        test1 = wilt(block)
        test2 = block.wilt()
        self.assertEqual(control, test1)
        self.assertEqual(control, test2)

    def test_lstrip_with_no_chars(self):
        control_group = [
            "",
            "",
            "xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
            "xxxx",
            "",
        ]
        control = os.linesep.join(control_group)
        test = self.padded_block.lstrip()
        self.assertEqual(control, wilt(test))

    def test_lstrip_with_chars(self):
        control_group1 = [
            "",
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "abcd   ",
            "   xxxx",
            "    ",
        ]
        control_group2 = [
            "",
            "",
            "abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "abcd   ",
            "",
            "",
        ]
        control1 = os.linesep.join(control_group1)
        control2 = os.linesep.join(control_group2)
        test1 = self.padded_block.lstrip("xy")
        test2 = self.padded_block.lstrip("xy ")
        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))

    def test_rstrip_with_no_chars(self):
        control_group = [
            "",
            "",
            "  xy  abcd  xy",
            "abcd",
            "abcdxyyy",
            "xyxyabcd",
            "   xxxx",
            "",
        ]
        control = os.linesep.join(control_group)
        test = self.padded_block.rstrip()
        self.assertEqual(control, wilt(test))

    def test_rstrip_with_chars(self):
        control_group1 = [
            "",
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcd",
            "xyxyabcd   ",
            "   ",
            "    ",
        ]
        control_group2 = [
            "",
            "",
            "  xy  abcd",
            "abcd",
            "abcd",
            "xyxyabcd",
            "",
            "",
        ]
        control1 = os.linesep.join(control_group1)
        control2 = os.linesep.join(control_group2)
        test1 = self.padded_block.rstrip("xy")
        test2 = self.padded_block.rstrip("xy ")
        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))

    def test_tstrip_with_no_chars(self):
        control_group = [
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
            "   xxxx",
            "    ",
        ]
        control = os.linesep.join(control_group)
        test = self.padded_block.tstrip()
        self.assertEqual(control, wilt(test))

    def test_tstrip_with_chars(self):
        control_group1 = [
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
            "   xxxx",
            "    ",
        ]
        control_group2 = [
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
            "   xxxx",
            "    ",
        ]
        control1 = os.linesep.join(control_group1)
        control2 = os.linesep.join(control_group2)
        test1 = self.padded_block.tstrip("xy")
        test2 = self.padded_block.tstrip("xy ")
        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))

    def test_bstrip_with_no_chars(self):
        control_group = [
            "",
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
            "   xxxx",
        ]
        control = os.linesep.join(control_group)
        test = self.padded_block.bstrip()
        self.assertEqual(control, wilt(test))

    def test_bstrip_with_chars(self):
        control_group1 = [
            "",
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
            "   xxxx",
            "    ",
        ]
        control_group2 = [
            "",
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcdxyyy",
            "xyxyabcd   ",
        ]
        control1 = os.linesep.join(control_group1)
        control2 = os.linesep.join(control_group2)
        test1 = self.padded_block.bstrip("xy")
        test2 = self.padded_block.bstrip("xy ")
        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))

    def test_2d_strip_with_no_chars(self):
        control_group = [
            "xy  abcd  xy",
            "abcd",
            "abcdxyyy",
            "xyxyabcd",
            "xxxx",
        ]
        control = os.linesep.join(control_group)
        test = self.padded_block.strip()
        self.assertEqual(control, wilt(test))

    def test_2d_strip_with_chars(self):
        control_group1 = [
            "     ",
            "  xy  abcd  xy    ",
            "abcd",
            "abcd",
            "abcd   ",
            "   ",
            "    ",
        ]
        control_group2 = ["abcd", "abcd", "abcd", "abcd"]
        control1 = os.linesep.join(control_group1)
        control2 = os.linesep.join(control_group2)
        test1 = self.padded_block.strip("xy")
        test2 = self.padded_block.strip("xy ")
        self.assertEqual(control1, wilt(test1))
        self.assertEqual(control2, wilt(test2))
