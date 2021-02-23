import concurrent.futures


def mergeSort(sequence):
    """
    Sequence of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(sequence) < 2:
        return sequence

    mid = len(sequence) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_sequence = mergeSort(sequence[:mid])
    right_sequence = mergeSort(sequence[mid:])

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
    """
    This function splits a list in x amount of chunks and returns it in a list.
    :param lst: The list that will be chunkified
    :param chunks: The amount of chunks the list will be splitted
    :return: A list of lists
    """
    return [lst[i::chunks] for i in range(chunks)]


def threadedMergeSort(threads: int, data: list):
    """
    This sorting algorithm uses the merge sort functionality multi threaded.
    :param threads: The amount of threads you want to add. (without the main thread)
    :param data: The list you want to sort
    :return: The sorted data

    Note: The amount of threads you want to add
            needs to be a power of 2! (1, 2, 4, 8, 16, 32, 64.......)
    """
    if not (threads & (threads - 1) == 0) and threads != 0:
        raise Exception("Sorry, the amount of threads needs to be a power of 2")

    if threads:
        # Data opsplitsen in hoeveel threads je hebt
        data = chunkify(data, threads)

        # Elke thread zijn stukje data mee geven en dit laten sorteren doormiddel van Merge Sort
        outputs = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            for index in range(threads):
                futures.append(executor.submit(mergeSort, data[index]))
            for future in concurrent.futures.as_completed(futures):
                outputs.append(future.result())
    else:
        return mergeSort(data)

    # Alle gesorteerde losse data weer verder mergen.
    # Als je 1 thread hebt gebruikt returnt die alle data gesorteerd in 1 keer, dus
    # is verder mergen niet nodig.

    while len(outputs) > 1:
        finalOutput = []
        for i in range(0, len(outputs), 2):
            finalOutput.append(merge(outputs[i], outputs[i + 1]))
        outputs = finalOutput.copy()

    return outputs[0]








"""
################################################################################
##################################### BRON #####################################
##### https://stackoverflow.com/questions/18761766/mergesort-with-python #######
################################################################################
################################################################################
"""