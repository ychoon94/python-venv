Number = []
counterEven = 0
counterOdd = 0

for i in range(5):
    userInput = int(input("Please enter integers: "))
    Number.append(userInput)

for j in range(5):
    if (Number[j] % 2 != 0):
        counterOdd += 1
    else:
        counterEven += 1

print("There are a total of {} of Odd number in the array.".format(counterOdd))
print("There are a total of {} of Even number in the array.".format(counterEven))
