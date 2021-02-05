import unittest
from BucketSort.BucketSort import *


class TestBucketSort(unittest.TestCase):

    def testBucketSort(self):
        testCasePositive = [100, 3, 97, 5, 122, 1, 10000, 2]
        testCaseNegative = [-100, -3, -97, -5, -122, -1, -10000, -2]
        testCasePositiveAndNegative = [100, 3, -97, 5, -122, 1, 10000, 2]
        self.assertEqual(bucketSort(testCasePositive), sorted(testCasePositive))
        self.assertEqual(bucketSort(testCaseNegative), sorted(testCaseNegative))
        self.assertEqual(bucketSort(testCasePositiveAndNegative), sorted(testCasePositiveAndNegative))

    def testBucketSortRecursive(self):
        testCasePositive = [100, 3, 97, 5, 122, 1, 10000, 2]
        testCaseNegative = [-100, -3, -97, -5, -122, -1, -10000, -2]
        testCasePositiveAndNegative = [100, 3, -97, 5, -122, 1, 10000, 2]
        self.assertEqual(bucketSortRecursive(testCasePositive), sorted(testCasePositive))
        self.assertEqual(bucketSortRecursive(testCaseNegative), sorted(testCaseNegative))
        self.assertEqual(bucketSortRecursive(testCasePositiveAndNegative), sorted(testCasePositiveAndNegative))

    def testBucketSortFunctional(self):
        testCase = [100, 3, 97, 5, 122, 1, 10000, 2]
        self.assertEqual(bucketSortFunctional(testCase), sorted(testCase))

    def testBucketSortFunctionalRecursive(self):
        testCase = [100, 3, 97, 5, 122, 1, 10000, 2]
        self.assertEqual(bucketSortFunctionalRecursive(testCase, len(str(max(testCase)))), sorted(testCase))


if __name__ == '__main__':
    unittest.main()
