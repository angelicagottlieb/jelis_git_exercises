from lib.cohort import *
from lib.student import *
from datetime import datetime, date 

class CohortRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(item)
        return cohorts
    
    def find(self, cohort_id):
        rows = self._connection.execute('SELECT * from cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row["id"], row["name"], row["starting_date"])
    
    def find_with_students(self, cohort_id):
        rows = self._connection.execute("SELECT cohorts.id as cohort_id, cohorts.name, cohorts.starting_date, students.id AS student_id, students.student_name FROM cohorts JOIN students ON cohorts.id = students.cohort_id WHERE cohort_id = %s", [cohort_id])
        students = []
        for row in rows:
            student = Student(row["student_id"], row["student_name"], row["cohort_id"])
            students.append(student)
        return Cohort(rows[0]["cohort_id"], rows[0]["name"], rows[0]["starting_date"], students)

        