
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332): #default value for student id given in the arg
    student = {"name": name, "student_id": student_id}
    students.append(student)



def read_file():
    try:
        file = open("students.txt", "r")
        for student in read_students(file):
            add_student(student)
        file.close()
    except Exception:
        print("Could not read file")


def read_students(file): # Generator functions 
    for line in file:
        yield line

def save_file(student):
    try:
        file = open("students.txt", "a")
        file.write(student + "\n")
        file.close()
    except Exception:
        print("Could not update file")

read_file()
print(print_student_titlecase())

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)