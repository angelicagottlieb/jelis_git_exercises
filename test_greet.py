from lib.greet import * 

def test_greet_returns_greeting():
    result = greet("Jeli")
    assert result == "Hello, Jeli!"

