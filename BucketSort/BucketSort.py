import sys


def bucketSortFunctionalRecursive(data: list, maxDigitPosition: int, digitPosition: int = -1) -> list:
    """
    Plaats elke waarde van de een-dimensionale array in een rij van de bucket array, gebaseerd op het meest rechtse cijfer in het getal (de "een"-waarde). Bijvoorbeeld, 97 wordt geplaatst in rij 7, 3 wordt geplaatst in rij 3 en 100 wordt geplaatst in rij 0. Deze stap heet de distribution pass.
    Loop door de bucket array rij voor rij, en kopieer de waardes terug in de originele array. Deze stap heet de gathering pass. De volgorde van de hierboven genoemde getallen is dus nu 100, 3, 97.
    Herhaal dit proces voor elke volgende digit-positie (dus voor de tientallen, honderdtallen, etc.). Na de laatste gathering pass is de array gesorteerd. Dit wordt recursive gedaan.

    :param data: De lijst die gesorteerd moet worden
    :return: De gesorteerde lijst
    """
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
    """
    Plaats elke waarde van de een-dimensionale array in een rij van de bucket array, gebaseerd op het meest rechtse cijfer in het getal (de "een"-waarde). Bijvoorbeeld, 97 wordt geplaatst in rij 7, 3 wordt geplaatst in rij 3 en 100 wordt geplaatst in rij 0. Deze stap heet de distribution pass.
    Loop door de bucket array rij voor rij, en kopieer de waardes terug in de originele array. Deze stap heet de gathering pass. De volgorde van de hierboven genoemde getallen is dus nu 100, 3, 97.
    Herhaal dit proces voor elke volgende digit-positie (dus voor de tientallen, honderdtallen, etc.). Na de laatste gathering pass is de array gesorteerd.

    :param data: De lijst die gesorteerd moet worden
    :return: De gesorteerde lijst
    """
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


def bucketSort(data: list) -> list:
    """
    Hij splits de data op in positieve en negatieven getallen. De negatieve getallen worden positief gemaakt, gesorteerd, positief gemaakt en tenslotte wordt de lijst omgedraaid.
    De positieve getallen worden alleen gesorteerd.
    Hij sorteerd de lijst met de functionaliteit van het bucketSort algoritme.
    Hij past de negatieve lijst aan omdat de functionaliteit van het bucketSort algoritme alleen werkt op positieve integers.

    :param data: De lijst die gesorteerd moet worden.
    :return: De gesorteerde lijst
    """
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


def bucketSortRecursive(data: list) -> list:
    """
    Hij splits de data op in positieve en negatieven getallen. De negatieve getallen worden positief gemaakt, gesorteerd, positief gemaakt en tenslotte wordt de lijst omgedraaid.
    De positieve getallen worden alleen gesorteerd.
    Hij sorteerd de lijst met de functionaliteit van het bucketSort algoritme.
    Hij past de negatieve lijst aan omdat de functionaliteit van het bucketSort algoritme alleen werkt op positieve integers.
    Hij geeft de functionaliteit van het bucketSort algoritme mee hoevaak die zichzelf moet aanroepen, omdat de recursieve variant dit vereist.

    :param data: De lijst die gesorteerd moet worden.
    :return: De gesorteerde lijst
    """
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


def bucketSortFloats(data: list, sortAlgoritme = bucketSort) -> list:
    """
    Deze functie maakt het mogelijk om met de functionaliteit van het bucketSort algoritme te kunnen werken met floats.
    Hij vermenigvuldigd elk item in de lijst met oneindig (max int van python) en cast dit naar een int om de ".0" weg te krijgen.
    Nu kan de lijst gesorteerd worden met als standaard het bucketSort algoritme.
    Dan worden alle items weer gedeeld door oneindig (max int van python) en het zijn weer de orginele items.

    :param data: De lijst met floats die gesorteerd moet worden.
    :param sortAlgoritme: Het sorteer algoritme, standaard bucketSort.
    :return: De gesorteerde lijst.
    """
    multiply = sys.maxsize
    data = [int(item * multiply) for item in data]
    data = sortAlgoritme(data)
    data = [item / multiply for item in data]
    return data




