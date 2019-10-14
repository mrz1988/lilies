from lilies.terminal.ansicodes import fg_to_bg, esc


def test_fg_to_bg_returns_None_on_None_input():
    assert fg_to_bg(None) is None


def test_esc_returns_emptystr_on_None_input():
    assert esc(None) == ""
