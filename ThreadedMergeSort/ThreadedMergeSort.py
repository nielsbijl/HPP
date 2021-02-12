import random
import threading, logging, time
import concurrent.futures
from typing import List


def merge_sort(sequence):
    """
    Sequence of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(sequence) < 2:
        return sequence

    mid = len(sequence) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_sequence = merge_sort(sequence[:mid])
    right_sequence = merge_sort(sequence[mid:])

    return merge(left_sequence, right_sequence)


def merge(left, right):
    """
    Traverse both sorted sub-arrays (left and right), and populate the result array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


def chunkify(lst, chunks):
    return [lst[i::chunks] for i in range(chunks)]


if __name__ == "__main__":

    threads = 1024
    data = random.sample(range(0, 100000), 100000)

    if not (threads & (threads - 1) == 0) and threads != 0:
        raise Exception("Sorry, the amount of threads needs to be a power of 2")

    print("Running threaded:")
    threadedStart = time.time()

    """ Data opsplitsen in hoeveel threads je hebt. """
    data = chunkify(data, threads)

    """ Elke thread zijn stukje data mee geven en dit laten sorteren doormiddel van Merge Sort. """
    outputs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for index in range(threads):
            futures.append(executor.submit(merge_sort, data[index]))
        for future in concurrent.futures.as_completed(futures):
            outputs.append(future.result())

    """ 
    Alle gesorteerde losse data weer verder mergen.
    Als je 1 thread hebt gebruikt returnt die alle data gesorteerd in 1 keer, dus
    is verder mergen niet nodig.
    """
    while len(outputs) > 1:
        finalOutput = []
        for i in range(0, len(outputs), 2):
            finalOutput.append(merge(outputs[i], outputs[i + 1]))
        outputs = finalOutput.copy()

    print("Threaded time:", time.time() - threadedStart)
    print(outputs[0])



"""
################################################################################
##################################### BRON #####################################
##### https://stackoverflow.com/questions/18761766/mergesort-with-python #######
################################################################################
################################################################################
"""