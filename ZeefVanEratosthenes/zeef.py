def zeefVanEratosthenes(n):
    zeef = [True for item in range(n + 1)]
    zeef[0] = False
    zeef[1] = False
    k = 2  # Aangezien 0 en 1 geen priem is, zetten we k op 2.
    while (k ** 2) <= n:
        if zeef[k]:
            for i in range(k * 2, n + 1, k):
                zeef[i] = False
        k += 1
    return [i for i in range(len(zeef)) if zeef[i]]  # return de priemgetallen

