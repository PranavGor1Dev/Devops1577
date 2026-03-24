import pytest
import app  

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0

def test_subtract():
    assert app.subtract(5, 3) == 2
    assert app.subtract(0, 5) == -5
    assert app.subtract(-3, -2) == -1

def test_multiply():
    assert app.multiply(4, 3) == 12
    assert app.multiply(-2, 3) == -6
    assert app.multiply(0, 100) == 0

def test_divide():
    assert app.divide(10, 2) == 5
    assert app.divide(-9, 3) == -3

    assert app.divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        app.divide(5, 0)
    assert "Cannot divide by zero" in str(exc_info.value)
