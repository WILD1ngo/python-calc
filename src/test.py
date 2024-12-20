import pytest
from main import calculate_expression

def test_basic_arithmetic():
    # Addition
    assert calculate_expression("2 + 2") == 4
    assert calculate_expression("0 + 0") == 0
    assert calculate_expression("-2 + 3") == 1
    
    # Subtraction
    assert calculate_expression("10 - 5") == 5
    assert calculate_expression("0 - 10") == -10
    assert calculate_expression("-5 - (-5)") == 0

    # Multiplication
    assert calculate_expression("4 * 3") == 12
    assert calculate_expression("0 * 5") == 0
    assert calculate_expression("-3 * 3") == -9

    # Division
    assert calculate_expression("15 / 3") == 5
    assert calculate_expression("-12 / 4") == -3
    assert calculate_expression("5 / 2") == 2.5  # Ensure proper handling of float results

def test_complex_expressions():
    # Operator precedence
    assert calculate_expression("2 + 3 * 4") == 14
    assert calculate_expression("(2 + 3) * 4") == 20
    assert calculate_expression("10 / 2 + 3") == 8

    # Nested parentheses
    assert calculate_expression("((2 + 3) * 4) / 2") == 10
    assert calculate_expression("(1 + (2 * (3 + 4)))") == 15

    # Combination of operators
    assert calculate_expression("3 + 4 * 2 / (1 - 5)^2") == 3.5
    assert calculate_expression("(5 - 3) * (8 + 2) / 2") == 10

def test_edge_cases():
    # Zero division
    with pytest.raises(ZeroDivisionError):
        calculate_expression("10 / 0")
    with pytest.raises(ZeroDivisionError):
        calculate_expression("0 / 0")

    # Complex nesting
    assert calculate_expression("((((10 + 2) * 3) - 4) / 2) + 1") == 17
    assert calculate_expression("(5 + (3 * (4 + (2 * 3))))") == 35

    # Negative numbers
    assert calculate_expression("-5 + (-3)") == -8
    assert calculate_expression("(-5 * -3) + (-10)") == 5

def test_invalid_input():
    # Non-numeric input
    with pytest.raises(Exception):
        calculate_expression("abc")
    with pytest.raises(Exception):
        calculate_expression("2 + two")
    
    # Invalid syntax
    with pytest.raises(Exception):
        calculate_expression("2 + + 2")
    with pytest.raises(Exception):
        calculate_expression("(2 + 3")
    with pytest.raises(Exception):
        calculate_expression("2 + 3)")

def test_large_numbers():
    # Very large values
    assert calculate_expression("1000000000 * 1000000000") == 1000000000000000000
    assert calculate_expression("999999999 + 1") == 1000000000
    assert calculate_expression("10 ^ 10") == 10000000000

def test_decimal_numbers():
    # Floating-point operations
    assert calculate_expression("2.5 + 3.1") == 5.6
    assert calculate_expression("10.0 / 4.0") == 2.5
    assert calculate_expression("-5.5 * 2") == -11.0
