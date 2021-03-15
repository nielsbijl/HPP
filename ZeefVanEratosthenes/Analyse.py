import time
from ZeefVanEratosthenes.zeef import zeefVanEratosthenes


def timeFunction(function, n):
    startTime = time.time()
    function(n)
    return time.time() - startTime


if __name__ == "__main__":
    print("sequentiële variant:", timeFunction(zeefVanEratosthenes, 100000000), "seconden")
