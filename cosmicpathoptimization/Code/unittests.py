__author__ = "Anthony Hunter"
__date__ = "2023/9/11"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Anthony Hunter"

"""
Unittesting Solution of Mia Dice Game
"""
import unittest
from cosmicpathoptimization import FindAvg, SetM


class TestSolution(unittest.TestCase):

    def test_1(self) -> None:
        arr = [0, 0, 0]
        sol = FindAvg(arr, len(arr))
        self.assertEqual(sol, 0)

    def test_2(self) -> None:
        arr = [10, 20, 30, 40, 50]
        sol = FindAvg(arr, len(arr))
        self.assertEqual(sol, 30)

    def test_3(self) -> None:
        sol = SetM('5')
        self.assertEqual(sol, 5)

    def test_4(self) -> None:
        sol = SetM('0')
        self.assertEqual(sol, 0)

    def test_5(self) -> None:
        arr = [-2000, -350, 650]
        sol = FindAvg(arr, len(arr))
        self.assertEqual(sol, 1000)

    def test_6(self) -> None:
        arr = [350, 250, 120, 80]
        sol = FindAvg(arr, SetM('-4'))
        self.assertEqual(sol, 200)


if __name__ == '__main__':

    unittest.main(verbosity=2)
