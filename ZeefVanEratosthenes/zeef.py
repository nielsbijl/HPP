from mpi4py import MPI
from multiprocessing import Process, Manager
import math
import time


def chuckify(item, n):
    start = 0
    delta = math.ceil(item / n)
    end = start + delta
    chunks = []
    for i in range(n):
        if end > item:
            end = item
        chunks.append((start, end))
        start += delta
        end += delta
    return chunks


def loop(zeef, num, kStart, kEnd):
    for k in range(kStart, kEnd):
        for x in range(0, len(zeef)):
            if (x + num) % k == 0:
                if num + x >= k * 2:
                    zeef[x] = 0
    return zeef


def functionality(n, rank, amountRanks, amountOfProcesses):
    num = int(n / amountRanks) * rank  # Bepalen welke deel van de totale zeef we zitten
    if (amountRanks - 1) == rank:  # Als het de laatste rank is
        zeef = [1 for _ in range(int(n / amountRanks) + 1)]  # Aanmaken van de deelzeef
    else:
        zeef = [1 for _ in range(int(n / amountRanks))]
    if rank == 0:
        zeef[0] = 0
        zeef[1] = 0
    chucks = chuckify(math.ceil(math.sqrt(n)), amountOfProcesses)
    chucks[0] = (2, chucks[0][1])
    manager = Manager()
    zeef = manager.list(zeef)
    processes = []
    for i in range(amountOfProcesses):
        processes.append(Process(target=loop, args=(zeef, num, chucks[i][0], chucks[i][1])))
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return sum(zeef)


def zeefVanEratosthenesMPIandMultiProcessing(n, processes):
    startTime = time.time()

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    localPrimes = functionality(n, rank, size, processes)

    totalPrimes = comm.reduce(localPrimes, op=MPI.SUM, root=0)

    if rank == 0:
        print("Number of primes:", totalPrimes)
        print("Total time: ", time.time() - startTime)


if __name__ == "__main__":
    zeefVanEratosthenesMPIandMultiProcessing(10000, 2)

"""
RUN
mpiexec -n AMOUNTOFPROCESSES python3 test.py

"""
