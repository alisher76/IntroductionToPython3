age = 24
print("My age is" + " " + str(age))
# isntead of converting data everyime like this python provides better solution in python 3

print("My age is {}".format(age))   # same output as the above example

# we can also give more than one parameter in replacement field

print("""
There are {2} days in January,
{0} in February,
{2} in March,
{1} in April,
{2} in May,
{1} in June,
{2} in July,
{2} in August,
{1} in September,
{2} in October,
{1} in November, 
and {2} in December
""".format(28, 30, 31))
# To format and spacing nicely we can use this technique
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))