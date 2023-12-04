from functools import reduce
from operator import concat
from typing import List, Optional, Tuple


class Bingo():

    def __init__(self, board: List[List[int]], size: int) -> None:
        self.board = board
        self.boardSize = size
        self.calledNumbers = []

    def checkWin(self) -> Optional[bool]:
        if(len(self.calledNumbers) > 4):
            for i in range(self.boardSize):
                row = [x for x in self.board[i]]
                column = [x for x in [y[i] for y in self.board]]
                if(all([x in self.calledNumbers for x in row])):
                    return True
                if(all([x in self.calledNumbers for x in column])):
                    return True
        return False

    def callNumber(self, number: int) -> None:
        self.calledNumbers.append(number)

    def getResult(self) -> int:
        flatBoard = reduce(concat, self.board)
        return sum([x for x in flatBoard if x not in self.calledNumbers])*self.calledNumbers[-1]


def getData() -> Tuple[List[int], List[Bingo]]:
    with open('input', 'r') as file:
        calledNumbers = list(map(int, file.readline().strip().split(',')))
        bingos = [list(map(int, x.replace('  ', ' ').strip().split(' ')))
                  for x in file.readlines() if x != '\n']
        bingos = [bingos[i:i+5] for i in range(0, len(bingos), 5)]
        bingos = [Bingo(x, 5) for x in bingos]
        return (calledNumbers, bingos,)


def part1():
    calledNumbers, bingos = getData()
    found = False
    # part 1
    for number in calledNumbers:
        for bingo in bingos:
            bingo.callNumber(number)
            check = bingo.checkWin()
            if (check):
                print(f'Result: {bingo.getResult()}')
                found = True
                break
        if(found):
            break


def part2():
    found = False
    calledNumbers, bingos = getData()
    for number in calledNumbers:
        [b.callNumber(number) for b in bingos]
        if(len(bingos) > 1):
            checkedBingos = [b.checkWin() for b in bingos]
            bingos = [b for b in bingos if not checkedBingos[bingos.index(b)]]
        else:
            check = bingos[0].checkWin()
            if(check):
                print(f'Result: {bingos[0].getResult()}')
                found = True
                break
        if(found):
            break


if __name__ == '__main__':
    part1()
    part2()
