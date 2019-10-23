from copy import deepcopy
from functools import wraps
import time

from memory_profiler import profile

usedTime = None


def timer(function):

    def timer_(*args, **kwlist):
        global usedTime
        print(function.__name__ + ":")
        t0 = time.time()
        result = function(*args, **kwlist)
        t1 = time.time()
        usedTime = str(t1 - t0)
        print("used time:" + usedTime)
        return result

    return timer_


class SortMethonds:
    
    dataSize, result = None, None
    list = []
    origin_list = []

    def __init__(self, data, dataSize, result):
        self.list = deepcopy(data)
        self.origin_list = deepcopy(data)
        self.dataSize = dataSize
        self.result = result
        
    def analyse(function):

        @wraps(function)
        def analyse__(self, *args, **kwlist):
            result = function(self, *args, **kwlist)
            self.list = deepcopy(self.origin_list)
            return result
    
        return analyse__

    @analyse
    @timer
    def insertSort(self):
        for i in range(1, len(self.list)):
            t = self.list[i]
            j = i - 1
            while self.list[j] > t and j >= 0:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = t

    @analyse
    @timer
    def selectSort(self):
        self.__selectSort(0, len(self.list) - 1)
        
    def __selectSort(self, l, r):
        for i in range(l, r + 1):
            minV = i;
            for j in range(i + 1, len(self.list)):
                if self.list[j] < self.list[minV]:
                    minV = j
            t = self.list[i]
            self.list[i] = self.list[minV]
            self.list[minV] = t
    
    @analyse
    @timer
    def bubbleSort(self):
        b = True
        while b:
            b = False
            for i in range(1, len(self.list)):
                if self.list[i] < self.list[i - 1]:
                    t = self.list[i]
                    self.list[i] = self.list[i - 1]
                    self.list[i - 1] = t
                    b = True
    
    def __merge(self, a1, a2):
        i1, i2, list = 0, 0, []
        while i1 < len(a1)  and i2 < len(a2) :
            if a1[i1] < a2[i2]:
                list.append(a1[i1])
                i1 += 1
            else:
                list.append(a2[i2])
                i2 += 1
        if i1 < len(a1):
            list.extend(a1[i1:])
        if i2 < len(a2) :
            list.extend(a2[i2:])
        return list
    
    def __mergeSort(self, l, r):
        if l >= r:
            return [self.list[l]]
        elif l == r - 1:
            if self.list[r] < self.list[l]:
                return [self.list[r], self.list[l]]
            else:
                return [self.list[l], self.list[r]]
        else:
            mid = int((r + l) / 2)
            a1 = self.__mergeSort(l, mid - 1)
            a2 = self.__mergeSort(mid, r)
            return self.__merge(a1, a2)
        
    @analyse
    @timer
    def mergeSort(self):
        self.list = self.__mergeSort(0, len(self.list) - 1)
    
    def __quickSort(self, l, r):
#         if r > l and r - l < 16:
#             return self.__selectSort(l, r)
        print(l, r)
        if l < r:
            x = self.list[r]
            i = l - 1
            for j in range(l, r):
                if self.list[j] <= x:
                    i += 1
                    self.list[i], self.list[j] = self.list[j], self.list[i]
            self.list[i + 1], self.list[r] = self.list[r], self.list[i + 1]
            self.__quickSort(l, i)
            self.__quickSort(i + 2, r)
    #         if r - l < 16:
    #             return self.__mergeSort(list, l, r)
    #         l1, r1 = l + 1, r
    #         while l1 != r1:
    #             while list[l1] < list[l] and l1 != r1:
    #                 l1 += 1
    #             while list[r1] >= list[l] and l1 != r1:
    #                 r1 -= 1
    #             list[l1], list[r1] = list[r1], list[l1]
    #         if list[l1] < list[l]:
    #             list[l1], list[l] = list[l], list[l1]
    #         else:
    #             list[l1 - 1], list[l] = list[l], list[l1 - 1]
    #             l1 -= 1
    #         self.__quickSort(list, l, l1 - 1)
    #         self.__quickSort(list, l1 + 1, r)
    #         return list
    
    @analyse
    @timer
    def __quickSort2(self):
        startStack = [0, ]
        endStack = [len(self.list) - 1, ]
        while startStack and endStack:
            start = startStack.pop()
            end = endStack.pop()
            if start > end:
                continue
            i = start 
            j = end
            while i < j:
                if self.list[i] > self.list[j]:
                    self.list[i], self.list[j - 1], self.list[j] = self.list[j - 1], self.list[j], self.list[i]
                    j -= 1
                else:
                    i += 1
            startStack.append(start)
            endStack.append(i - 1)
            startStack.append(i + 1)
            endStack.append(end)

    @analyse
    @timer
    def quickSort(self):
        return self.__quickSort(0, len(self.list) - 1)
    
#     @profile
    def sortAll(self):
        self.bubbleSort()
        self.result.loc[0, self.dataSize] = usedTime
        self.insertSort()
        self.result.loc[1, self.dataSize] = usedTime
        self.selectSort()
        self.result.loc[2, self.dataSize] = usedTime
        self.mergeSort()
        self.result.loc[3, self.dataSize] = usedTime
#         self.quickSort()       
        self.__quickSort2()
        self.result.loc[4, self.dataSize] = usedTime
        print()
        
