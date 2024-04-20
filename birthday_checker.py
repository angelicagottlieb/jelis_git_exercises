from datetime import datetime, timedelta
from dateutil import relativedelta


class BirthdayChecker:
    def __init__(self):
        self.birthdays = []

    def add_birthday(self, name, date_of_birth, sent=False):
        formatted_dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        self.birthdays.append({"name": name, "dob": formatted_dob, "sent": sent})

    def update_dob(self, name, new_dob):
        for person in self.birthdays:
            if person["name"] == name:
                person["dob"] = new_dob
                break

    def update_name(self, old_name, new_name):
        for person in self.birthdays:
            if person["name"] == old_name:
                person["name"] = new_name
                break

    def find_upcoming_birthdays(self):

    # upcoming_birthdays = []
    # today_date = datetime.today().date()
    # seven_days_from_now = today_date + timedelta(days=7)
    # for person in self.birthdays:
    #     dob_without_year = person["dob"].replace(year=today_date.year)
    #     # if today_date <= dob_without_year <= seven_days_from_now:
    #     if (dob_without_year - today_date).days <= 7:
    #         upcoming_birthdays.append(person)

    # Parameters: none
    # Returns: list of people whose birthdays will be in the next 7 days
    # Side effects: none

    def calculate_age(self):
        pass

    # Returns: person's age as an int
    # Side effects: none

    def mark_sent(self):
        pass
# Parameters: none
# Returns: nothing
# Side effects: sets 'sent' to True
