from datetime import datetime
from dateutil.relativedelta import *

def user_access(birth_date):

    if type(birth_date) != str:
        raise Exception("Wrong input type.")
    try:
        your_birth_date = datetime.strptime(birth_date,"%Y-%m-%d")
    except:
        raise Exception("Wrong input format.")
    
    today = datetime.today().date()
    your_birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    age = relativedelta(today, your_birth_date)
    age_years = age.years
    if age_years < 16:
        return f"Access is denied. You are {age_years} years old. You need to be 16 to use this service."
    if age_years >= 16:
        return "Access granted!"


#COULD ALSO TAKE OFF FIRST IF BECAUSE THEN IF IT"S WRONG TYPE IT ALSO WONT WORK!!!
#e.g.
#just 
# try:
    #     your_birth_date = datetime.strptime(birth_date,"%Y-%m-%d")
    # except:
    #     raise Exception("Wrong input format or type.")

# upcoming_birthdays = []
# today_date = datetime.today().date()
# seven_days_from_now = timedelta(days=7) + today_date 
# for person in self_birthdays:
#     dob_without_year = person["dob"].replace(year=today_date.year).date()
#     if today.date <= dob_without_year <= seven_days_from_now:
#         upcoming_birthdays.append(person)