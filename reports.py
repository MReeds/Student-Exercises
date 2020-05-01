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
    
    def exercises_with_students(self):


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

    def students_with_exercises(self):


        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            students = dict()

            db_cursor.execute("""
                SELECT
                    s.Id,
                    s.FirstName,
                    s.LastName,
                    e.Id ExerciseId,
                    e.Name
                FROM Student s
                JOIN StudentExercises se ON se.StudentId = s.Id
                JOIN Exercise e ON e.Id = se.ExerciseId
            """)

            dataset = db_cursor.fetchall()
            
            for row in dataset:
                exercise_id = row[3]
                exercise_name = row[4]
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                
                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)
                    
            for student_name, exercises in students.items():
                print(f"{student_name} is working on: ")
                for exercise_name in exercises:
                    print(f'\t* {exercise_name}')

                    
    def assigned_by_instructors(self):

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            instructors = dict()

            db_cursor.execute("""
                SELECT 
                    i.Id,
                    i.FirstName,
                    i.LastName,
                    e.Id AS "ExerciseId",
                    e.Name AS "Exercise Name"
                FROM Instructor i
                JOIN StudentExercises se ON se.InstructorId = i.Id
                JOIN Exercise e ON se.Id = e.Id;
            """)

            dataset = db_cursor.fetchall()
            
            for row in dataset:
                exercise_id = row[3]
                exercise_name = row[4]
                instructor_id = row[0]
                instructor_name = f'{row[1]} {row[2]}'
                
                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    instructors[instructor_name].append(exercise_name)
                    
            for instructor_name, exercises in instructors.items():
                print(f"{instructor_name} is working on: ")
                for exercise_name in exercises:
                    print(f'\t* {exercise_name}')
                    
    def popular_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            exercises = dict()

            db_cursor.execute("""
                SELECT
                    s.Id,
                    s.FirstName,
                    s.LastName,
                    e.Id ExerciseId,
                    e.Name
                FROM Student s
                JOIN StudentExercises se ON se.StudentId = s.Id
                JOIN Exercise e ON e.Id = se.ExerciseId
            """)

            dataset = db_cursor.fetchall()
            
            for row in dataset:
                exercise_id = row[3]
                exercise_name = row[4]
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                
                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
                    
            for exercise_name, exercises in exercises.items():
                print(f"{exercise_name} is being worked on by: ")
                for student_name in exercises:
                    print(f'\t* {student_name}')
                    
reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
# reports.all_js_exercises()
# reports.all_python_exercises()
# reports.all_sql_exercises()
# reports.students_and_cohorts()
# reports.instructors_and_cohorts()
# reports.exercises_with_students()
# reports.students_with_exercises()
# reports.assigned_by_instructors()
reports.popular_exercises()
