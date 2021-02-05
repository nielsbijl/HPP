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



