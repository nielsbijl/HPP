import sys
import time
import random
import matplotlib.pyplot as plt
from BucketSort import bucketSort, bucketSortRecursive
sys.setrecursionlimit(10 ** 9)


def testSortTime(algorithm, array: list):
    """
    Deze functie is te gebruiken voor het timen van sorteer algoritmes
    :param algorithm: Het sorteer algoritme die getimet wil worden
    :param array: De array waarop het sorteer algoritme getest moet worden
    :return: De tijd die het duurde voor het algoritme om de meegegeven lijst te sorteren
    """
    start_time = time.time()
    algorithm(array)
    return time.time() - start_time  # current time - start time


def plotTimeComplexity(algorithm):
    """
    Het plotten van de tijdscomplexiteit van het mee gekregen algoritme
    :param algorithm: Het sorteer algoritme die plot moet worden
    """
    print("\nHet plotten van de tijd complexiteit.....")
    x = []
    y = []
    for i in range(1000, 76000, 1000):
        testList = random.sample(range(-1000000, 1000000), i)  # i aantal getallen tussen de -1000000 en 1000000
        time = testSortTime(algorithm, testList)
        x.append(i)
        y.append(time)
    plt.plot(x, y)
    plt.show()

"""
De test cases voor de analyse:
"""

randomTestLists = [random.sample(range(-1000000, 1000000), 1000),
                   random.sample(range(-1000000, 1000000), 10000),
                   random.sample(range(-1000000, 1000000), 30000)]
sortedTestList = sorted(randomTestLists[2])
reversedSortedTestList = sorted(randomTestLists[2], reverse=True)

"""
Het printen van de analyse
"""

print("Het sorteren van de lijst met random 1.000 items duurde:", testSortTime(bucketSort, randomTestLists[0]), "seconden.")
print("Het sorteren van de lijst met random 10.000 items duurde:", testSortTime(bucketSort, randomTestLists[1]), "seconden.")
print("Het sorteren van de lijst met random 30.000 items duurde:", testSortTime(bucketSort, randomTestLists[2]), "seconden.")
print("Het sorteren van de lijst met gesorteerde 30.000 items duurde:", testSortTime(bucketSort, sortedTestList), "seconden.")
print("Het sorteren van de lijst met omgekeerde gesorteerde 30.000 items duurde:", testSortTime(bucketSort, reversedSortedTestList), "seconden.")

print("\n")

print("Het recursive sorteren van de lijst met random 1.000 items duurde:", testSortTime(bucketSortRecursive, randomTestLists[0]), "seconden.")
print("Het recursive sorteren van de lijst met random 10.000 items duurde:", testSortTime(bucketSortRecursive, randomTestLists[1]), "seconden.")
print("Het recursive sorteren van de lijst met random 30.000 items duurde:", testSortTime(bucketSortRecursive, randomTestLists[2]), "seconden.")
print("Het recursive sorteren van de lijst met gesorteerde 30.000 items duurde:", testSortTime(bucketSortRecursive, sortedTestList), "seconden.")
print("Het recursive sorteren van de lijst met omgekeerde gesorteerde 30.000 items duurde:", testSortTime(bucketSortRecursive, reversedSortedTestList), "seconden.")



"""
Het plotten van de tijdscompexiteit
"""

plotTimeComplexity(bucketSortRecursive)
plotTimeComplexity(bucketSort)

