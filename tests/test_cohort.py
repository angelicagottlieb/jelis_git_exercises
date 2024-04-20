from lib.cohort import *
from datetime import datetime , date


def test_cohort_constructs():
    cohort = Cohort(1, "Test Cohort", date(2023, 12, 3))
    assert cohort.id == 1
    assert cohort.name == "Test Cohort"
    assert cohort.starting_date == date(2023, 12, 3)


def test_construct_formats_nicely():
    cohort = Cohort(1, "Test Cohort", date(2023, 12, 3))
    assert str(cohort) == "Cohort(1, Test Cohort, 2023-12-03)"

def test_cohorts_are_equal():
    cohort1 = Cohort(1, "Test Cohort", date(2023, 12, 3))
    cohort2 = Cohort(1, "Test Cohort", date(2023, 12, 3))
    assert cohort1 == cohort2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
