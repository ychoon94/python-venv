# debug program

from Vehicle import *
from Person import *
from Hash import *
from Menu import *
from os import system, name
import pickle

if __name__ == "__main__":
    with open('hashowner.txt', 'rb') as input:
        hashO = pickle.load(input)
    with open('hashregvehicle.txt', 'rb') as input:
        hashRV = pickle.load(input)

    hashO.displayHash()

    owner = hashO.searchKey("123456-12-1234")

    print(len(owner.ownedVehicle))

    hashRV.displayHash()
