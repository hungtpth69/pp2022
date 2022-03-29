nStudents = int (input ("Number of Students: "))

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
    
print("\nStudents List: ")
for s in studentList:
    print(s.description())
    

nCourses = int(input ("Number of Courses: "))
    
class Course:
    
    def __init__(self):
        course_id = input ("Course id: ")
        course_name = input ("Course name: ")
        
        self.id = course_id
        self.name = course_name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
        
    def description(self):
        return f"{self.id} - {self.name}"
    
courseList = []

for i in range (nCourses):
    course = Course()
    courseList.append(course)
    
print("\nCourses List: ")
for c in courseList:
    print(c.description())

def find_course(courseList):
    while True:
        course_id = input ("Course id: ")
        for i in courseList:
            if i.get_id() == course_id:
                return i
        print('Invalid course id!')
    
def inputMark(courseList, studentList, studentMarks):

    course = find_course(courseList)

    for i, student in enumerate(studentList):
        mark = input(f"Mark for {student.get_name()}: ")
        studentMarks[i][course.get_id()] = mark


def CourseMark(studentMarks):
    print(studentMarks)
    
inputMark(courseList, studentList, studentMarks)
inputMark(courseList, studentList, studentMarks)

CourseMark(studentMarks)