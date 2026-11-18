import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string_right_by_k():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_by_string_length():
    assert module.rotate_string("abc", 3) == "abc"


def test_empty_string():
    assert module.rotate_string("", 2) == ""
