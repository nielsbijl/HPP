from mpi4py import MPI
import math
import time


def functionality(n, rank, amountRanks):
    """
    This function uses the sieve of eratosthenes over a sublist
    :param n: The length of the total list
    :param rank: Which computer I am
    :param amountRanks: The total amount of computers
    :return: The amount of primes in this sublist
    """
    num = int(n / amountRanks) * rank  # Bepalen welke deel van de totale zeef we zitten
    if (amountRanks - 1) == rank:  # Als het de laatste rank is
        zeef = [1 for _ in range(int(n / amountRanks) + 1)]  # Aanmaken van de deelzeef
    else:
        zeef = [1 for _ in range(int(n / amountRanks))]
    if rank == 0:
        zeef[0] = 0
        zeef[1] = 0
    for k in range(2, math.ceil(math.sqrt(n))):
        for x in range(0, len(zeef)):
            if (x + num) % k == 0:
                if num + x >= k * 2:
                    zeef[x] = 0
    return sum(zeef)


def zeefVanEratosthenesMPI(n):
    """
    This function uses MPI to devide the sieve of eratosthenes with sublists to loop over.
    :param n: Total length of the sieve
    """
    startTime = time.time()

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    localPrimes = functionality(n, rank, size)

    totalPrimes = comm.reduce(localPrimes, op=MPI.SUM, root=0)

    if rank == 0:
        print("Number of primes:", totalPrimes)
        print("Total time: ", time.time() - startTime)


if __name__ == "__main__":
    zeefVanEratosthenesMPI(1000)

"""
RUN
mpiexec -n AMOUNTOFPROCESSES python3 test.py

"""
