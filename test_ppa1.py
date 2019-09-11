import pytest
from io import StringIO
from functions import calculate_bmi, shortest_distance, email_verifier, split_bill

def test_bmi_nonfloat():
    with pytest.raises(ValueError):
        assert calculate_bmi("asdf", 150)

def test_bmi__return_list():
    assert type(calculate_bmi(63, 125)) is list

def test_bmi_normal():
    assert calculate_bmi(63, 125) == ['22.7', "Normal weight"], "Should be 22.7 and Normal weight"

def test_bmi_overweight():
    assert calculate_bmi(63, 150) == ['27.2', "Overweight"], "Should be 27.2 and Overweight"

def test_bmi_obese():
    assert calculate_bmi(60, 150) == ['30.0', "Obese"], "Should be 30.0 and Obese"

def test_bmi_underweight():
    assert calculate_bmi(67, 110) == ['17.6', "Underweight"], "Should be 17.6 and Underweight"

def test_bmi_zero_height():
    with pytest.raises(ZeroDivisionError):
        assert calculate_bmi(0, 150)

def test_distance_wrong_format_no_commas():
    with pytest.raises(Exception):
        assert shortest_distance("14", "25")

def test_distance_wrong_format_more_commas():
    with pytest.raises(Exception):
        assert shortest_distance("1,,4", "2,,5")

def test_distance_nonfloat():
    with pytest.raises(ValueError):
        assert shortest_distance("asdf,5", "33,5")

def test_distance_return_float():
    assert type(shortest_distance("1,5", "2,5")) is float

def test_distance_reg():
    assert shortest_distance("1,5", "2,5") == 1.0, "Should be 1.0"

def test_distance_sqrt():
    assert shortest_distance("1,4", "2,5") == 1.41, "Should be root 2"

def test_email_return_bool():
    assert type(email_verifier("abhi@gmail.com")) is bool

def test_email_no_at():
    assert email_verifier("abhigmail.com") == False

def test_email_many_at():
    assert email_verifier("abhi@@gmail.com") == False

def test_email_front_period():
    assert email_verifier(".abhi@gmail.com") == False

def test_email_two_periods():
    assert email_verifier("abhi..kante@gmail.com") == False

def test_email_front_digit():
    assert email_verifier("1abhi@gmail.com") == False

def test_email_incorrect_symbols():
    assert email_verifier("abhi`@gmail.com") == False

def test_email_correct_symbol():
    assert email_verifier("abhi!@gmail.com") == True

def test_email_correct():
    assert email_verifier("abhi@gmail.com") == True

def test_split_return_list():
    assert type(split_bill(1,2)) is list

def test_split_nonfloat():
    with pytest.raises(Exception):
        assert split_bill("hello", 2)
