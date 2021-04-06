from .person import Person

class Student(Person):
    def __init__(self, first_name, last_name, email, student_id, average):
        Person.__init__(self, first_name, last_name, email)
        self.student_id = student_id
        self.average = average
    