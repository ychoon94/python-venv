#Primes = [2,3,5,6,11,13]
#Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# print(Rainbow[0])
#
# for i in range(len(Rainbow)):
#    print(Rainbow[i])

import sys

#a = []  # start an empty list
# read number of element in the list
    # or
    # a.appent(int(input()))
#print(a)
#integer = 10
#try:
#    if(a.pop(a.index(integer))):
#        print("Success")
#        print(a)
#except ValueError:
#    print("Please try again")

#if(a.pop(index)):
#    print("Success")
#    print(a)
#else:
#    print("Fail")
#if(a.remove(100)):
#    print("success")
#else:
#    print("Fail")
a = []
print(a)
a.append([])
n = int(input('how many item in the list?'))

for k in range(n):
    new_element = int(input())  # read next element
    a[0].append(new_element)  # add into list

a[0].remove(12)
print(a)
