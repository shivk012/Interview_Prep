# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import unittest

def minimumBribes(q):
    moves = 0

    q = [p-1 for p in q]

    for i, p in enumerate(q):
        if p-i >2:
            print('Too chaotic')
            return 'Too chaotic'
        
        for j in range(max(p-1, 0), i):
            if q[j] > p:
                moves+=1
    print(moves)
    return moves

class MyTest(unittest.TestCase):
    def test_1(self):
        q = [2, 1, 5, 3, 4]
        expected = 3
        self.assertEqual(minimumBribes(q), expected)

    def test_2(self):
        q = [2, 5, 1, 3, 4]
        expected = 'Too chaotic'
        self.assertEqual(minimumBribes(q), expected)

    def test_3(self):
        q = [1, 2, 5, 3, 7, 8, 6, 4]
        expected = 7
        self.assertEqual(minimumBribes(q), expected)

    def test_4(self):
        q = [5, 1, 2, 3, 7, 8, 6, 4]
        expected = 'Too chaotic'
        self.assertEqual(minimumBribes(q), expected)

if __name__ == '__main__':
    unittest.main()
