import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercises
from instructor import Instructor

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
            
    def all_cohorts(self):
        
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT c.Id, c.name
            FROM Cohort c
            """)
            
            all_cohorts = db_cursor.fetchall()
            
            [print(c) for c in all_cohorts]
            
    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(
                row[1], row[2])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Lang
            FROM Exercise e
            """)
            
            all_exercises = db_cursor.fetchall()
            
            [print(e) for e in all_exercises]

    def all_js_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(
                row[1], row[2])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Lang
            FROM Exercise e
            WHERE e.Lang LIKE 'Javascript'
            """)
            
            all_js_exercises = db_cursor.fetchall()
            
            [print(e) for e in all_js_exercises]

    def all_python_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(
                row[1], row[2])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Lang
            FROM Exercise e
            WHERE e.Lang LIKE 'Python'
            """)
            
            all_python_exercises = db_cursor.fetchall()
            
            [print(e) for e in all_python_exercises]

    def all_sql_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercises(
                row[1], row[2])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT e.Id, e.Name, e.Lang
            FROM Exercise e
            WHERE e.Lang LIKE 'SQL'
            """)
            
            all_sql_exercises = db_cursor.fetchall()
            
            [print(e) for e in all_sql_exercises]
            
    def students_and_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[0], row[1], row[2], row[3])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT s.Id, s.FirstName, s.LastName, c.Name
            FROM Student s
            LEFT JOIN Cohort c ON s.CohortId = c.Id
            ORDER BY s.CohortId
            """)
            
            students_cohorts = db_cursor.fetchall()
            
            [print(s) for s in students_cohorts]

    def instructors_and_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[0], row[1], row[2], row[3])
            
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT i.Id, i.FirstName, i.LastName, c.Name
            FROM Instructor i
            LEFT JOIN Cohort c ON i.CohortId = c.Id
            ORDER BY i.CohortId
            """)
            
            instructor_cohorts = db_cursor.fetchall()
            
            [print(i) for i in instructor_cohorts]
    
    def students_exercises(self):


        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            exercises = dict()

            db_cursor.execute("""
                SELECT
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.FirstName,
                    s.LastName
                FROM Exercise e
                JOIN StudentExercises se ON se.ExerciseId = e.Id
                JOIN Student s ON s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()
            
            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                
                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
                    

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')
                    
reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
# reports.all_js_exercises()
# reports.all_python_exercises()
# reports.all_sql_exercises()
# reports.students_and_cohorts()
# reports.instructors_and_cohorts()
reports.students_exercises()


# Display all cohorts.
# Display all exercises.
# Display all JavaScript exercises.
# Display all Python exercises.
# Display all C# exercises.
# Display all students with cohort name.
# Display all instructors with cohort name.