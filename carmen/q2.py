from timeit import repeat

def run_sorting_algorithm(algorithm,list):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({list})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number =10)

    print(f"Algorithm: {algorithm}. Minimum runtime taken: {min(times)}")


def Bubble_Sort(list1):
    n = len(list1)

    for i in range(n):
        swapped = False
        x = 0
        while x<len(list1)-1:
            if list1[x]>list1[x+1]:
                list1[x],list1[x+1] = list1[x+1],list1[x]
                swapped = True
            x += 1
        if swapped == False:
            break
    return list

def Bubble_Sort(list1,asc=True):
    lst = list(list1)
    for passesLeft in range(len(lst)-1, 0, -1):
        for i in range(passesLeft):
            if asc:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

if __name__ == '__main__':
    list1 = [2,4,5,7,8,10,12,25,30,40,50,60,70,100,100,10000,12333123,123123123123213,12312312313123123]
    print(Bubble_Sort(list1,asc=True))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list1)
    print(Bubble_Sort(list1,asc=False))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list1)
