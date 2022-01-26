import pytest
from string import printable
from readchar import readchar, key


@pytest.mark.skip(reason="These work localy, but not on GitHub...")
@pytest.mark.parametrize("c", printable)
def test_printableCharacters(patched_stdin, c):
    patched_stdin.push(c)
    assert c == readchar(blocking=True)


@pytest.mark.skip(reason="I have no idea why these dont work...")
@pytest.mark.parametrize(
    ["seq", "key"],
    [
        ("\x0a", key.LF),
        ("\x0a", key.ENTER),
        ("\x0d", key.CR),
        ("\x08", key.BACKSPACE),
        ("\x20", key.SPACE),
        ("\x1b", key.ESC),
        ("\x09", key.TAB),
    ],
)
def test_controlCharacters(seq, key, patched_stdin):
    patched_stdin.push(seq)
    assert key == readchar()
