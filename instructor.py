from NSSPerson import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__(first_name, last_name, slack)
        self.specialty = ""
        self.cohort = cohort
        
    def assign_assignment(self, student, assignment):
        student.exercises.append(assignment)
        
    def __repr__(self):
        return f"{self.first_name} {self.last_name} instructs {self.cohort}"