import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_number_middle():
    assert module.missing_number_xor([3, 0, 1]) == 2


def test_missing_number_zero():
    assert module.missing_number_xor([1, 2, 3]) == 0


def test_missing_number_last():
    assert module.missing_number_xor([0, 1, 2]) == 3
