import re


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


def getGears(line: str) -> list[int]:
    symbols = re.finditer(r'\*', line)
    return [m.start() for m in symbols]


def getGearRatio(gear: int, lineNumber: int, numbers: list[list[tuple[int, int, int]]]) -> int:
    availableNums = numbers[min(0, lineNumber-1):min(lineNumber+1, len(numbers))]


def solution(lines: list[str]) -> int:
    numbers = [getNumberRange(l) for l in lines]
    symbols = [getSymbols(l) for l in lines]

    return sum([number[2] for i, n in enumerate(numbers)
                for number in n if isAdjacent((number[0], number[1]), i, symbols)])


def solution2(lines: list[str]) -> int:
    numbers = [getNumberRange(l) for l in lines]
    gears = [getGears(l) for l in lines]
    print(gears)
    for i, gear in enumerate(gears):
        [getGearRatio(g, i, numbers) for g in gear]


if __name__ == '__main__':
    data = getData(True)
    # print(solution(data))
    solution2(data)
