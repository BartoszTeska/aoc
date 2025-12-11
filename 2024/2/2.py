from itertools import pairwise
from os import remove


def getData(test=True):
    if test:
        return [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9",
        ]
    with open("test2.txt", "r") as file:
        return file.readlines()


def parseData(data):
    return [list(map(int, x.strip().split())) for x in data]


def checkIfSafe(line):
    if line not in (sorted(line), sorted(line, reverse=True)):
        return 0
    if not all(1 <= abs(a - b) <= 3 for a, b in pairwise(line)):
        return 0
    return 1


def checkIfSafe2(line):
    if checkIfSafe(line) == 1:
        return 1
    for i, _ in enumerate(line):
        removed = line[:i] + line[i + 1 :]
        if removed not in (sorted(removed), sorted(removed, reverse=True)):
            
        if not all(1 <= abs(a - b) <= 3 for a, b in pairwise(removed)):


def solution(data):
    return sum([checkIfSafe(x) for x in data])


def solution2(data):
    return sum([checkIfSafe2(x) for x in data])


if __name__ == "__main__":
    data = getData(False)
    data = parseData(data)
    print(solution(data))
    print(solution2(data))
