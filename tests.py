import unittest

from generator1 import gen3
from generator1 import fibonacci as fib

class TestGen(unittest.TestCase):

    def test_gen3(self):
        g = gen3(5)

        res = []
        for i in g:
            res.append(i)

        self.assertEqual(res, [1,2,3,4,5])

    def test_fib5(self):
        f = fib()

        res = []
        counter = 0
        for i in f:
            res.append(i)
            counter += 1
            if (counter >= 5):
                break

        self.assertEqual(res, [0,1,1,2,3])
