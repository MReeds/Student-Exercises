from exercise import Exercises
from cohort import Cohort
from student import Student
from instructor import Instructor

exercise1 = Exercises("Exercise 1", "HTML")
exercise2 = Exercises("Exercise 2", "JavaScript")
exercise3 = Exercises("Exercise 3", "React")
exercise4 = Exercises("Exercise 4", "Python")

cohort38 = Cohort("Day Cohort 38")
cohort39 = Cohort("Day Cohort 39")
cohort40 = Cohort("Day Cohort 40")

student1 = Student("Matt", "Reeds", "MReeds")
student2 = Student("Tyler", "Weinhoff", "TWeinhoff")
student3 = Student("Jack", "Nichols", "JNickels")
student4 = Student("Jason", "Borne", "JBorne")

cohort38.students.append(student1)
cohort39.students.append(student2)
cohort40.students.append(student3)
cohort38.students.append(student4)

instructor1 = Instructor("Andy", "Collins", "ACollins")
instructor2 = Instructor("Jisie", "David", "JDavid")
instructor3 = Instructor("Steve", "Brownlee", "SBrownlee")

cohort38.instructors.append(instructor1)
cohort39.instructors.append(instructor2)
cohort40.instructors.append(instructor3)

instructor1.assign_assignment(student1, exercise1)
instructor1.assign_assignment(student1, exercise2)

instructor1.assign_assignment(student2, exercise1)
instructor1.assign_assignment(student2, exercise2)

instructor1.assign_assignment(student3, exercise3)
instructor1.assign_assignment(student3, exercise4)

instructor1.assign_assignment(student4, exercise3)
instructor1.assign_assignment(student4, exercise4)

students = [student1, student2, student3, student4]
exercises = [exercise1, exercise2, exercise3, exercise4]

for student in students:
  student.student_summary()
