import os
import random
import re
import sys

import pandas
from pandas.core.frame import DataFrame

from Sort.Sorts import SortMethonds

sys.setrecursionlimit(100000000)
address = "../datasets/"
n = 20000


def readFile():
    for datatypes in os.listdir(address):  # 遍历文件夹
        for dataforms in os.listdir(address + datatypes):
            result = DataFrame()
            result["method"] = ["bubbleSort", "insertSort", "selectSort", "mergeSort", "quickSort"]
            for file in os.listdir(address + datatypes + "/" + dataforms):
                print(datatypes + "/" + dataforms + "/" + file)
                if file != "result.csv":
                    dataSize = re.findall("_(.+?)\.", file)[0]
                    result[dataSize] = None
                    result.to_csv(address + datatypes + "/" + dataforms + "/" + "result.csv", sep=",")
                    yield address + datatypes + "/" + dataforms + "/" + file, dataSize, result
    return None

            
def randomGenerator():
    file = open(address + "test.csv", "w")
    i = 0;
    while i < n :
        file.write(str(random.randint(0, 1000000)) + "\t")
        i += 1
    file.close()

    
def orderedGenerator():
    file = open(address + "test.csv", "w")
    i = 0;
    while i < n :
        file.write(str(100 * i + random.randint(0, 100)) + "\t")
        i += 1
    file.close()


def analyse(data, dataSize, result):
#     print("reading date...")
#     data = pandas.read_csv(address + "test.csv", header=None, sep="\t").iloc[0].tolist()
#     data = [123,46,2,21,4,516,43,216,54,84,-48,-4,0,-654]
#     print("data imported")
    sortMethonds = SortMethonds(data, dataSize, result)
    sortMethonds.sortAll()


datas = readFile()
# randomGenerator()
# orderedGenerator()
while True:
#     try:
        data, dataSize, result = next(datas)
        analyse(pandas.read_csv(data, header=None, sep="\t").iloc[0].tolist(), dataSize, result)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

