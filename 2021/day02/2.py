from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'


class Submarine():

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move(self, direction: str, value: int) -> None:
        if(direction.lower() == Direction.DOWN.value):
            self.down(value)
            return
        if(direction.lower() == Direction.UP.value):
            self.up(value)
            return
        if(direction.lower() == Direction.FORWARD.value):
            self.forward(value)
            return

    def forward(self, value: int) -> None:
        self.x += value

    def up(self, value: int) -> None:
        self.y -= value

    def down(self, value: int) -> None:
        self.y += value

    def result(self) -> int:
        return self.x*self.y


class ImprovedSubmarine(Submarine):
    def __init__(self) -> None:
        super().__init__()
        self.aim = 0

    def forward(self, value: int) -> None:
        self.x += value
        self.y += self.aim*value

    def up(self, value: int) -> None:
        self.aim -= value

    def down(self, value: int) -> None:
        self.aim += value


def getData(test: bool = False) -> List[Tuple[str, int]]:

    if(test):
        return [('forward', 5),
                ('down', 5),
                ('forward', 8),
                ('up', 3),
                ('down', 8),
                ('forward', 2)]

    with open('input', 'r') as file:
        return list(map(parseLine, file.readlines()))


def parseLine(line: str) -> str:
    direction, value = line.strip().split(' ')
    return (direction, int(value))


def main():
    # day2 part1
    submarine = Submarine()
    movement = getData()
    for move in movement:
        submarine.move(move[0], move[1])
    print('* day 2 part 1')
    print(f'- Answer: {submarine.result()}')

    # day2 part2
    submarine = ImprovedSubmarine()
    for move in movement:
        submarine.move(move[0], move[1])
    print('* day 2 part 2')
    print(f'- Answer: {submarine.result()}')


if __name__ == '__main__':
    main()
