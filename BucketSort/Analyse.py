import sys
import time
import random
import matplotlib.pyplot as plt
from BucketSort import bucketSort, bucketSortRecursive
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