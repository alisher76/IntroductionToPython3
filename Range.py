# Using exceptions

student = {
    "name": "Alisher",
    "student-id": 1991,
    "feedback": None
}

student["last_name"] = "Abdukarim"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I cant add these two together")
    print(error)