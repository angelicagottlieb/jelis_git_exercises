import pytest 
from lib.password_checker import *

def test_returns_true_if_valid_more_than_8():
    pwd = PasswordChecker()
    result = pwd.check("Angelicalil1")
    assert result == True

def test_returns_error_message_if_unvalid():
    pwd = PasswordChecker()
    with pytest.raises(Exception) as e:
        pwd.check("Jeli1")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_if_password_is_empty():
    pwd = PasswordChecker()
    with pytest.raises(Exception) as e:
        pwd.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_if_password_is_exactly_eight():
    pwd = PasswordChecker()
    result = pwd.check("abcdefgh")
    assert result == True

def test_if_password_is_exactly_eight_with_special_character():
    pwd = PasswordChecker()
    result = pwd.check("a@c!e.gh")
    assert result == True

# Test for passwords with exactly 8 characters.
# Test for passwords with more than 8 characters.
# Test for passwords containing only letters.
# Test for passwords containing only numbers.
# Test for passwords containing only special characters.
# Test for passwords containing a mix of letters and numbers.
# Test for passwords containing a mix of letters and special characters.
# Test for passwords containing a mix of numbers and special characters.
# Test for passwords containing a mix of letters, numbers, and special characters.
# Test for passwords containing spaces.
# Test for passwords containing leading or trailing spaces.
# Test for passwords containing leading or trailing whitespace characters (such as tabs or newlines).
# Test for passwords containing non-ASCII characters.
# Test for passwords exceeding a certain maximum length (if applicable).
# Test for passwords that are exactly at the minimum length allowed (if applicable).

# def test_password_attribute_if_valid():
#     pwd = PasswordChecker()
#     pwd.check("Angelica1")
#     assert pwd.password == "Angelica1"
    # doesn't work because there's no password attribute in password it's only in check 

