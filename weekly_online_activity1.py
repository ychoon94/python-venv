def generatingArray():
    timetable = [["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "210CT", "210CT", "210CT"],
                 ["220CT", "220CT", "260CT", "260CT",
                     "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["220CT", "220CT", "x", "x", "210CT", "x", "x", "A202SGI", "A202SGI", "x"]]

    return timetable


def q2PrintArray(x):
    print("q2: ")
    for i in range(len(x)):
        for j in range(len(x[i])):
            print(x[i][j], end=" ")
        print()
    print()


def q3a(x):
    print("q3a: ")
    repeat = 'x'
    for i in range(len(x[2])):
        if (x[2][i] != 'x'):
            if (repeat != x[2][i]):
                repeat = x[2][i]
                print(x[2][i], end=" ")
    print('\n')


def q3b(x):
    print("q2b: ")
    counter = 0
    for i in range(len(x[4])):
        if (x[4][i] != 'x'):
            counter += 1
    return counter


def q3c(x):
    print("q3c: ")
    checkClasses = 0
    for i in range(len(x[0])):
        if (x[0][i] != 'x'):
            checkClasses += 1

    if (checkClasses != 0):
        return "You have classes on Monday.\n"
    else:
        return "You have no classes on Monday.\n"


if __name__ == "__main__":

    # print(generatingArray())
    q2PrintArray(generatingArray())
    q3a(generatingArray())
    print("There is total of {} hours of classes to attend on Friday.\n" .format(
        q3b(generatingArray())))

