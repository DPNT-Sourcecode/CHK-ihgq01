import pytest
from solutions.CHK import checkout_solution


def test_checkout_solution_illegal():
    result = checkout_solution.checkout('954698379')
    assert result == -1


def test_checkout_solution():
    result = checkout_solution.checkout('AAAC')
    assert result == 150


def test_checkout_solution_2():
    result = checkout_solution.checkout('DBABA')
    assert result == 160


def test_checkout_solution_3():
    result = checkout_solution.checkout('AAAAAAAAA')
    assert result == 380


def test_checkout_solution_4():
    result = checkout_solution.checkout('AAEEB')
    assert result == 180


def test_checkout_solution_5():
    result = checkout_solution.checkout('EEEEBB')
    assert result == 160


def test_checkout_solution_6():
    result = checkout_solution.checkout('BEBEEE')
    assert result == 160


def test_checkout_solution_7():
    result = checkout_solution.checkout('ABCDEABCDE')
    assert result == 280


def test_checkout_solution_8():
    result = checkout_solution.checkout('FFF')
    assert result == 20


def test_checkout_solution_9():
    result = checkout_solution.checkout('FFFF')
    assert result == 30


def test_checkout_solution_10():
    result = checkout_solution.checkout('UUU')
    assert result == 120


def test_checkout_solution_11():
    result = checkout_solution.checkout('UUUU')
    assert result == 120


def test_checkout_solution_12():
    result = checkout_solution.checkout('STX')
    assert result == 45


def test_checkout_solution_13():
    result = checkout_solution.checkout('STT')
    assert result == 45

