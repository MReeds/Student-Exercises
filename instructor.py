from NSSPerson import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack):
        super().__init__(first_name, last_name, slack)
        self.specialty = ""
        
    def assign_assignment(self, student, assignment):
        student.exercises.append(assignment)