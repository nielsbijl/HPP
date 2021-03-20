from multiprocessing import Process, Manager


def zeefVanEratosthenes(zeef, kStart, kEnd):
    """
    This function contains the algorithm of the sieve of eratosthenes
    :param zeef: The sieve list
    :param kStart: The K to start with
    :param kEnd: The K to end with
    :return: The sieved list
    """
    zeef[0] = 0
    zeef[1] = 0
    for k in range(kStart, kEnd):
        for x in range(0, len(zeef), k):
            number = x
            if number >= k * 2:
                zeef[x] = 0
    return zeef  # return de priemgetallen


if __name__ == '__main__':
    """
    Hier wordt een voorbeeld gegeven van het verdelen van de k's over 2 processen.
    Het eerste proces doet k 2-16 het tweede proces doet 16-32.
    """
    n = 1000

    zeef = [1 for _ in range(n + 1)]
    manager = Manager()
    zeef = manager.list(zeef)

    processes = [Process(target=zeefVanEratosthenes, args=(zeef, 2, 16)),
                 Process(target=zeefVanEratosthenes, args=(zeef, 16, 32))]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(sum(zeef))
