# Main Program

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

    main(hashO, hashRV)

    with open('hashowner.txt', 'wb') as output:
        pickle.dump(hashO, output, pickle.HIGHEST_PROTOCOL)
    with open('hashregvehicle.txt', 'wb') as output:
        pickle.dump(hashRV, output, pickle.HIGHEST_PROTOCOL)
