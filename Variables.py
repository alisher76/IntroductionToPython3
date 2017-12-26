# When program runs everything will get to stored somewhere in the memory
# When we create a variable by giving a name for instance fruit="apple"
# memory allocates storage for it
# we can name variables like: greeting = "Hello", _myage = 26, ali_job_title = "software engineer"


# converting in python
age = 25 # whole number Integer
name = "Alisher"
salary = 50.550 # Float number
print(name + " is " + str(age) + " years old.")

# Math Operators basic calculations

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) # gives us float number
print(a // b) # gives us integer whole number
print(a % b) # gives us a remainder

for i in range(1, a//b):
    print(i)

# little complex calculation demonstration
print((((a + b) / 3) -4) *12)

# Accessing String
language = "Python Programming Language"
print(language)
print(language[0])
print(language[5] + " show 5th char")
print(language[-1] + " show 2nd char from right side")
print(language[0:6] + " show up to 6 chars")
print(language[:6] + " show 6 chars")
print(language[6:] + " show from the 6th  char")
print(language[0:6:2] + " skip 2 up to 6th character ")

# we can also multiply strings in python
greeting = "Hello"
print(greeting *2) # prints hello 2 times
# useful built in tool in python is in
print("He" in greeting) # prints True which indicates that greeting has that string
print("l" in greeting)
print("false" in greeting) # will print false as greeting variable does not have that false word