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
