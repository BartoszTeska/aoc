from ast import parse
from math import prod


def getData(test=False):
    if (test):
        return [
            'Time:      7  15   30',
            'Distance:  9  40  200',
        ]
    with open('input.txt', 'r') as file:
        return file.readlines()


def parseData(data):
    time = [int(x) for x in data[0].split(':')[1].split()]
    distance = [int(x) for x in data[1].split(':')[1].split()]

    return zip(time, distance)


def race(time: int, distance: int):
    ways = 0
    for i in range(time+1):
        remainingTime = time-i
        distanceTravelled = remainingTime*i
        if (distanceTravelled > distance):
            ways += 1
    return ways


def race2(time: int, distance: int):
    start = -1
    end = -1
    for i in range(time+1):
        remainingTime = time-i
        distanceTravelled = remainingTime*i
        if (distanceTravelled > distance):
            start = i
            end = time-i
            break

    return len(range(start, end))


def parseData2(data):
    time = int(''.join([x for x in data[0].split(':')[1].split()]))
    distance = int(''.join([x for x in data[1].split(':')[1].split()]))
    return time, distance


def solution(data):
    return prod([race(*x) for x in data])


def solution2(data):
    return race2(*data)


if __name__ == "__main__":
    data = parseData(getData())
    print(solution(data))
    data = parseData2(getData())
    print(solution2(data))
