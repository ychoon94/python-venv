import random

random.seed(None)

for i in range(1):
    print(random.randint(0, 9))

a = []
index = 5

for i in range(10):
    a.append([])

a.insert(-1, 10)
print(a)
a.remove(10)
print(a)

if a[8]:
    print("list is not empty")
else:
    print("List is empty")


def double_hashing(keys, hashtable_size, double_hash_value):
    hashtable_list = [None] * hashtable_size
    counter = 0
    for i in range(len(keys)):
        hashkey = keys[i] % hashtable_size
        if hashtable_list[hashkey] is None:
            hashtable_list[hashkey] = keys[i]
        else:
            new_hashkey = hashkey
            counter += 1
            while hashtable_list[new_hashkey] is not None:
                steps = double_hash_value - (keys[i] % double_hash_value)
                new_hashkey = (new_hashkey + counter*steps) % hashtable_size  # problem 1 is here
            hashtable_list[new_hashkey] = keys[i]
    return hashtable_list  # problem 2 is here


values = [100, 70, 10, 1]
print(double_hashing(values, 10, 7))

#[26, None, 54, 94, 17, 31, 44, 51, None, None, None, None, 77]
