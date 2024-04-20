from lib.check_codeword import check_codeword

def test_checks_codeword_is_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_checks_codeword_is_close():
    result = check_codeword("hirse")
    assert result == "Close, but nope."


def test_checks_codeword_is_incorrect():
    result = check_codeword("mother")
    assert result == "WRONG!"

def test_checks_codeword_is_definitey_incorrect_even_with_correct_first_letter():
    result = check_codeword("hous")
    assert result == "WRONG!"

def test_checks_codeword_is_definitey_incorrect_even_with_correct_last_letter():
    result = check_codeword("meenie")
    assert result == "WRONG!"
# Remember all separate tests for different things need to be called
#     something different
#     can also add multiline string to describe
#     what is going on 
#     e.g. """ If the codeword is correct, the function
# return Correct! Come in."""