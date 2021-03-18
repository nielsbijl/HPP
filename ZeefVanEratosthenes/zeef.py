from multiprocessing import Process, Queue
import math


def zeefVanEratosthenes(n):
    zeef = [True for item in range(n + 1)]
    zeef[0] = False
    zeef[1] = False
    kStart = 2  # Aangezien 0 en 1 geen priem is, zetten we k op 2.
    for k in range(kStart, math.ceil(math.sqrt(n))):
        for x in range(0, len(zeef), k):
            number = x
            if number >= k * 2:
                zeef[x] = 0
    return [i for i in range(len(zeef)) if zeef[i]]  # return de priemgetallen


def zeefVanEratosthenesMulti(n):
    zeef = [1 for item in range(n + 1)]
    zeef[0] = 0
    zeef[1] = 0
    queue = Queue()
    processes = [Process(target=functionality, args=(zeef, 2, 16, n, queue,)),
                 Process(target=functionality, args=(zeef, 16, 32, n, queue,))]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    results = [queue.get() for _ in processes]
    summed = []
    for i in range(len(results[0])):
        summed.append(results[0][i] + results[1][i])
    return [i for i in range(len(summed)) if summed[i]]


# def functionality(zeef, start, end, n):
#     for k in range(2, math.ceil(math.sqrt(n))):
#         if zeef[k]:
#             currStart = start - (start % k)
#             for x in range(currStart, end + 1, k):
#                 if x + start >= k * 2:
#                     zeef[x] = 0
#     return zeef[start:end].count(1)


# def functionality(n, rank, amountRanks, isLast):
# #     num = int(n/amountRanks * rank)
# #     if isLast:
# #         zeef = [1 for item in range(int(n / 4) + 1 + int((num % math.ceil(math.sqrt(n)))))]
# #     else:
# #         zeef = [1 for item in range(int(n / 4) + int((num % math.ceil(math.sqrt(n)))))]
# #     if rank == 0:
# #         zeef[0] = 0
# #         zeef[1] = 0
# #     for k in range(2, math.ceil(math.sqrt(n))):
# #         for x in range(round((num % k)), int(n/amountRanks), k):
# #             if num + x >= k * 2:
# #                 zeef[x] = 0
# #     return sum(zeef[:int((num % math.ceil(math.sqrt(n))))])

def zeefVanEratosthenesVectorVersie(n):
    zeef = [1 for _ in range(n + 1)]
    zeef[0] = 0
    zeef[1] = 0
    zeef[4::2] = [0 for _ in range(len(zeef[4::2]))]
    for i in range(3, int(1 + n**0.5), 2):
        if zeef[i]:
            zeef[i*i::2*i] = [0 for _ in range(len(zeef[i*i::2*i]))]
    return sum(zeef)


if __name__ == "__main__":
    n = 1000

    print(zeefVanEratosthenesVectorVersie(n))
