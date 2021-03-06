import unittest
from lilies.style.colors import rgb_to_hsl, hsl_to_rgb
from lilies.style import Color, Style
from lilies.style.palette import get_color


class TestStyles(unittest.TestCase):
    def test_get_returns_color(self):
        result = get_color("deepskyblue4b")
        self.assertIsInstance(result, Color)

    def test_get_return_none_for_invalid(self):
        result = get_color("nonsense")
        self.assertIsNone(result)

    def test_blank_color_isreset(self):
        color = Color()
        self.assertTrue(color.isreset())

    def test_color_equality(self):
        color1 = Color(rgb=(1, 2, 3))
        color2 = Color(rgb=(1, 2, 3))
        self.assertEqual(color1, color2)

    def test_color_inequality(self):
        color1 = Color(rgb=(1, 2, 3))
        color2 = Color(rgb=(1, 2, 4))
        self.assertNotEqual(color1, color2)

    def test_color_hashing_equality(self):
        color1 = Color(rgb=(1, 2, 3))
        color2 = Color(rgb=(1, 2, 3))
        self.assertEqual(hash(color1), hash(color2))

    def test_color_hashing_inequality(self):
        color1 = Color(rgb=(1, 2, 3))
        color2 = Color(rgb=(1, 2, 4))
        self.assertNotEqual(hash(color1), hash(color2))

    def test_color_hashing_works_with_hsl(self):
        color1 = Color(hsl=(23, 100, 10))
        color2 = Color(hsl=(23, 100, 10))
        color3 = Color(hsl=(20, 10, 100))
        self.assertEqual(hash(color1), hash(color2))
        self.assertNotEqual(hash(color1), hash(color3))

    # These tests are a little finicky with preloaded colors
    # mainly because of bad rounding when converting to HSL.
    # The colors don't cleanly map back and forth to any
    # accuracy unfortunately, but simple colors are decent.
    def test_rgb_to_hsl(self):
        color = get_color("aqua")
        hsl = rgb_to_hsl(*color.rgb)

        self.assertAlmostEqual(color.hsl[0], hsl[0])
        self.assertAlmostEqual(color.hsl[1], hsl[1])
        self.assertAlmostEqual(color.hsl[2], hsl[2])

    def test_hsl_to_rgb(self):
        color = get_color("aqua")
        rgb = hsl_to_rgb(*color.hsl)

        self.assertAlmostEqual(color.rgb[0], rgb[0])
        self.assertAlmostEqual(color.rgb[1], rgb[1])
        self.assertAlmostEqual(color.rgb[2], rgb[2])

    def test_style_equality_fg_colors(self):
        style1 = Style(fg=Color(rgb=(1, 2, 3)))
        style2 = Style(fg=Color(rgb=(1, 2, 3)))
        assert style1 == style2

    def test_style_equality_mixed(self):
        style1 = Style(fg=Color(rgb=(1, 2, 3)), bg=Color(rgb=(1, 2, 3)))
        style2 = Style(fg=Color(rgb=(1, 2, 3)), bg=Color(rgb=(1, 2, 3)))
        assert style1 == style2

    def test_style_inequality_fg_colors(self):
        style1 = Style(fg=Color(rgb=(1, 2, 3)))
        style2 = Style(fg=Color(rgb=(2, 3, 4)))
        assert style1 != style2

    def test_style_diff_from_default(self):
        fg = get_color("red")
        bg = get_color("blue")
        attrs = ["bold", "underline"]
        style = Style(fg, bg, attrs)
        diff = style.diff(Style())
        self.assertEqual(fg, diff.fg)
        self.assertEqual(bg, diff.bg)
        self.assertEqual({"bold": True, "underline": True}, diff.attrs)

    def test_style_diff_color_change_fgbg(self):
        fg1 = get_color("red")
        fg2 = get_color("blue")
        bg1 = get_color("green")
        bg2 = get_color("gold")
        style1 = Style(fg1, bg1)
        style2 = Style(fg2, bg2)
        diff = style2.diff(style1)
        self.assertEqual(fg2, diff.fg)
        self.assertEqual(bg2, diff.bg)
        self.assertEqual({}, diff.attrs)

    def test_style_diff_color_change_fg(self):
        fg1 = get_color("red")
        fg2 = get_color("blue")
        style1 = Style(fg1, bg=get_color("black"))
        style2 = Style(fg2, bg=get_color("black"))
        diff = style2.diff(style1)
        self.assertEqual(fg2, diff.fg)
        self.assertIsNone(diff.bg)
        self.assertEqual({}, diff.attrs)

    def test_style_diff_color_change_bg(self):
        bg1 = get_color("red")
        bg2 = get_color("blue")
        style1 = Style(fg=get_color("red"), bg=bg1)
        style2 = Style(fg=get_color("red"), bg=bg2)
        diff = style2.diff(style1)
        self.assertIsNone(diff.fg)
        self.assertEqual(bg2, diff.bg)
        self.assertEqual({}, diff.attrs)

    def test_style_diff_color_change_attr(self):
        attr1 = ["bold", "underline"]
        attr2 = ["bold", "italic"]
        style1 = Style(attrs=attr1)
        style2 = Style(attrs=attr2)
        diff = style2.diff(style1)
        self.assertIsNone(diff.fg)
        self.assertIsNone(diff.bg)
        self.assertEqual({"underline": False, "italic": True}, diff.attrs)
