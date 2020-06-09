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
