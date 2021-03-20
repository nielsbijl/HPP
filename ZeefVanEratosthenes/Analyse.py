import time

from ZeefVanEratosthenes.sequentieel import zeefVanEratosthenesVectorVersie, zeefVanEratosthenes
import matplotlib.pyplot as plt


def timeFunction(function, n):
    """
    This functions times a function with 1 parameter
    """
    startTime = time.time()
    function(n)
    return time.time() - startTime


MPI = [1, 2, 3, 4, 5, 6, 7, 8, 10, 16, 32, 64]
MP1 = [124, 49, 27, 17, 12, 12, 12, 12, 12, 12, 13, 12]
MP2 = [112, 45, 26, 19, 13, 12, 13, 12, 12, 12, 13, 12]
MP3 = [108, 47, 28, 19, 13, 13, 13, 13, 13, 12, 13, 13]
MP4 = [109, 46, 28, 21, 13, 13, 13, 13, 13, 12, 13, 13]
MP6 = [107, 48, 28, 20, 13, 13, 13, 12, 13, 12, 13, 13]
MP8 = [114, 47, 28, 20, 13, 13, 13, 12, 13, 12, 13, 12]

if __name__ == "__main__":
    print("sequentiële variant:", timeFunction(zeefVanEratosthenes, 100000), "seconden")
    print("vector variant:", timeFunction(zeefVanEratosthenesVectorVersie, 100000), "seconden")

    plt.plot(MPI, MP1, label="multi processes 1")
    plt.plot(MPI, MP2, label="multi processes 2")
    plt.plot(MPI, MP3, label="multi processes 3")
    plt.plot(MPI, MP4, label="multi processes 4")
    plt.plot(MPI, MP6, label="multi processes 6")
    plt.plot(MPI, MP8, label="multi processes 8")

    plt.xlabel('Computers (MPI)')
    plt.ylabel('Time (s)')
    plt.title('Timing of the sieve of eratosthenes')
    plt.suptitle("n = 100000", fontsize=10)
    plt.show()
