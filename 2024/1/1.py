from collections import Counter
from functools import reduce
from typing import List, Tuple


def getData(test=True):
    if test:
        return [
            "3   4",
            "4   3",
            "2   5",
            "1   3",
            "3   9",
            "3   3",
        ]
    with open("test1.txt", "r") as file:
        return file.readlines()


def formatData(data: List[str]):
    l1 = []
    l2 = []

    for l in data:
        splitted = list(map(int, l.strip().split()))
        l1.append(splitted[0])
        l2.append((splitted[1]))
    return l1, l2


def solution1(data):
    l1 = sorted(data[0])
    l2 = sorted(data[1])
    return reduce(lambda x, y: x + abs(y[0] - y[1]), zip(l1, l2), 0)


def solution2(data):
    l1 = data[0]
    l2 = data[1]
    l2Counter = Counter(l2)

    return sum([x * l2Counter[x] for x in l1])


if __name__ == "__main__":
    d = getData(False)
    d = formatData(d)
    print(solution1(d))
    print(solution2(d))
