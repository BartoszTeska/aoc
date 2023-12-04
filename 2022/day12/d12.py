from math import sqrt
from traceback import print_tb
from typing import List, Tuple
from string import ascii_lowercase


class Point():
    def __init__(self, elevation, weight, isStart=False, isEnd=False) -> None:
        self.weight = weight
        self.elevation = elevation
        self.visited = False
        self.isStart = isStart
        self.isEnd = isEnd

    def __repr__(self) -> str:
        return f'{self.elevation}:{self.weight}'


def getData(test: bool = False):
    if test:
        return ['Sabqponm',
                'abcryxxl',
                'accszExk',
                'acctuvwj',
                'abdefghi',]

    with open('inputD12.txt', 'r') as file:
        return file.readlines()


def getStartEnd(arr: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    for i, line in enumerate(arr):
        if 'S' in line:
            start = (i, line.index('S'))
        if 'E' in line:
            end = (i, line.index('E'))
    return (start, end)


def makeWeights(arr: List[str], end: Tuple[int, int]):
    newArr = []
    for i, line in enumerate(arr):
        newLine = []
        for c in line:
            weight = sqrt((end[0]-line.index(c))**2 + (end[1]+i)**2)
            point = Point(c, weight)
            if point.elevation == 'S':
                point.isStart = True
            if point.elevation == "E":
                point.isEnd = True
            newLine.append(point)
        newArr.append(newLine)
    return newArr


if __name__ == "__main__":
    data = getData(True)
    start, end = getStartEnd(data)
    print(makeWeights(data, end))
