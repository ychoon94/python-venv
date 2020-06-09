import random
import timeit
from os import system, name


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def pause():
    try:
        input("Press Enter to continue...")
    except SyntaxError:
        pass


def this_is_a_dashing_line():
    print("----------------------------------------------------------")
    print("\n")


def bubbleSort(array, option):
    # we minus 1 because we are always comparing the current
    # value with the next value
    lengthOfArray = len(array) - 1
    # numbe of rounds will be the total length - 1, for array with length 5,
    # we will do 4 rounds: 0 and 1, 1 and 2, 2 and 3, 3 and 4.
    for i in range(lengthOfArray):
        # at each round, we compare the current j with the next value
        for j in range(lengthOfArray - i):
            if option == 1:  # sort ascending
                # only swap their positions if left value < right value as
                # we aim to move all the small values to the back
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            elif option == 2:  # sort descending
                # only swap their positions if left value > right value as
                # we aim to move all the small values to the back
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

    return array


def insertionSort(array, option):
    for i in range(1, len(array)):
        # element to be compared
        current = array[i]

        # comparing the current element with the sorted portion and swapping
        if option == 1:
            while i > 0 and array[i-1] > current:  # sort ascending
                array[i] = array[i-1]
                i = i-1
                array[i] = current
        elif option == 2:
            while i > 0 and array[i-1] < current:  # sort descending
                array[i] = array[i-1]
                i = i-1
                array[i] = current

    return array


def mergeSort(L):
    array = []
    if len(L) == 1:
        return L
    mid = len(L) // 2

    sublist1 = mergeSort(L[:mid])

    sublist2 = mergeSort(L[mid:])

    x, y = 0, 0
    while x < len(sublist1) and y < len(sublist2):
        if sublist1[x] > sublist2[y]:  # < for descending
            array.append(sublist2[y])
            y = y + 1

        else:
            array.append(sublist1[x])
            x = x + 1

    array = array + sublist1[x:]

    array = array + sublist2[y:]
    return array


def reverseMergeSort(array):
    newList = []
    if len(array) == 1:
        return array
    mid = len(array) // 2

    sublist1 = reverseMergeSort(array[:mid])

    sublist2 = reverseMergeSort(array[mid:])

    x, y = 0, 0
    while x < len(sublist1) and y < len(sublist2):
        if sublist1[x] < sublist2[y]:  # < for descending
            newList.append(sublist2[y])
            y = y + 1

        else:
            newList.append(sublist1[x])
            x = x + 1

    newList = newList + sublist1[x:]

    newList = newList + sublist2[y:]

    return newList


def ascendingList():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20]
    return mylist


def descendingList():
    mylist = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4,
              3, 2, 1]
    return mylist


def randomList():
    mylist = []
    random.seed(1)
    for i in range(20):
        mylist.append(random.randint(1, 100))
    return mylist


def showMenuOuter():
    print("Please choose a sorting method to perform: ")
    print("1. Insertion Sort")
    print("2. Bubble Sort")
    print("3. Merge Sort")
    print("4. Exit System")


def showMenuInner():
    print("Please choose a list to perform sorting method: ")
    print("1. Ascending Order List")
    print("2. Descending Order List")
    print("3. Random Order List")
    print("4. Return to main menu")


def showMenuInnerMost():
    print("Please choose the order to perform sorting method: ")
    print("1. Ascending Order")
    print("2. Descending Order")
    print("3. Return to previous menu")


def optionOuter():
    while True:
        clear()
        showMenuOuter()
        try:
            choice1 = int(input("Choice: "))
        except ValueError:
            print("Enter number only.\n")
            pause()
            continue

        if choice1 == 1:
            clear()
            optionInner(choice1)

        elif choice1 == 2:
            clear()
            optionInner(choice1)

        elif choice1 == 3:
            clear()
            optionInner(choice1)

        elif choice1 == 4:
            clear()
            print("Thank you for using XYZ sorting system.\n")
            return False
        else:
            print("Choose option 1-4 only.\n")


def optionInner(choice1):
    while True:
        clear()
        showMenuInner()
        try:
            choice2 = int(input("Choice: "))
        except ValueError:
            print("Enter number only.\n")
            pause()
            continue

        if choice2 == 1:
            clear()
            optionInnerMost(choice1, choice2)

        elif choice2 == 2:
            clear()
            optionInnerMost(choice1, choice2)

        elif choice2 == 3:
            clear()
            optionInnerMost(choice1, choice2)

        elif choice2 == 4:
            clear()
            return False
        else:
            print("Choose option 1-4 only.\n")


def optionInnerMost(choice1, choice2):
    while True:
        clear()
        showMenuInnerMost()
        try:
            choice3 = int(input("Choice: "))
        except ValueError:
            print("Enter number only.\n")
            pause()
            continue

        if choice3 == 1:
            if choice1 == 1 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = insertionSort(ascendingList(), choice3)
                print("Sorted List = {}" .format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 1 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = insertionSort(descendingList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 1 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = insertionSort(randomList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 2 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(ascendingList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 2 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(descendingList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 2 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(randomList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 3 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = mergeSort(ascendingList())
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 3 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = mergeSort(descendingList())
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 3 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = mergeSort(randomList())
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

        elif choice3 == 2:
            if choice1 == 1 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = insertionSort(ascendingList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 1 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = insertionSort(descendingList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 1 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = insertionSort(randomList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 2 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(ascendingList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 2 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(descendingList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 2 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = bubbleSort(randomList(), choice3)
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 3 and choice2 == 1:
                clear()
                print("Original List = {}" .format(ascendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = reverseMergeSort(ascendingList())
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 3 and choice2 == 2:
                clear()
                print("Original List = {}" .format(descendingList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = reverseMergeSort(descendingList())
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

            elif choice1 == 3 and choice2 == 3:
                clear()
                print("Original List = {}" .format(randomList()))
                this_is_a_dashing_line()
                starttime = timeit.default_timer()
                sortedList = reverseMergeSort(randomList())
                print("Sorted List = {}".format(sortedList))
                print("It took {} second to finish sorting."
                      .format(timeit.default_timer() - starttime))
                pause()

        elif choice3 == 3:
            clear()
            return False
        else:
            print("Choose option 1-3 only.\n")


if __name__ == "__main__":
    optionOuter()
