# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

import unittest
# unordered array of unique consequitive integers
# can swap any 2 elements
# find minimum number of swaps to get ascending order
def minimumSwaps(arr):

    # example 1:
    #     [4, 1, 3, 2]
    #     [2, 1, 3, 4] - 1 - swap to where the right index is and check if it's in the right place
    #     [1, 2, 3, 4] - 2 - swapped again

    # example 2:
    #     [7, 1, 3, 2 ,4, 5, 6]
    #     [6, 1, 3, 2, 4, 5, 7] - 1 - start at index 1 and continue swapping until in the right place
    #     [5, 1, 3, 2, 4, 6, 7] - 2
    #     [4, 1, 3, 2, 5, 6, 7] - 3
    #     [2, 1, 3, 4, 5, 6, 7] - 4
    #     [1, 2, 3, 4, 5, 6, 7] - 5

    i = 0
    swaps = 0
    while i < len(arr):
        while arr[i] != i+1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            swaps+=1
        i+=1

    return swaps
class MyTest(unittest.TestCase):
    def test_1(self):
        arr = [2, 3, 4, 1, 5]
        expected = 3
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)

    def test_2(self):
        arr = [1, 3, 5, 2, 4, 6, 7]
        expected = 3
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)

    def test_3(self):
        arr = [4, 3, 2, 1]
        expected = 2
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)

    def test_4(self):
        arr = [4, 3, 5, 1, 2]
        expected = 3
        received = minimumSwaps(arr)
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
