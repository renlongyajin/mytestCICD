# test_app.py

from app import add_numbers

def test_add_positive_numbers():
    """Test with positive numbers."""
    assert add_numbers(2, 3) == 5

def test_add_negative_numbers():
    """Test with negative numbers."""
    assert add_numbers(-1, -1) == -2

def test_add_zero():
    """Test with zero."""
    assert add_numbers(0, 5) == 5

def test_add_float_numbers():
    """Test with float numbers."""
    assert add_numbers(1.5, 2.5) == 4.0
