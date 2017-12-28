# First way

# import Classes
#
# james = Classes.HighSchoolStudent("James")
# print(james.get_school_name())

# most common way
# from Classes import * imports everything from that file

from Classes import HighSchoolStudent

james = HighSchoolStudent("James")
print(james.get_school_name())