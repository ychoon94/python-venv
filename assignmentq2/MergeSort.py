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
