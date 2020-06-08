from timeit import repeat

def run_sorting_algorithm(algorithm,list):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    
    stmt = f"{algorithm}({list})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number =10)

    print(f"Algorithm: {algorithm}. Minimum runtime taken: {min(times)}")


def Bubble_Sort(list1,asc = True):
    lst = list(list1)
    for passLeft in range(len(lst)-1, 0, -1):
        for x in range(passLeft):
            if asc:
                if lst[x] > lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
            else:
                if lst[x] < lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst

def Insertion_Sort(list1,desc = True):
    lst = list(list1)
    for passLeft in range(len(lst)-1, 0, -1):
        for i in range(passLeft):
            if desc :
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def Bubble_Sort(list2,asc = True):
    lst = list(list2)
    for passLeft in range(len(lst)-1, 0, -1):
        for x in range(passLeft):
            if asc:
                if lst[x] > lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
            else:
                if lst[x] < lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst


def Insertion_Sort(list2, desc = True):
    lst = list(list2)
    for passLeft in range(len(lst)-1, 0, -1):
        for i in range(passLeft):
            if desc :
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst




if __name__ == '__main__':
    # Bubble Sort and Insertion Sort List 1
    list1 = [2,4,5,7,8,10,12,25,28,34,45,60,80,87,94,99]
    print('Ascending Order ---> Ascending Order')
    print(Bubble_Sort(list1,asc=True))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list1)
    print(Insertion_Sort(list1,desc=False))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list1)

    print(' ')
    print('Ascending Order ---> Descending Order')
    print(Bubble_Sort(list1,asc=False))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list1)
    print(Insertion_Sort(list1,desc=True))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list1)
    print(' ')
    
    # Bubble Sort and Insertion Sort List 2
    list2 = ['Zac','Yong','Wil','Treasure','Seesaw','Rihanna','Philip','Nelson','Lee','Hilson','Forest','Carmen','Alice']
    print('Descending Order ---> Descending Order')
    print(Bubble_Sort(list2,asc=False))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list2)
    print(Insertion_Sort(list2,desc=True))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list2)
    
    print(' ')
    print('Descending Order ---> Ascending Order')
    print(Bubble_Sort(list2,asc=True))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list2)
    print(Insertion_Sort(list2,desc=False))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list2)


    




    
