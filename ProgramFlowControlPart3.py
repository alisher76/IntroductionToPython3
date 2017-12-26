#
name = input("Hey, what is your name? ")
age = int(input("Good to meet you {}, What is your age? ".format(name)))

#if (age >= 16) and (age <= 65):
 # we can also use this way
if 15 < age < 65: # we also have or operator to check if one of the expressions is true
    print("Go to work and enjoy your adulthood")
else:
    print("Enjoy your free time")

# To  check if variable is empty
x = input("Please enter something: ")

if x: # in python ther is no Boolean type like in Swift or other languages
    # when a variable has a value it returns true
    print("You entered {}".format(x))
else:
    print("You entered nothing")

# we also have not operator that reverses true or false
if not(age < 18): # needs to be true
    print("You are old enough to vote")
else:
    print("Please come back in {} years".format(18 - age))


# We have gone over 'in' before but lets use it in one more case
letter = input("Please enter a letter to see if your name has it? lol )")

for letter in name: # if we use not in would give us the opposite result
    print("Give me an {0}, {1}".format(letter, name))
else:
    print("I care less about that letter")