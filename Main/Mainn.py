import os
import random
import re
import sys

from matplotlib import pyplot
import pandas
from pandas.core.frame import DataFrame

from Sort.Sorts import SortMethonds

sys.setrecursionlimit(100000000)
address = "../datasets/"
n = 20000


def generateGraph():
    for datatypes in os.listdir(address):
        for dataforms in os.listdir(address + datatypes):
            for file in os.listdir(address + datatypes + "/" + dataforms):
                if file.find("result") != -1 and file.find("csv") != -1:
                    pyplot.cla()
                    result = pandas.read_csv(address + datatypes + "/" + dataforms + "/" + file)
                    x = list(result.columns.values)[2:]
                    ys = result.iloc[:, 1:]
                    for i in range(ys.shape[0]):
                        y = ys.iloc[i]
                        pyplot.plot(x, y.tolist()[1:])
                    pyplot.xlabel(dataforms)
                    if file == "result_time.csv":
                        pyplot.ylabel("Time")
                    else:
                        pyplot.ylabel("Extra Memory Use")
                    pyplot.title(datatypes + " " + dataforms)
                    pyplot.legend(ys.iloc[:, 0].tolist())
#                     pyplot.show()
                    try:
                        os.remove(address + datatypes + "/" + dataforms + "/" + file[:-4] + ".png")
                    except:
                        None
                    pyplot.savefig(address + datatypes + "/" + dataforms + "/" + file[:-4] + ".png")


def readFile():
    for datatypes in os.listdir(address):  # 遍历文件夹
        for dataforms in os.listdir(address + datatypes):
            result_time, result_memory = DataFrame(), DataFrame()
            result_time["method"] = ["bubbleSort", "insertSort", "selectSort", "mergeSort", "quickSort"]
            result_memory["method"] = ["bubbleSort", "insertSort", "selectSort", "mergeSort", "quickSort"]
            for file in os.listdir(address + datatypes + "/" + dataforms):
                print(datatypes + "/" + dataforms + "/" + file)
                if file.find("result") == -1:
                    dataSize = re.findall("_(.+?)\.", file)[0]
                    result_time[dataSize] = None
                    result_time.to_csv(address + datatypes + "/" + dataforms + "/" + "result_time.csv", sep=",")
                    result_memory[dataSize] = None
                    result_memory.to_csv(address + datatypes + "/" + dataforms + "/" + "result_memory.csv", sep=",")
                    yield address + datatypes + "/" + dataforms + "/" + file, dataSize, result_time, result_memory
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


def analyse(data, dataSize, result_time, result_memory):
#     print("reading date...")
#     data = pandas.read_csv(address + "test.csv", header=None, sep="\t").iloc[0].tolist()
#     data = [123,46,2,21,4,516,43,216,54,84,-48,-4,0,-654]
#     print("data imported")
    sortMethonds = SortMethonds(data, dataSize, result_time, result_memory)
    sortMethonds.sortAll()


generateGraph()

# datas = readFile()
# randomGenerator()
# orderedGenerator()
# while True:
#     data, dataSize, result_time, result_memory = next(datas)
#     analyse(pandas.read_csv(data, header=None, sep="\t").iloc[0].tolist(), dataSize, result_time, result_memory)

