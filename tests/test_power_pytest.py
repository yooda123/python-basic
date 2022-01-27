import pytest

from pythontest.power import power, times

# pip install pytest
# python -m unittest test_power.py

# pip install pytest-cov
# pytest tests/test_power_pytest.py --cov=power --cov-report html

# クラスにしてもOK。その際は各メソッド引数にself忘れずに


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8

    with pytest.raises(TypeError):
        power(3, "2")


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6
