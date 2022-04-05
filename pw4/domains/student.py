from domains.Student import Student

class Student:
    
    def __init__(self):
        student_id = input ("Student id: ")
        student_name = input ("Student name: ")
        DoB = input ("Student's dob (d/m/y): ")
        
        self.id = student_id
        self.name = student_name
        self.dob = DoB
        
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def description(self):
        return f"{self.id} - {self.name} - {self.dob}"
    
studentList = []
studentMarks = []

for i in range (nStudents):
    student = Student()
    studentList.append(student)
    studentMarks.append({"Student": student.id})