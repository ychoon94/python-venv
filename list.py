#Primes = [2,3,5,6,11,13]
#Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# print(Rainbow[0])
#
# for i in range(len(Rainbow)):
#    print(Rainbow[i])

a = []  # start an empty list
# read number of element in the list
n = int(input('how many item in the list?'))
for i in range(n):
    new_element = int(input())  # read next element
    a.append(new_element)  # add into list
    # or
    # a.appent(int(input()))
print(a)
