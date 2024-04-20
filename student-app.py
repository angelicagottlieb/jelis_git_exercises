# file: app.py

from lib.cohort_repo import *
from lib.cohort import *
from lib.database_connection import DatabaseConnection
from lib.student import *

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/student_directory_2.sql")
        self.cohort_repository = CohortRepository(self._connection)
        
    def run(self):
        cohort = self.cohort_repository.find_with_students(1)
        print(cohort)


if __name__ == '__main__':
    app = Application()
    app.run()
