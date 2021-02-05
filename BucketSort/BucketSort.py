import sys
import time
import random
import matplotlib.pyplot as plt
sys.setrecursionlimit(10 ** 9)


def testSortTime(algorithm, array: list):
    start_time = time.time()
    algorithm(array)
    return time.time() - start_time


def plotTimeComplexity(algorithm):
    print("\nHet plotten van de tijd complexiteit.....")
    x = []
    y = []
    for i in range(1000, 76000, 1000):
        testList = random.sample(range(-1000000, 1000000), i)
        time = testSortTime(algorithm, testList)
        x.append(i)
        y.append(time)
    plt.plot(x, y)
    plt.show()


def bucketSortFunctionalRecursive(data: list, maxDigitPosition: int, digitPosition: int = -1) -> list:
    buckets = [[], [], [], [], [], [], [], [], [], []]
    for item in data[:]:  # distribution pass
        if int(len(str(item))) >= abs(digitPosition):
            index = int(str(item)[digitPosition])
            buckets[index].append(item)
            data.remove(item)
    for bucket in buckets:  # gathering pass
        for item in bucket:
            data.append(item)
    if abs(digitPosition) == maxDigitPosition:
        return data
    return bucketSortFunctionalRecursive(data, maxDigitPosition, digitPosition - 1)


def bucketSortFunctional(data: list) -> list:
    for i in range(1, int(len(str(max(data))))+1):
        buckets = [[], [], [], [], [], [], [], [], [], []]
        for item in data[:]:  # distribution pass
            if int(len(str(item))) >= i:
                char = str(item)[-i]
                index = int(char)
                buckets[index].append(item)
                data.remove(item)
        for bucket in buckets:  # gathering pass
            for item in bucket:
                data.append(item)
    return data


def bucketSort(data):
    negative = []
    positive = []
    for item in data:
        if item >= 0:
            positive.append(item)
        else:
            negative.append(item)
    if negative:
        negative = [i * -1 for i in negative]
        negative = bucketSortFunctional(negative)
        negative = [i * -1 for i in negative]
        negative = list(reversed(negative))
    if positive:
        positive = bucketSortFunctional(positive)
    return negative + positive


def bucketSortRecursive(data):
    negative = []
    positive = []
    for item in data:
        if item >= 0:
            positive.append(item)
        else:
            negative.append(item)
    if negative:
        negative = [i * -1 for i in negative]
        negative = bucketSortFunctionalRecursive(negative, int(len(str(max(negative)))))
        negative = [i * -1 for i in negative]
        negative = list(reversed(negative))
    if positive:
        positive = bucketSortFunctionalRecursive(positive, int(len(str(max(positive)))))
    return negative + positive


test = [100, 3, -97, 5, -122, 1, 10000, 2]

# print(bucketSortRecursive(test))
# print(bucketSort(test))

print(bucketSort(test))
print(bucketSortRecursive(test))

randomTestLists = [random.sample(range(-10000, 1000), 1000),
                   random.sample(range(-10000, 10000), 10000),
                   random.sample(range(-300000, 300000), 30000)]
sortedTestList = sorted(randomTestLists[2])
reversedSortedTestList = sorted(randomTestLists[2], reverse=True)

print("Het sorteren van de lijst met random 1.000 items duurde:", testSortTime(bucketSort, randomTestLists[0]), "seconden.")
print("Het sorteren van de lijst met random 10.000 items duurde:", testSortTime(bucketSort, randomTestLists[1]), "seconden.")
print("Het sorteren van de lijst met random 30.000 items duurde:", testSortTime(bucketSort, randomTestLists[2]), "seconden.")
print("Het sorteren van de lijst met gesorteerde 30.000 items duurde:", testSortTime(bucketSort, sortedTestList), "seconden.")
print("Het sorteren van de lijst met omgekeerde gesorteerde 30.000 items duurde:", testSortTime(bucketSort, reversedSortedTestList), "seconden.")

# plotTimeComplexity(bucketSort)
# plotTimeComplexity(bucketSortRecursive)

# print("Het sorteren van de lijst met random 30.000 items duurde:", testSortTime(bucketSort, randomTestLists[2]), "seconden.")
# print("Het sorteren van de lijst met random 30.000 items duurde:", testSortTime(bucketSortRecursive, randomTestLists[2]), "seconden.")
