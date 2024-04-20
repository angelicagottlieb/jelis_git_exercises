from lib.string_builder import *

def test_empty_string():
    string = StringBuilder()
    result = string.output()
    assert result == ""

def test_standard_string():
    string = StringBuilder()
    string.add("Jels")
    result = string.output()
    assert result == "Jels"

def test_standard_string_and_length():
    string = StringBuilder()
    string.add("Jels")
    result2 = string.size()
    result = string.output()
    assert result == "Jels"
    assert result2 == 4

def test_length_of_empty():
    string = StringBuilder()
    result2 = string.size()
    assert result2 == 0

def test_adding_multiple():
    string = StringBuilder()
    string.add("Jels")
    string.add("eats")
    result = string.output()
    assert result == "Jelseats"


def test_adding_multiple_with_space():
    string = StringBuilder()
    string.add("Jels")
    string.add(" eats")
    result = string.output()
    assert result == "Jels eats"

# recommendations from Kay that I haven't included

def test_adding_multiple_with_space_as_extra_string():
    string = StringBuilder()
    string.add("Jels")
    string.add(" ")
    string.add("eats")
    result = string.output()
    assert result == "Jels eats"

def test_adding_multiple_with_space_as_extra_string_size():
    string = StringBuilder()
    string.add("Jels")
    string.add(" ")
    string.add("eats")
    result = string.size()
    assert result == 9