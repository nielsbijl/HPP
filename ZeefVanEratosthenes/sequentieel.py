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


if __name__ == "__main__":
    primes = zeefVanEratosthenes(1000)
    print(len(primes))