from multiprocessing import Process, Manager


def zeefVanEratosthenes(zeef, kStart, kEnd):
    zeef[0] = 0
    zeef[1] = 0
    for k in range(kStart, kEnd):
        for x in range(0, len(zeef), k):
            number = x
            if number >= k * 2:
                zeef[x] = 0
    return zeef  # return de priemgetallen


if __name__ == '__main__':
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
