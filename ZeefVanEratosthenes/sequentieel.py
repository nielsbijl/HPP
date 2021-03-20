import math


def zeefVanEratosthenes(n):
    """
    This function is the sequential version of the sieve of eratosthenes
    :param n: Lenght of the sieve
    :return: The amount of primes of the sieve
    """
    zeef = [1 for _ in range(n + 1)]
    zeef[0] = 0
    zeef[1] = 0
    kStart = 2  # Aangezien 0 en 1 geen priem is, zetten we k op 2.
    for k in range(kStart, math.ceil(math.sqrt(n))):
        for x in range(0, len(zeef), k):
            number = x
            if number >= k * 2:
                zeef[x] = 0
    return sum(zeef)  # return de hoeveelheid priemgetallen


def zeefVanEratosthenesVectorVersie(n):
    """
    This function is the vectorized sequential version of the sieve of eratosthenes
    :param n: The length of the sieve
    :return: The amount of primes of the sieve
    """
    zeef = [1 for _ in range(n + 1)]
    zeef[0] = 0
    zeef[1] = 0
    zeef[4::2] = [0 for _ in range(len(zeef[4::2]))]
    for i in range(3, math.ceil(math.sqrt(n)), 2):
        if zeef[i]:
            zeef[i*i::2*i] = [0 for _ in range(len(zeef[i*i::2*i]))]
    return sum(zeef)


if __name__ == "__main__":
    primes = zeefVanEratosthenes(1000)
    print(primes)
    print(zeefVanEratosthenesVectorVersie(1000))