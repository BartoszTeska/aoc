from typing import List, Dict


def getData(test: bool = False) -> List[str]:
    if test:
        return [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ]
    with open('input.txt', 'r') as file:
        return file.readlines()


def parseLine(line: str) -> str:
    digitsMap: Dict[str, str] = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    first = getFirst(line, digitsMap)
    last = getLast(line, digitsMap)
    if (last == ''):
        return f'{first}{first}'
    return f'{first}{last}'


def getLast(line: str, digitsMap: Dict[str, str]) -> str:
    buf = []
    for c in line[::-1]:
        buf.insert(0, c)
        if (c.isdigit()):
            return ''.join(c)
        s = ''.join(buf)
        if (len(s) >= 3 and len([key for key in digitsMap.keys() if key in s]) > 0):
            key = [key for key in digitsMap.keys() if key in s][0]
            return digitsMap[key]
    return ''


def getFirst(line: str, digitsMap: Dict[str, str]) -> str:
    buf = ''
    for c in line:
        buf += c
        if (c.isdigit()):
            return c
        if (len(buf) >= 3 and len([key for key in digitsMap.keys() if key in buf]) > 0):
            key = [key for key in digitsMap.keys() if key in buf][0]
            return digitsMap[key]
    return ''


def solution(arr: List[str]) -> int:
    digits = [list(filter(lambda x: x.isdigit(), line)) for line in arr]
    return sum([int(f'{x[0]}{x[-1]}') for x in digits])


def solution2(arr: List[str]) -> int:
    digits = [int(parseLine(x)) for x in arr]
    return sum(digits)


if __name__ == '__main__':
    data = getData()
    print(solution(data))
    print(solution2(data))
