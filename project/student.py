class Student():
    def __init__(self, name, lastname, id, courses, attendance):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.courses = courses
        self.attendance = attendance

    def get_name(self):
        return self.name + ' ' + self.lastname
    
    def get_courses(self):
        return self.courses
    
    def get_attendance(self):
        return self.attendance

    def get_id(self):
        return self.id