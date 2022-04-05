import math
from domains.Student import Student
from domains.Course import Course

nStudents = int (input ("Number of Students: "))

nCourses = int(input ("Number of Courses: "))

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