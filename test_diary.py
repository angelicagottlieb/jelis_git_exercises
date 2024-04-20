from lib.diary import *

def test_contents_initialised():
    diary = Diary("Hello")
    assert diary.contents == "Hello"

def test_reading_of_contents():
    diary = Diary("Hello")
    assert diary.read() == "Hello"