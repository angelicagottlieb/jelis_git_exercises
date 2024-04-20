
from lib.counter import *

def test_checks_report_is_correct_with_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_checks_report_is_correct_with_number_added():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

def test_checks_report_method_twice():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    assert counter.report() == "Counted to 15 so far."

def test_checks_report_method_twice():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    assert counter.report() == "Counted to 15 so far."

def test_checks_num_attribute():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5
#     #tried to do counter.num didn't work because 
#     num is only listed as num would need to be self.num 
# and self.num = num in that ask 

def test_checks_num_attribute():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5
    # This works because at this point when 
    # the count attribute is accessed self.count from 
    # the initiliaser it's then become 5
    # assert counter.count == 5 ensures that after calling the add() method with an argument of 5 on the counter instance, the count attribute of the counter instance is set to 5.

def test_checks_num_attribute_with_zero():
    counter = Counter()
    assert counter.count == 0

def tests_check_with_minus_numbers():
    counter = Counter()
    counter.add(-5)
    assert counter.report() == "Counted to -5 so far."



# recommendations from Kay that I haven't included 
    # e.g. when you break it and you make the function self.count = num (not self.count += num) it still passes









