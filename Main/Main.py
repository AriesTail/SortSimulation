import random
import sys

import pandas

from Sort.Sorts import SortMethonds


sys.setrecursionlimit(10000000)
n = 1000000


def randomGenerator():
    file = open("random.csv", "w")
    i = 0;
    while i < n :
        file.write(str(random.randint(0, 1000000)) + "\t")
        i += 1
    file.close()

    
def orderedGenerator():
    file = open("random.csv", "w")
    i = 0;
    while i < n :
        file.write(str(100 * i + random.randint(0, 100)) + "\t")
        i += 1
    file.close()


def analyse():
    print("reading date...")
    data = pandas.read_csv("random.csv", header=None, sep="\t").iloc[0].tolist()
    print("data imported")
#     data = [123,46,2,21,4,516,43,216,54,84,-48,-4,0,-654]
    sortMethonds = SortMethonds(data)
    sortMethonds.sortAll()

# randomGenerator()
# orderedGenerator()
analyse()

