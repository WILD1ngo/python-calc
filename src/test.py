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
    assert calculate_expression("5 / 2") == 2.5 

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


def test_minus_numbers():
    assert calculate_expression("---(--2)") == -2
    assert calculate_expression("-(3)!") == -6
    assert calculate_expression("2 +-2^2") == 6
    assert calculate_expression("2 --2^2") == -2
    assert calculate_expression("2 + -2") == 0
    assert calculate_expression("-2 + -2") == -4
    assert calculate_expression("-2 * -2") == 4
    assert calculate_expression("-2 * 2") == -4
    assert calculate_expression("-2 / -2") == 1

    # Mixed operators with different signs
    assert calculate_expression("-2 - -2") == 0
    assert calculate_expression("2 * -2") == -4
    assert calculate_expression("2 / -2") == -1
    assert calculate_expression("2 + --2") == 4

    # Parentheses with negations
    assert calculate_expression("-(3 + 2)") == -5
    assert calculate_expression("-(2 - (3 + 4))") == 5
    assert calculate_expression("-(2 + (3 - 4))") == -1

    # Power with multiple signs
    assert calculate_expression("2 +-3^2") == 11
    assert calculate_expression("2 --3^2") == -7

    # Factorial and signs
    assert calculate_expression("-(5)!") == -120  
    assert calculate_expression("-(4)!") == -24   

    # Large exponentiation with multiple signs
    assert calculate_expression("(-2)^3") == -8
    assert calculate_expression("-(2^3)") == -8
    assert calculate_expression("(-2)^2") == 4
    assert calculate_expression("-(2^2)") == -4

    # Edge case: unary minus followed by expression
    assert calculate_expression("-(-5 + 3)") == 2  
    assert calculate_expression("-(3 + (-5 + 3))") == -1


EPSILON = 0.1


def test_white_spaces_equation():
    assert calculate_expression("     2                   +3 ") == 5


def test_simple_plus_equation():
    assert calculate_expression("3+3") == 6


def test_simple_decrease_equation():
    assert calculate_expression("123-23") == 100


def test_simple_multiply_equation():
    assert calculate_expression("25*8") == 200


def test_simple_divide_equation():
    assert calculate_expression("200/4") == 50


def test_simple_power_equation():
    assert calculate_expression("2^3") == 8


def test_simple_modulo_equation():
    assert calculate_expression("22%3") == 1


def test_simple_max_equation():
    assert calculate_expression("5$9") == 9


def test_simple_min_equation():
    assert calculate_expression("5&9") == 5


def test_simple_avg_equation():
    assert calculate_expression("10@2") == 6


def test_simple_tilde_equation():
    assert calculate_expression("~2+6") == 4


def test_simple_factorial_equation():
    assert calculate_expression("5!-2") == 118


def test_simple_digit_sum_equation():
    assert calculate_expression("2.2222222#") == 16


def test_simple_unary_minus_equation():
    assert calculate_expression("---3!") == -6


def test_simple_sign_minus_equation():
    assert calculate_expression("2+--3!") == 8


def test_complex_equation1():
    assert calculate_expression("(7 + 3) * 5! - 10 @ ((6$2)#) ^ (1^2) * 8&9 * (2.5)") == 1040


def test_complex_equation2():
    assert calculate_expression("(9 * 3) + 2! @ 8 & 4 ^ 5 $ (3 * 2) + 8 + 1.23") == 4132.23


def test_complex_equation3():
    assert calculate_expression("(2 * 3) - 4--- 3@ ~6 & (8 ^ 4) $ (7 - 1.23) + 2 + ~ 10") == -11.77


def test_complex_equation4():
    assert calculate_expression("-----3! - ~2 ^ (2 - 4) $ (8+-2) ----- 10 * 2! + 9 # ") == -81


def test_complex_equation5():
    assert calculate_expression("(~5 @ 7) $ ((15 & 8)# ! + 4^2) % (3! * (~2 $ 6))") == 16


def test_complex_equation6():
    assert calculate_expression("~(15# ^ 2) @ ((42# $ 7) & (~3 * 4!))") == -54


def test_complex_equation7():
    assert calculate_expression("(25# * 3!) @ (16# $ (8# & 7^2))") == 45.5


def test_complex_equation8():
    assert abs(calculate_expression("~(15 @ 9) * (27# $ 8) + ((4 & 7) ^ (3!)) / (3.25 * (12 @ 4))") - 49.54) < EPSILON


def test_complex_equation9():
    assert calculate_expression("((12.5 @ 7.5) & ~4) ^ (31# $ (5 * 2)) + (15 & 9) * ((21# @ 6) $ 12)") == 1048684


def test_complex_equation10():
    assert calculate_expression("(~((16 $ 7)#) @ 12) * ((25# & 8) ^ 3) + (9.75 & 15) * ((18 @ 6) $ 3!)") == 974.5


def test_complex_equation11():
    assert calculate_expression("( (2 * 2) + 3 ) ^ 2 @ 4 + (9! #) - 7 % 2") == 369


def test_complex_equation12():
    assert calculate_expression("--2 @ 3 * (5! - 2) + 3 ^ ~4 & (6 - 1.5) $ 8 # + 2!") == 6858


def test_complex_equation13():
    assert calculate_expression("(7 * 4) @ ~5 + 3! & 2 ^ 9 $ (8 - 1) # * 6") == 3083.5


def test_complex_equation14():
    assert calculate_expression("(3 ^ 3) * ~6 @ 5! $ (7 - 3) + 2.2222# ") == 1549


def test_complex_equation15():
    assert calculate_expression("2+-2 ^ 3 * 2! @ ~6 + 7 & (4 - 1) $ 2  ") == 21


def test_complex_equation16():
    assert calculate_expression("2 ^ (3 & 1) * (8 + ~4) $ 6! @ 2 & (10 - 1.5) # -(5 ^ 3) + 4!") == -75


def test_complex_equation17():
    assert calculate_expression("((5! * (3 + 2)) @ (9 * ~4)) + ((7 - 1) * (8 + 2)) $ ((6 - 2) * 5) & 3 - (4! + 2)") == 259


def test_complex_equation18():
    assert calculate_expression("4! * 2 ^ 3 @ ~7 $ 6 + 8 * 2 & 10.11111# +-----4 - 1") == 1547


def test_complex_equation19():
    assert calculate_expression("---9 * --(3! + 5) ## @ 7 - ~2 $ 8 & 4 - (6 - 1)") == -49.5


def test_complex_equation20():
    assert calculate_expression("-3+2 @ (2 ^ 2) + 5 * 5! - 4! $ (8 & 2) + 2 ^ ~4 * (2! + 10) @ 8 # + -2^3") == 568.625