import sqlite3
from student import Student

class StudentExerciseReports():
    def __init__(self):
        self.db_path = "/home/matt_reeds/backend/intro/StudentExercises/studentExercises.db"
        
    def all_students(self):
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT s.Id,
                s.FirstName,
                s.LastName,
                s.Slack,
                s.CohortId,
                c.name
            FROM Student s
            JOIN Cohort c ON s.CohortId = c.Id
            ORDER BY s.CohortId
            """)
            
            all_students = db_cursor.fetchall()
            
            [print(s) for s in all_students]
            
reports = StudentExerciseReports()
reports.all_students()