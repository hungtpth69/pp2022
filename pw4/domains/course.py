from domains.Course import Course

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