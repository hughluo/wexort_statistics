import unittest
from statistics import (
                        pstdev,

                        )
from basic import (
                    weighted_mean,
                    quartiles,
                    standard_deviation,
                    )

class MyTest(unittest.TestCase):

    def test(self):
        tl = [1.2, 3.4, 4.5, 5.6, 6, 7]
        self.assertAlmostEqual(weighted_mean([10,40,30,50,20],[1,2,3,4,5]), 32.0)
        self.assertEqual(quartiles([3,7,8,5,12,14,21,13,18]), (6, 12, 16))
        self.assertAlmostEqual(standard_deviation(tl), pstdev(tl))

if __name__ == '__main__':
    unittest.main()