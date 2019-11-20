from copy import deepcopy
# from functools import wraps
# import os
# import time
# 
# from joblib.externals.loky.backend.utils import psutil

usedTime = None
usedMemory = None

# def timer(self, function):
# 
#     def timer_(self, *args, **kwlist):
#         global usedTime, usedMemory
#         print(function.__name__ + ":")
#         t0 = time.time()
#         m0 = psutil.Process(os.getpid()).memory_info().rss
#         result = function(self, *args, **kwlist)
#         t1 = time.time()
#         m1 = psutil.Process(os.getpid()).memory_info().rss
#         usedTime = str(t1 - t0)
#         usedMemory = (str((m1 - m0) / 2))
#         print("used time:" + usedTime)
#         return result
# 
#     return timer_


class SortMethonds:
    
    dataSize, result_time, result_memory = None, None, None
    list = []
    origin_list = []

    def __init__(self, data, dataSize=32, result_time=0, result_memory=0):
        self.list = deepcopy(data)
        self.origin_list = deepcopy(data)
        self.dataSize = dataSize
        self.result_time = result_time
        self.result_memory = result_memory
        
#     def analyse(function):
# 
#         @wraps(function)
#         def analyse__(self, *args, **kwlist):
#             result = function(self, *args, **kwlist)
#             self.list = deepcopy(self.origin_list)
#             return result
#     
#         return analyse__

#     @analyse
#     @timer
    def insertSort(self):
        frames = [deepcopy(self.list)]
        for i in range(1, len(self.list)):
            t = self.list[i]
            j = i - 1
            while self.list[j] > t and j >= 0:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = t
            frames.append(deepcopy(self.list))
        return frames

#     @analyse
#     @timer
    def selectSort(self):
        frames = self.__selectSort(0, len(self.list) - 1)
        return frames
        
    def __selectSort(self, l, r):
        frames = [deepcopy(self.list)]
        for i in range(l, r + 1):
            minV = i;
            for j in range(i + 1, len(self.list)):
                if self.list[j] < self.list[minV]:
                    minV = j
            t = self.list[i]
            self.list[i] = self.list[minV]
            self.list[minV] = t
            frames.append(deepcopy(self.list))
        return frames
    
#     @analyse
#     @timer
    def bubbleSort(self):
        frames = [deepcopy(self.list)]
        b = True
        while b:
            b = False
            for i in range(1, len(self.list)):
                if self.list[i] < self.list[i - 1]:
                    t = self.list[i]
                    self.list[i] = self.list[i - 1]
                    self.list[i - 1] = t
                    b = True
            frames.append(deepcopy(self.list))
        return frames
    
    def __merge(self, l, mid, r, frames):
        a1 = self.list[l:mid]
        a2 = self.list[mid:r + 1]
        i1, i2 = 0, 0
        list = []
        while i1 < len(a1)  and i2 < len(a2) :
            if a1[i1] < a2[i2]:
                list.append(a1[i1])
                i1 += 1
                self.list[l:l + i1 + i2] = list
            else:
                list.append(a2[i2])
                i2 += 1
                self.list[l:l + i1 + i2] = list
            frames.append(deepcopy(self.list))
        while i1 < len(a1):
            self.list[l + i1 + i2] = a1[i1]
            i1 += 1
            frames.append(deepcopy(self.list))
        while i2 < len(a2):
            self.list[l + i1 + i2] = a2[i2]
            i2 += 1
            frames.append(deepcopy(self.list))
        return list
    
    def __mergeSort(self, l, r, frames):
        if l >= r:
                pass
        elif l == r - 1:
            if self.list[r] < self.list[l]:
                self.list[l] , self.list[r] = self.list[r] , self.list[l]
                frames.append(deepcopy(self.list))
            else:
                pass
        else:
            mid = int((r + l) / 2)
            self.__mergeSort(l, mid - 1, frames)
            self.__mergeSort(mid, r, frames)
            self.__merge(l, mid, r, frames)
        return frames
        
#     @analyse
#     @timer
    def mergeSort(self):
        frames = [deepcopy(self.list)]
        frames = self.__mergeSort(0, len(self.list) - 1, frames)
        return frames
    
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
    
#     @analyse
#     @timer
    def quickSort2(self):
        frames = [deepcopy(self.list)]
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
            frames.append(deepcopy(self.list))
        return frames

#     @analyse
#     @timer
    def quickSort(self):
        return self.__quickSort(0, len(self.list) - 1)
    
#     @profile
    def sortAll(self):
        self.bubbleSort()
        self.result_time.loc[0, self.dataSize] = usedTime
        self.result_memory.loc[0, self.dataSize] = usedMemory
        
        self.insertSort()
        self.result_time.loc[1, self.dataSize] = usedTime
        self.result_memory.loc[1, self.dataSize] = usedMemory
        
        self.selectSort()
        self.result_time.loc[2, self.dataSize] = usedTime
        self.result_memory.loc[2, self.dataSize] = usedMemory
        
        self.mergeSort()
        self.result_time.loc[3, self.dataSize] = usedTime
        self.result_memory.loc[3, self.dataSize] = usedMemory

#         self.quickSort()       
        self.quickSort2()
        self.result_time.loc[4, self.dataSize] = usedTime
        self.result_memory.loc[4, self.dataSize] = usedMemory
        print()
        
