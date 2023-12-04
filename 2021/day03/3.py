from typing import Counter, List, Tuple


def getData(test: bool = False) -> List[Tuple[str, int]]:

    if(test):
        return ['00100',
                '11110',
                '10110',
                '10111',
                '10101',
                '01111',
                '00111',
                '11100',
                '10000',
                '11001',
                '00010',
                '01010']

    with open('input', 'r') as file:
        return list(map(lambda x: x.strip(), file.readlines()))


def getGamma(arr: List[str], string: bool = False) -> int:
    wordLength = len(arr[0])
    gamma = []
    for i in range(wordLength):
        tmp = []
        for word in arr:
            tmp.append(word[i])
        g = Counter(tmp)
        zeros = g['0']
        ones = g['1']
        if(g['1'] == g['0']):
            gamma.append('1')
        else:
            gamma.append('1' if ones > zeros else '0')
    if string:
        return ''.join(gamma)
    return int(''.join(gamma), 2)


def getEpsilon(arr: List[str], string: bool = False) -> int:
    wordLength = len(arr[0])
    epsilon = []
    for i in range(wordLength):
        tmp = []
        for word in arr:
            tmp.append(word[i])
        e = Counter(tmp)
        zeros = e['0']
        ones = e['1']
        if(e['1'] == e['0']):
            epsilon.append('0')
        else:
            epsilon.append('1' if ones < zeros else '0')
    if(string):
        return ''.join(epsilon)
    return int(''.join(epsilon), 2)


def getOxygenGeneratorRating(arr: List[str]) -> int:
    wordLength = len(arr[0])
    tmp = arr
    for i in range(wordLength):
        if(len(tmp) == 1):
            return int(tmp[0], 2)
        gamma = getGamma(tmp, True)
        tmp = list(filter(lambda x: x[i] == gamma[i], tmp))
    return int(tmp[0], 2)


def getCO2ScrubberRating(arr: List[str]) -> int:
    wordLength = len(arr[0])
    tmp = arr
    for i in range(wordLength):
        if(len(tmp) == 1):
            return int(tmp[0], 2)
        epsilon = getEpsilon(tmp, True)
        tmp = list(filter(lambda x: x[i] == epsilon[i], tmp))
    return int(tmp[0], 2)


def main():
    data = getData()
    gamma = getGamma(data)
    epsilon = getEpsilon(data)
    print('* day 3 part 1')
    print(f'- Gamma rate: {gamma}')
    print(f'- Epsilon rate: {epsilon}')
    print(f'- Power consumption: {gamma*epsilon}')
    print('*day 3 part 2')
    oxygen = getOxygenGeneratorRating(data)
    co2 = getCO2ScrubberRating(data)
    print(f'- Oxygen generator rating: {oxygen}')
    print(f'- CO2 scrubber rating: {co2}')
    print(f'- Life support rating: {oxygen*co2}')


if __name__ == '__main__':
    main()
