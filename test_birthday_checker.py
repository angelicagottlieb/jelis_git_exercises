from lib.birthday_checker import *


def test_init():
    checker = BirthdayChecker()
    assert checker.birthdays == []


def test_add_birthday():
    checker = BirthdayChecker()
    checker.add_birthday("Emily", "1991-07-04")
    assert checker.birthdays == [{"name": "Emily", "dob": "1991-07-04", "sent": False}]


def test_update_dob():
    checker = BirthdayChecker()
    checker.add_birthday("Emily", "1991-07-04")
    checker.update_dob("Emily", "2003-07-04")
    assert checker.birthdays == [{"name": "Emily", "dob": "2003-07-04", "sent": False}]


def test_update_name():
    checker = BirthdayChecker()
    checker.add_birthday("Emily", "1991-07-04")
    checker.update_name("Emily", "Xiangnan")
    assert checker.birthdays == [{"name": "Xiangnan", "dob": "1991-07-04", "sent": False}]


def test_find_upcoming_birthdays():
    checker = BirthdayChecker()
    checker.add_birthday("Emily", "1991-07-04")
    checker.add_birthday("Ben", "1991-07-05")
    checker.add_birthday("Angelica", "1991-07-06")
    checker.add_birthday("Harry", "2001-04-15")
    assert checker.find_upcoming_birthdays() == [{"name": "Harry", "dob": "2001-04-15", "sent": False}]

# """
# Return a list of birthdays upcoming within the next 7 days.
# """
# checker = BirthdayChecker()
# checker.add_birthday("Emily", "1991-07-04")
# checker.add_birthday("Ben", "1991-07-05")
# checker.add_birthday("Angelica", "1991-07-06")
# checker.add_birthday("Harry", "2001-04-15")
# checker.find_upcoming_birthdays() => [{"name": "Harry", "dob": "2001-04-15", "sent": False}]
#
# """
# For people in checker.find_upcoming_birthdays(), return each person's age in years, as a list of ints.
# """
# checker = BirthdayChecker()
# checker.add_birthday("Emily", "1991-07-04")
# checker.add_birthday("Ben", "1991-07-05")
# checker.add_birthday("Angelica", "1991-07-06")
# checker.add_birthday("Harry", "2001-04-15")
# upcoming_birthdays = checker.find_upcoming_birthdays()
# upcoming_birthdays.calculate_age() => [23]
#
# """
# For a specific entry in self.birthdays, set 'sent' to True.
# """
# checker = BirthdayChecker()
# emily = checker.add_birthday("Emily", "1991-07-04")
# emily.mark_sent() => 'sent' is True
