from calculator.subtraction import subtract

def test_subtract_positive_numbers():
    first, second = 5, 3
    expected = 2
    result = subtract(first, second)
    assert result == expected

def test_subtract_negative_numbers():
    first, second = -5, -3
    expected = -2
    result = subtract(first, second)
    assert result == expected

def test_subtract_zero():
    first, second = 0, 5
    expected = -5
    result = subtract(first, second)
    assert result == expected