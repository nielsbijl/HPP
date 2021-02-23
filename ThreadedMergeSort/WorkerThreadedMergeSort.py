import threading
from ThreadedMergeSort import chunkify, mergeSort, merge


class ThreadWithResult(threading.Thread):
    """
    This ThreadWithResult class makes it possible te get
    the result of a thread
    """

    def __init__(self, target, args):
        self.target = target
        self.args = args

        def function():
            self.result = self.target(*self.args)

        super().__init__(target=function, args=())


def workerThreadsMergeSort(lst):
    """
    This function uses MergeSort with worker threads recursive
    :param lst: The list that needs to be sorted
    :return: The sorted list
    """

    if len(lst) > 2:
        lstChunks = chunkify(lst, 2)
        thread = ThreadWithResult(target=workerThreadsMergeSort, args=(lstChunks[1],))
        thread.start()
        return merge(workerThreadsMergeSort(lstChunks[0]), thread.result)
    return mergeSort(lst)


"""
Bron ThreadWithResult: https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
"""
