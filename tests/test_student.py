from lib.student import *
from datetime import datetime , date


def test_student_constructs():
    student = Student(1, "Jeli", 2)
    assert student.id == 1
    assert student.student_name == "Jeli"
    assert student.cohort_id == 2


def test_construct_formats_nicely():
    student = Student(1, "Jeli", 2)
    assert str(student) == "Student(1, Jeli, 2)"

def test_cohorts_are_equal():
    student1 = Student(1, "Jeli", 2)
    student2 = Student(1, "Jeli", 2)
    assert student1 == student2