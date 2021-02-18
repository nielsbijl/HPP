import unittest
import random
from  ThreadedMergeSort.ThreadedMergeSort import threadedMergeSort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = random.sample(range(-10000, 100000), 1000)
        self.assertEqual(threadedMergeSort(0, data), sorted(data))
        self.assertEqual(threadedMergeSort(1, data), sorted(data))
        self.assertEqual(threadedMergeSort(2, data), sorted(data))
        self.assertEqual(threadedMergeSort(4, data), sorted(data))
        self.assertEqual(threadedMergeSort(8, data), sorted(data))
        self.assertEqual(threadedMergeSort(16, data), sorted(data))
        self.assertEqual(threadedMergeSort(32, data), sorted(data))





if __name__ == '__main__':
    unittest.main()
