from lib.user_age_function import *
import pytest 

def test_user_under_sixteen():
    result = user_access("2020-07-06")
    assert result == "Access is denied. You are 3 years old. You need to be 16 to use this service."

def test_over_sixteen():
    result = user_access("1997-07-06")
    assert result == "Access granted!"

def test_wrong_type():
    with pytest.raises(Exception) as e:
        user_access(1997-7-6)
    error_message = str(e.value)
    assert error_message == "Wrong input type."

def test_wrong_type_again():
    with pytest.raises(Exception) as e:
        user_access(2.5)
    error_message = str(e.value)
    assert error_message == "Wrong input type."

def test_wrong_format():
    with pytest.raises(Exception) as e:
        user_access("07-02-2003")
    error_message = str(e.value)
    assert error_message == "Wrong input format."