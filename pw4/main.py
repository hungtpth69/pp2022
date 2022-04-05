from domains.Student import Student
from domains.Course import Course

studentList = []
studentMarks = []
courseList = []

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