from mpi4py import MPI
from multiprocessing import Process, Manager
import math
import time


def chuckify(x, n):
    """
    This function devides a number in n amount of parts
    :param x: The number
    :param n: Amount of parts
    :return: tuple of parts
    x = 32, n = 2 -> [(0, 16), (16, 32)]
    """
    start = 0
    delta = math.ceil(x / n)
    end = start + delta
    chunks = []
    for i in range(n):
        if end > x:
            end = x
        chunks.append((start, end))
        start += delta
        end += delta
    return chunks


def loops(zeef, num, kStart, kEnd):
    """
    This function is the 2 for loops of the sieve of eratosthenes
    :param zeef: The sieve
    :param num: The actual start index of the sieve
    :param kStart: The k it starts with
    :param kEnd: The k it ends with
    :return: The sieved list
    """
    for k in range(kStart, kEnd):
        for x in range(0, len(zeef)):
            if (x + num) % k == 0:
                if num + x >= k * 2:
                    zeef[x] = 0
    return zeef


def zeefFunctionality(n, rank, amountRanks, amountOfProcesses):
    """
    This function inits the sieve list. Divides the k's over the processes and handles the processes
    :param n: Length of this sublist
    :param rank: Which computer I am
    :param amountRanks: The total amount of computers
    :param amountOfProcesses: The amount of processes it will use
    :return: The amount of primes in this sublist
    """
    num = int(n / amountRanks) * rank  # Bepalen welke deel van de totale zeef we zitten
    if (amountRanks - 1) == rank:  # Als het de laatste rank is
        zeef = [1 for _ in range(int(n / amountRanks) + 1)]  # Aanmaken van de deelzeef
    else:
        zeef = [1 for _ in range(int(n / amountRanks))]  # Aanmaken van de deelzeef
    if rank == 0:
        zeef[0] = 0
        zeef[1] = 0
    chucks = chuckify(math.ceil(math.sqrt(n)), amountOfProcesses)  # Berekenen hoe we de k's verdelen
    chucks[0] = (2, chucks[0][1])  # De eerste k's begint altijd bij 2
    manager = Manager()
    zeef = manager.list(zeef)  # Het maken van de globale zeef lijst waar elk process bij kan
    processes = []
    for i in range(amountOfProcesses):
        processes.append(Process(target=loops, args=(zeef, num, chucks[i][0], chucks[i][1])))  # Processen aanmaken
    for p in processes:
        p.start()  # Processen starter
    for p in processes:
        p.join()  # Processen joinen
    return sum(zeef)  # Brekenen hoeveel primes in deze sublist zitten


def zeefVanEratosthenesMPIandMultiProcessing(n, processes):
    """
    This function dived's the total sieve list over the computers.
    :param n: The total lenght of the sieve list
    :param processes: The amount of processes every computer wil use
    """
    startTime = time.time()

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    localPrimes = zeefFunctionality(n, rank, size, processes)

    totalPrimes = comm.reduce(localPrimes, op=MPI.SUM, root=0)  # Het optellen van alle hoeveelheden primes uit de computers

    if rank == 0:
        print("Number of primes:", totalPrimes)
        print("Total time: ", time.time() - startTime)


if __name__ == "__main__":
    zeefVanEratosthenesMPIandMultiProcessing(10000, 2)

"""
RUN
mpiexec -n AMOUNTOFPROCESSES python3 zeef.py

"""
