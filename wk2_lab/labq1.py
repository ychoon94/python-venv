Mark = []
counter = 0
tempo = 0
i = 0

while i < 10:
    userInput = int(input("Please enter mark from 1-100: "))

    if (userInput <= 100) and (userInput >= 0):
        Mark.append(userInput)
        print('\n')
        i += 1
    else:
        print("Please only enter value between 1 and 100.\n")
        i = i

for j in range(len(Mark)):
    if (Mark[j] >= tempo):
        tempo = Mark[j]
        counter = j + 1
    else:
        tempo = tempo
        counter = counter

print("The largest number {0} is stored at {1} location of the array".format(
    tempo, counter))
