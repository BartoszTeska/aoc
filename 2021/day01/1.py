from functools import reduce
from typing import List, Tuple


def getData(test: bool = False) -> List[int]:
    if(test):
        return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    with open('./input', 'r') as file:
        return list(map(int, file.readlines()))


def comparator(x: Tuple[int, int], y: int) -> Tuple[int, int]:
    sum, previous = x
    if(previous == 0):
        return (0, y)
    sum += 1 if y-previous > 0 else 0
    return (sum, y)


def getIncreases(arr: List[int]) -> int:
    return reduce(comparator, arr, (0, 0))[0]


def prepareWindowSum(arr: List[int], windowSize: int) -> List[int]:
    tempArr = []
    for i in range(len(arr)-windowSize+1):
        tempArr.append(arr[i:i+windowSize])
    return list(map(sum, tempArr))


def main():
    # day 1 part 1
    print('* day 1 part 1')
    print(f'- Answer: {getIncreases(getData())}')
    # day 1 part 2
    print('* day 1 part 2')
    print(f'- Answer {getIncreases(prepareWindowSum(getData(), 3))}')


if __name__ == "__main__":
    main()
