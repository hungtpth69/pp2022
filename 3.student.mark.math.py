import math


     
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
    
    
nCourses = int(input ("Number of Courses: "))
    
class Course:
    
    def __init__(self):
        course_id = input ("Course id: ")
        course_name = input ("Course name: ")
        course_credits = int(input("Course credits: "))
        self.id = course_id
        self.name = course_name
        self.credit = course_credits

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_credit(self):
        return self.credit
        
    def description(self):
        return f"{self.id} - {self.name} - {self.credit}"
    
courseList = []

for i in range (nCourses):
    course = Course()
    courseList.append(course)
    

def find_course(courseList):
    while True:
        course_id = input ("Input Course id to enter marks: ")
        for i in courseList:
            if i.get_id() == course_id:
                return i
        print('Invalid course id!')
    
def rounded_mark(num):
    num *= 10
    if num - math.floor(num) >= 0.5:
        return math.floor(num + 1) / 10
    return math.floor(num) / 10

def inputMark(courseList, studentList, studentMarks):

    course = find_course(courseList)

    for i, student in enumerate(studentList):
        mark = rounded_mark(float(input(f"Mark for {student.get_name()}: ")))
        studentMarks[i][course.get_id()] = mark
                                  
inputMark(courseList, studentList, studentMarks)


#GPA = sum(studentMarks*credits)/sum(credits)

def GPA(studentMarks, courseList):
    GPA = 0
    for i in studentMarks:
        for j in courseList:
            if i[j.get_id()] != None:
                GPA += i[j.get_id()] * j.get_credit()
    return GPA / sum(course.get_credit() for course in courseList)


while True:
        print("\n1. List all courses")
        print("2. List all students")
        print("3. List all marks")
        print("4. Student's GPA")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            for course in courseList:
                print("Course: ", course.description())
        elif choice == 2:
            for student in studentList:
                print("Student: ", student.description())
        elif choice == 3:
            for student in studentMarks:
                print(studentMarks)
        elif choice == 4:
            print("GPA: ", GPA(studentMarks, courseList))
        elif choice == 5:
            break
        else:
            print("Invalid choice")