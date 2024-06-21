import pytest

from main import sum_of_digits
from main import is_lucky


@pytest.mark.parametrize(
    "number, result",
    [
        (1234, 10),
        (-1234, 10),
        (100, 1),
        (0, 0),
        (7, 7)
    ],
)
def test_sum_success(number, result):
    assert sum_of_digits(number) == result


@pytest.mark.parametrize(
    "number, result",
    [
        (15, 5),
        (10, 10),
        (-17, 12)
    ],
)
def test_sum_fail(number, result):
    assert sum_of_digits(number) != result


def test_sum_exception():
    with pytest.raises(ValueError):
        sum_of_digits('1d2')


@pytest.mark.parametrize(
    "number, result",
    [
        (1212, True),
        (-8035, True),
        (7, True),
        (135, False)
    ],
)
def test_lucky_success(number, result):
    assert is_lucky(number) == result


def test_lucky_exception():
    with pytest.raises(ValueError):
        is_lucky('1d2')
