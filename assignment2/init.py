# Run this file first
# Program to initialise the save file.

from Vehicle import *
from Person import *
from Hash import *
from Menu import *
from os import system, name
import pickle

if __name__ == "__main__":
    with open('hashowner.txt', 'wb') as output:
        hashO = Hash(30)
        pickle.dump(hashO, output, pickle.HIGHEST_PROTOCOL)
    with open('hashregvehicle.txt', 'wb') as output:
        hashRV = Hash(30)
        pickle.dump(hashRV, output, pickle.HIGHEST_PROTOCOL)
