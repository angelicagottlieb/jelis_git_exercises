from lib.report_length import *

def test_correct_length_returns_correct_string():
    result = report_length("Angelica")
    assert result == "This string was 8 characters long."

def test_correct_length_returns_correct_string_with_space():
    result = report_length("Angelica ")
    assert result == "This string was 9 characters long."


def test_correct_length_returns_correct_long_string_with_space():
    result = report_length("Angelica went to Israel and she loved everything she saw there")
    assert result == "This string was 62 characters long."

def test_correct_length_returns_correct_long_string_with_space_and_exclamation():
    result = report_length("Angelica went to Israel and she! loved! everything! she saw there")
    assert result == "This string was 65 characters long."

