from NSSPerson import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack):
        super().__init__(first_name, last_name, slack)
        self.exercises = list()
            
    def student_summary(self):
        print("\n--- STUDENT SUMMARY ---")
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Slack Handle: {self.slack}")
        print("Exercises Assigned:")
        for exercise in self.exercises:
            print(f" - {exercise.name}")