from functools import reduce
from operator import iconcat
import re


class Gear():
    touchingNumbers: list[int]

    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position
        self.touchingNumbers = []

    def ratio(self) -> int:
        if (0 <= len(self.touchingNumbers) <= 1):
            return 0
        return self.touchingNumbers[0]*self.touchingNumbers[1]


def getData(test: bool = False) -> list[str]:
    if (test):
        return [
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..',
        ]
    with open('input.txt', 'r') as file:
        return file.readlines()


def getNumberRange(line: str) -> list[tuple[int, int, int]]:
    numbers = re.finditer(r'\d+', line)
    numsWithSpans = []
    for m in numbers:
        numsWithSpans.append((m.start(), m.end()-1, int(m.group(0))))
    return numsWithSpans


def getSymbols(line: str) -> list[int]:
    symbols = re.finditer(r'[^\.\d\n]', line)
    symbolsPositions = []
    for m in symbols:
        symbolsPositions.append(m.start())
    return symbolsPositions


def isAdjacent(span: tuple[int, int], lineNumber: int, symbols: list[list[int]]):
    if (any([s == span[0]-1 or s == span[1]+1 for s in symbols[lineNumber]])):
        return True
    if (lineNumber < len(symbols)-1 and any([span[0]-1 <= s <= span[1]+1 for s in symbols[lineNumber+1]])):
        return True
    if (lineNumber > 0 and (any([span[0]-1 <= s <= span[1]+1 for s in symbols[lineNumber-1]]))):
        return True
    return False


def isTouchingGear(gear: Gear, number: tuple[int, int, int], lineNumber: int) -> bool:
    if (lineNumber == gear.position[0] and (number[0] == gear.position[1]+1 or number[1] == gear.position[1]-1)):
        return True
    if (lineNumber == gear.position[0]-1 and (any([number[0] <= x <= number[1] for x in range(gear.position[1]-1, gear.position[1]+2)]))):
        return True
    if (lineNumber == gear.position[0]+1 and (any([number[0] <= x <= number[1] for x in range(gear.position[1]-1, gear.position[1]+2)]))):
        return True
    return False


def getGears(line: str, lineNumber: int) -> list[Gear]:
    symbols = re.finditer(r'\*', line)
    return [Gear((lineNumber, m.start())) for m in symbols]


def flatten(arr):
    return reduce(iconcat, arr, [])


def fillGears(gear: Gear, numbers: list[list[tuple[int, int, int]]]) -> Gear:
    for i, n in enumerate(numbers):
        for num in n:
            if (len(gear.touchingNumbers) == 2):
                break
            if (isTouchingGear(gear, num, i)):
                gear.touchingNumbers.append(num[2])

    return gear


def solution(lines: list[str]) -> int:
    numbers = [getNumberRange(l) for l in lines]
    symbols = [getSymbols(l) for l in lines]

    return sum([number[2] for i, n in enumerate(numbers)
                for number in n if isAdjacent((number[0], number[1]), i, symbols)])


def solution2(lines: list[str]) -> int:
    numbers = [getNumberRange(l) for l in lines]
    gears = flatten([getGears(l, i) for i, l in enumerate(lines)])
    gears = [fillGears(gear, numbers) for gear in gears]
    return sum(map(lambda x: x.ratio(), gears))


if __name__ == '__main__':
    data = getData()
    print(solution(data))
    print(solution2(data))
