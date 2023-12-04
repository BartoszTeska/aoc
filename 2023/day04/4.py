from functools import reduce
from operator import iconcat


def getData(test: bool = False) -> list[str]:
    if (test):
        return [
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
        ]

    with open('input.txt', 'r') as file:
        return file.readlines()


def parseLine(line: str) -> tuple[set[int], set[int]]:
    wininng, have = line.strip().split(':')[1].strip().split('|')
    wininng = [int(w.strip()) for w in wininng.strip().split() if w]
    have = [int(h.strip()) for h in have.strip().split(' ') if h]

    return (set(wininng), set(have))


def getPoints(winning: set[int], have: set[int]) -> int:
    points = winning.intersection(have)
    if (len(points) == 0):
        return 0
    return pow(2, len(points)-1)


def getNumberOfMatching(winning: set[int], have: set[int]) -> int:
    return len(winning.intersection(have))


def solution(lines: list[str]) -> int:
    l = [parseLine(line) for line in lines]
    return sum([getPoints(*s) for s in l])


def solution2(lines: list[str]) -> int:
    cards = [parseLine(line)for line in lines]
    c = [[x] for x in range(len(cards))]
    ans = 0
    while (not all([x == [] for x in c])):
        c1 = []
        for i in [it for r in c for it in r]:
            c1.append(
                [j for j in range(i+1, i+getNumberOfMatching(*cards[i])+1)])
        ans += len(c1)
        c = [*c1]
    return ans


if __name__ == '__main__':
    data = getData()
    print(solution(data))
    print(solution2(data))
