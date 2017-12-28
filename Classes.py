students = []


class Student:  # Upper case for naming Classes

    # Class Attribute
    school_name = "Springfield Elementary"

    # Construction is a __init__: creates custom constructer
    # self is the way we refer to our class from out class

    def __init__(self, name, student_id=332):  # default value for student id given in the arg
        self.name = name
        self.student_id = student_id
        students.append(self)  # Append self

    # str to give us better print result, method override
    def __str__(self):
        return "Student " + self.name

    def get_school_name(self):
        return "School Name: " + self.school_name

    def get_name_capitilized(self):
        return self.name.capitalize()


student = Student("Alisher")
print(student.get_school_name())
print(student)


# Inheritance

class HighSchoolStudent(Student):
    school_name = "Springfield High School"  # Overriding parent classes attribute

    def get_school_name(self):  # overriding parent class method
        return "This is a high school student {}".format(self.name)

    def get_name_capitilized(self):
        original_value = super().get_name_capitilized()  # Accessing super class method and modifying it
        return original_value + "-HS"


james = HighSchoolStudent("James")
print(james.get_school_name())
