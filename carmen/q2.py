from timeit import repeat

def run_sorting_algorithm(algorithm,list): #run_sorting_algorithm() is to get the name of the algorithm and the input of list
    #set up the context and call to the specified sorting algorithm
    #only import the algorithm function 
    system_setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    
    stmt = f"{algorithm}({list})" #Ready to call the sorting algorithm with the input list.

    # To call timeit.repeat() with the setup code and the sentence
    # This will execute the specified sorting algorithm five times
    # and return the number of seconds each one of the executions take. 
    times = repeat(setup = system_setup_code, stmt = stmt, repeat = 3, number = 5)

    # To identify the minimum runtime taken
    # and display the name of the sorting algorithm 
    print(f"Algorithm: {algorithm}. Minimum runtime taken: {min(times)}") 


def Bubble_Sort(list1,asc = True):
    lst = list(list1) #copy to list1
    for passLeft in range(len(lst)-1, 0, -1): #repeating loop the total number of items in list and compare the adjacent item by minus 1
        for x in range(passLeft):
            if asc: # for ascending order
                if lst[x] > lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
            else: # for descending order
                if lst[x] < lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst

def Insertion_Sort(list1,desc = True):
    lst = list(list1)
    for passLeft in range(len(lst)-1, 0, -1):
        for i in range(passLeft):
            if desc : # for descending order
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else: # for ascending order
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def merge(left, right):
    # Nothing to merge if the first list is empty,
    # and return the result of the second list
    if len(left) == 0:
        return right

    # Nothing to merge if the second list is empty,
    # and return the result of the first list
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Look through both lists and make it into the result list
    while len(result) < len(left) + len(right):
        # Compare the items at the head of both lists, and select the smallest value and append it to end of the result list
        # You can decide whether to get the next item from the first or the second list
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # Append any remaining items from another list to the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break


    return result


def Merge_Sort(list1):
    # Make sure that the list not contains less than two items
    # If less than two items, return it as the result of the function
    if len(list1) < 2:
        return list1

    midpoint = len(list1) // 2 # Calculate the middle point of the list

    # Sort the list by recursively 
    # Split the list into two equal halves
    # Sort each half of them and merge them together into the final result
    return merge(
        left=Merge_Sort(list1[:midpoint]),
        right=Merge_Sort(list1[midpoint:]))

    
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


def Merge_Sort(list2):
    if len(list2) < 2:
        return list2

    midpoint = len(list2) // 2

    return merge(
        left=Merge_Sort(list2[:midpoint]),
        right=Merge_Sort(list2[midpoint:]))

def Bubble_Sort(list3,asc = True):
    lst = list(list3)
    for passLeft in range(len(lst)-1, 0, -1):
        for x in range(passLeft):
            if asc:
                if lst[x] > lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
            else:
                if lst[x] < lst[x + 1]:
                    lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst

def Insertion_Sort(list3,desc = True):
    lst = list(list3)
    for passLeft in range(len(lst)-1, 0, -1):
        for i in range(passLeft):
            if desc :
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def Merge_Sort(list3):
    if len(list3) < 2:
        return list3

    midpoint = len(list3) // 2

    return merge(
        left=Merge_Sort(list3[:midpoint]),
        right=Merge_Sort(list3[midpoint:]))




if __name__ == '__main__':
    print('-----------------------------------------------------------------------------')
    print('                    [[[[Ascending Order List]]]                                     ')
    print(' ')
    # Bubble Sort, Insertion Sort, and Merge Sort of List 1
    list1 = [2,4,5,7,8,10,12,25,28,34,45,60,80,87,94,99]
    print('List 1:',list1)
    print(' ')
    print('Bubble Sort Ascending Order')
    print('Ascending Order List ---> Ascending Order List')
    print(Bubble_Sort(list1,asc=True))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list1)
    print(' ')
    print('Insertion Sort Ascending Order')
    print('Ascending Order List ---> Ascending Order List')
    print(Insertion_Sort(list1,desc=False))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list1)
    print(' ')

    print('Bubble Sort Descending Order')
    print('Ascending Order List ---> Descending Order List')
    print(Bubble_Sort(list1,asc=False))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list1)
    print(' ')
    print('Insertion Sort Descending Order')
    print('Ascending Order List ---> Descending Order List')
    print(Insertion_Sort(list1,desc=True))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list1)
    print(' ')

    print('Merge Sort')
    print(Merge_Sort(list1))
    run_sorting_algorithm(algorithm= "Merge_Sort", list = list1)
    
    print('-----------------------------------------------------------------------------')
    print('                    [[[[Descending Order List]]]                                     ')
    print(' ')
    # Bubble Sort, Insertion Sort, and Merge Sort of List 2
    list2 = ['Zac','Yong','Wil','Treasure','Seesaw','Rihanna','Philip','Nelson','Lee','Hilson','Forest','Carmen','Alice']
    print('List 2:',list2)
    print(' ')
    
    print('Bubble Sort Descending Order')
    print('Descending Order List ---> Descending Order List')
    print(Bubble_Sort(list2,asc=False))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list2)
    print(' ')
    print('Insertion Sort Descending Order')
    print('Descending Order List ---> Descending Order List')
    print(Insertion_Sort(list2,desc=True))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list2)
    print(' ')

    print('Bubble Sort Ascending Order')
    print('Descending Order List ---> Ascending Order List')
    print(Bubble_Sort(list2,asc=True))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list2)
    print(' ')
    print('Insertion Sort Ascending Order')
    print('Descending Order List ---> Ascending Order List')
    print(Insertion_Sort(list2,desc=False))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list2)
    print(' ')

    print('Merge Sort')
    print(Merge_Sort(list2))
    run_sorting_algorithm(algorithm= "Merge_Sort", list = list2)
    
    print('-----------------------------------------------------------------------------')
    print('                    [[[Random Order List]]]                                     ')
    print(' ')
    # Bubble Sort, Insertion Sort, and Merge Sort of List 3
    list3 = [45,12,23,89,78,6,19,43,66,52,100,93,1,75,10]
    print('List 3:',list3)
    print(' ')
    
    print('Bubble Sort Ascending Order')
    print('Random Order List ---> Ascending Order List')
    print(Bubble_Sort(list3,asc=True))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list3)
    print(' ')
    print('Insertion Sort Ascending Order')
    print('Random Order List ---> Ascending Order List')
    print(Insertion_Sort(list3,desc=False))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list3)
    print(' ')
    
    print('Bubble Sort Descending Order')
    print('Random Order List ---> Descending Order List')
    print(Bubble_Sort(list3,asc=False))
    run_sorting_algorithm(algorithm= "Bubble_Sort", list = list3)
    print(' ')
    print('Insertion Sort Descending Order')
    print('Random Order List ---> Descending Order List')
    print(Insertion_Sort(list3,desc=True))
    run_sorting_algorithm(algorithm= "Insertion_Sort", list = list3)
    print(' ')
    
    print('Merge Sort')
    print(Merge_Sort(list3))
    run_sorting_algorithm(algorithm= "Merge_Sort", list = list3)

    


    




    
