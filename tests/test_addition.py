from calculator.addition import add

def test_add_positive_numbers():
    # Arrange
    first, second = 2, 3
    expected = 5
    # Act
    result = add(first, second)
    # Assert
    assert result == expected

def test_add_negative_numbers():
    first, second = -2, -3
    expected = -5
    result = add(first, second)
    assert result == expected

def test_add_zero():
    first, second = 5, 0
    expected = 5
    result = add(first, second)
    assert result == expected

