nStudents = int (input ("Number of Students: "))
    
nCourses = int(input ("Number of Courses: "))
    
def inputStudentInfo ():
    sid = input ("Student id: ")
    sname = input ("Student name: ")
    sdob = input ("Student's dob (d/m/y): ")
    return sid, sname, sdob

def inputCourseInfo ():
    cid = input ("Course id: ")
    cname = input ("Course name: ")
    return cid, cname    
    
def getMarks (sid, cid):
    prompt = f"Enter marks for student {sid} for course {cid}: ".format (sid, cid)
    input (prompt)

studentLst = []
for i in range (nStudents):
    sid, sname, dob = inputStudentInfo ()
    studentLst.append ((sid, sname, dob))

courseLst = []
for i in range (nCourses):
    cid, cname = inputCourseInfo ()
    courseLst.append ((cid, cname))
    
d = {}    
n = int (input ("Number of student's marks in the course: "))
for i in range (n):
    while True:
        sid = input ("Student id: ")
        cid = input ("Course id: ")
        if sid not in [student [0] for student in studentLst]:
            print ("Invalid student id")
            continue 
        if cid not in [course [0] for course in courseLst]:
            print ("Invalid course id")
            continue 
        break
    marks = float (input ("Input marks for course: "))
    if cid in d:
        d [cid].append ((sid, marks))
    else:
        d [cid] = [(sid, marks)]
        
print ("\nStudents list: ")
for s in studentLst:
    print (f"Student id: {s[0]} Name: {s[1]} Date of birth: {s[2]}")

print ("\nCourses list: ")
for c in courseLst:
    print (f"Course id: {c[0]} Name: {c[1]}")
    
cid = input ("\nCourse id showing students'marks in the course: ")
if cid in d:
        for tups in d [cid]:
            print (f"Student {tups[0]} got {tups [1]} marks")