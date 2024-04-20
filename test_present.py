import pytest 
from lib.present import *

# def test_if_theres_contents():
#     prez = Present()
#     prez.wrap(True)
#     with pytest.raises(Exception) as e:
#         prez.wrap()
#     error_message = str(e.value)
#     assert error_message == "A contents has already been wrapped."
# This isn't working

# Advice from Kay
# wrapping and unwrapping = 
# present.wrap(3)
# present.unwrap()
# gets 3 
# gets error if try to unwrap present before wrapping
# if we do wrap and wrap again
# we get another error

# def test_it_wraps_contents():
#     prez = Present()
#     result = prez.wrap(2)
#     assert result == 2
    # This doesn't work because only time we get return is when we wrap and unwrap

def test_wrap_then_unwrap():
    prez = Present()
    prez.wrap(3)
    result = prez.unwrap()
    assert result == 3


def test_if_theres_no_contents_no_present_to_unwrap():
    prez = Present()
    with pytest.raises(Exception) as e:
        prez.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


# def test_if_theres_already_contents_wrapped():
#     prez = Present()
#     prez.wrap(3)
#     prez.wrap(3)
#     with pytest.raises(Exception) as e:
#         prez.wrap()
#     error_message = str(e.value)
#     assert error_message == "A contents has already been wrapped."
    # Why isn't this working??


def test_if_theres_already_contents_wrapped():
    prez = Present()
    prez.wrap(44)
    with pytest.raises(Exception) as e:
        prez.wrap(44)
        error_message = str(e.value)
        assert error_message == "A contents has already been wrapped."

def test_if_theres_already_contents_wrapped_different_contents():
    prez = Present()
    prez.wrap(44)
    with pytest.raises(Exception) as e:
        prez.wrap(5)
        error_message = str(e.value)
        assert error_message == "A contents has already been wrapped."

# #Little trick
# piece of behaviour
# if we try to wrap an already wrapped value but 
# we've already wrapped something successfully 
# first value should still be wrapped

def test_first_wrapped_unchanged():
    prez = Present()
    prez.wrap(44)
    with pytest.raises(Exception) as e:
        prez.wrap(5)
    assert prez.unwrap() == 44

