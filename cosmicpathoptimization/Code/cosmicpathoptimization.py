import sys
from typing import List


def FindAvg(arr: List[int], M: int) -> int:

    total = 0
    for i in arr:
        total += abs(i)
    return int(total / M)


def SetM(M: str) -> int:
    if abs(int(M)) >= 1:
        return abs(int(M))
    else:
        return 0


if __name__ == '__main__':
    """Main
    """
    M = SetM(sys.stdin.readline().replace('\n', ''))
    if M >= 1:
        val = sys.stdin.readline().replace('\n', '').split()
        arr = [int(value) for value in val]
        avg = FindAvg(arr, int(M))
        print(avg)
    else:
        exit()
