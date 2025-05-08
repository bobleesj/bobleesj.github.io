# package version
from bobleesj import functions


def test_dot_product():
    """Test the dot_product function."""
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert functions.dot_product(a, b) == 32.0
