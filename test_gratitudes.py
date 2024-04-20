from  lib.gratitudes import *

# First: test needs to be just "Be grateful for:" and nothing else

def test_if_there_is_no_gratitude():
    grat = Gratitudes()
    result = grat.format()
    assert result == "Be grateful for: "

def test_if_there_is_one_gratitude():
    grat = Gratitudes()
    grat.add("sunsets")
    result = grat.format()
    assert result == "Be grateful for: sunsets"

def test_if_there_is_two_gratitudes():
    grat = Gratitudes()
    grat.add("sunsets")
    grat.add("turtles")
    result = grat.format()
    assert result == "Be grateful for: sunsets, turtles"


# def test_gratitude_attribute():
#     grat = Gratitudes()
#     grat.add("sunset")
#     assert grat.gratitudes == "sunset"
# this doesn't work because grat.gratitudes is a list 
# to check it's been added

def test_gratitude_added_to_list():
    grat = Gratitudes()
    grat.add("sunsets")
    assert "sunsets" in grat.gratitudes

# def test_gratitudes_of_different_types():
#     grat = Gratitudes()
#     grat.add("sunsets")
#     grat.add(True)
#     grat.add(5)
#     result = grat.format()
#     assert result == "Be grateful for: sunsets, True, 5"
    # This isn't relevant right now because we're not creating the perfect code 
    # we're making tests based on the code

