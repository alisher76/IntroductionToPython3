
# If elif else statements

weekday = input("Please provide any weekday in number(1-7): ")

if weekday == "1":
    print("Its Monday")
elif weekday == '2':
    print("Tuesday")
elif weekday == '3':
    print("Wednesday")
elif weekday == '4':
    print("Thursday")
elif weekday == '5':
    print("Friday")
elif weekday == '6':
    print("Saturday")
elif weekday == '7':
    print("Sunday")
else:
    print("Please provide valid number: ")


temperature = input("Please provide temperature: ")

if int(temperature) < 10:
    print("Please wear all you got, its cold as hell")
elif int(temperature) < 32:
    print("Wear hat you should be fine")
elif int(temperature) < 50:
    print("Wear t shirts man")
elif int(temperature) > 50:
    print("Wear nothing if u wish to")
else:
    "Please provide valid temperature \n"


# guess number
num=10
guess = int(input("Please guess a number: "))
if guess != num:
    if guess < num:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input(": "))

    if guess == num:
        print("Well done u guessed it")
    else:
        print("Sorry you ran out of chance")
else:
    print("Wow you guessed it right away")