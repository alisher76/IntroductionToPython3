for i in range(1, 5):
    print("i is now {}".format(i))

name = "Alisher Abdukarimov"
vowelOnlyName = ''
vowelLessName = ''
for i in range(0, len(name)):
    if name[i] in 'auoei':
        vowelOnlyName = vowelOnlyName + name[i]
    else:
        vowelLessName = vowelLessName + name[i]

print(vowelOnlyName)
print(vowelLessName)

# wroking with arrays/lists/sequence
for state in ['is actively looking for job', 'is actively interviewing', 'doing freelance jobs', 'got a job']:
    print(name + " {}".format(state))

# 10 numbers times tables
for i in range(1, 11):
    for j in range(1, 11):
        print("{1} times {0} is {2}".format(i, j, i * j))

    print("======================")

# Continue Break and else

shoppingList = ['milk', 'pasta', 'eggs', 'bologna', 'bread', 'spread', 'rice']
for item in shoppingList:
    if item == 'bologna':
        continue  # when finds item continues to the next item leaving that item out // if we use break instead it will
        # exit out loop and stop going through the list
    print(item)  # prints without bologna

# Break use
songs = ["Thriller", "Go home", "Love you", "Hate", "My World"]
for song in songs:
    if song == "Hate":
        cant_listen_anymore = "song"
        break
    else:
        print("Love listening to {}".format(song))
if cant_listen_anymore:
    print("Why man now I cant hear any other songs cuz of you song named: {}".format(song))

# While loop
guessed = 0

while guessed == 0:
    guess = input("Guess my favorite number: ")
    if guess == "7":
        print("You got it!")
        guessed = 1
    else:
        print("Nope, that’s not it!")
