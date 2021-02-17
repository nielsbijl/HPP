from matplotlib import pyplot as plt
from ThreadedMergeSort import merge_sort, threadedMergeSort
import random
import time


def plot2formulas(func1, func2, data, maxThreads):
    x = []
    y1 = []
    y2 = []
    for thread in range(maxThreads):
        thread = 2 ** thread
        x.append(thread)

        startTime = time.time()
        func1(thread, data)
        y1.append(time.time() - startTime)

        startTime = time.time()
        func2(data)
        y2.append(time.time() - startTime)

    plt.plot(x, y1, label="Threaded Merge sort")
    plt.plot(x, y2, label="Normal Merge Sort")

    plt.xlabel('Threads')
    plt.ylabel('Time (s)')

    plt.legend()
    plt.show()
    return x, y1, y2


random.seed(1234)

data = random.sample(range(0, 100000), 100000)
plot2formulas(threadedMergeSort, merge_sort, data, 4)
