from functools import reduce
from itertools import groupby
from math import prod
from operator import iconcat
from typing import Any, Dict


def getData(test: bool = False) -> list[str]:
    if (test):
        return [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ]
    with open('input.txt', 'r') as file:
        return file.readlines()


def parseGame(line: str) -> int:
    gameMax: Dict[str, int] = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    game, cubes = line.strip().split(':')
    gameID = int(game.strip().split(' ')[-1])
    sets = [s.strip() for s in cubes.strip().split(';')]
    for set in sets:
        c = [s.strip().split(' ') for s in set.strip().split(',')]
        filtered = list(filter(lambda x: int(x[0]) > gameMax[x[1]], c))
        if (len(filtered) > 0):
            return 0
    return gameID


def parseGame2(line: str) -> int:
    minCubes: Dict[str, int] = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    _, cubes = line.strip().split(':')
    sets = [parseSet(s) for s in cubes.strip().split(';')]
    for key in minCubes.keys():
        minCubes[key] = max(map(lambda x: x[key], sets))

    return prod(minCubes.values())


def flatten(arr):
    return reduce(iconcat, arr, [])


def parseSet(set: str) -> dict[str, int]:
    cubes = set.strip().split(',')
    cubes = [[q for q in s.strip().split(' ')] for s in cubes]
    returnDict = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for c in cubes:
        returnDict[c[1]] = int(c[0])
    return returnDict


def solution(data: list[str]) -> int:
    return sum([parseGame(line) for line in data])


def solution2(data: list[str]) -> int:
    return sum([parseGame2(line) for line in data])


if __name__ == "__main__":
    data = getData()
    print(solution(data))
    print(solution2(data))
