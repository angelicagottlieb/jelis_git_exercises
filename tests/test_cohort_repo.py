from lib.cohort_repo import *
from lib.cohort import *
from datetime import datetime, date
from lib.student import *


def test_list_all_scohorts(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohorts = repository.all()
    assert cohorts == [Cohort(1, 'Cohort 1', date(2023, 5, 1)), Cohort(2, 'Cohort 2', date(2022, 4, 1))]


def test_get_single_record_socials(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort = repository.find(2)
    assert cohort == Cohort(2, 'Cohort 2', date(2022, 4, 1))

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, 'Cohort 1', date(2023, 5, 1), [Student(1, "Jeli", 1)])



