from collections import defaultdict
from functools import reduce
from itertools import islice
from operator import iconcat


def getData(test: bool = False):
    fileName = 'input.txt'
    if (test):
        fileName = 'test.txt'
    with open(fileName, 'r') as file:
        return file.read()


def parseData(data: str):
    d = data.split('\n\n')
    d = [x.split(":") for x in d]
    locationsMap = defaultdict(list)
    seeds = list(map(int, d[0][1].strip().split(' ')))
    for m in d[1:]:
        key = m[0].strip().split(' ')[0]
        value = [list(map(int, n.strip().split(' ')))
                 for n in m[1].strip().split('\n')]
        locationsMap[key] = value

    return seeds, locationsMap


def parseData2(data: str):
    d = data.split('\n\n')
    d = [x.split(":") for x in d]
    seeds = list(map(int, d[0][1].strip().split(' ')))
    seeds = [range(a, a+b) for a, b in chunk(seeds, 2)]
    mappings = []
    for m in d[1:]:
        ranges = [[int(x) for x in r.split()]
                  for r in m[1].strip().splitlines()]
        ranges = [(range(a, a+c), range(b, b+c)) for a, b, c in ranges]
        mappings.append(ranges)

    return seeds, mappings


def mapRanges(locationMap: defaultdict):
    d = defaultdict(list)
    for key, value in locationMap.items():
        d[key] = [{'destination': (v[0], v[0]+v[2]-1),
                   'source': (v[1], v[1]+v[2]-1),
                   'range': v[2]
                   } for v in value]

    return d


def marchSeed(seed: int, map: defaultdict):
    position = seed
    for _, v in map.items():
        containedInRange = list(
            filter(lambda m: m['source'][0] <= position <= m['source'][1], v))
        if (containedInRange != []):
            position = containedInRange[0]['destination'][0] + \
                (position-containedInRange[0]['source'][0])
    return position


def solution(seeds: list[int], locationMap: defaultdict) -> int:
    return min([marchSeed(s, locationMap) for s in seeds])


def getMin(r, locationMap, results):
    start, quant = r
    print(start, quant)
    results.append(min([marchSeed(s, locationMap)
                   for s in range(start, start+quant)]))


def chunk(arr: list[int], size: int):
    it = iter(arr)

    return list(iter(lambda: tuple(islice(it, size)), ()))


def flatten(arr):
    return reduce(iconcat, arr, [])


def solution2(seeds, mappings):
    for m in mappings:
        newSeeds = []
        for s in seeds:
            for dest, source in m:
                offset = dest.start - source.start
                if s.stop <= source.start or source.stop <= s.start:
                    continue
                ir = range(max(s.start, source.start),
                           min(s.stop, source.stop))
                lr = range(s.start, ir.start)
                rr = range(ir.stop, s.stop)
                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                newSeeds.append(range(ir.start + offset, ir.stop + offset))
                break
            else:
                newSeeds.append(s)
        seeds = newSeeds

    return min(x.start for x in seeds)


if __name__ == '__main__':
    data = getData()
    seeds, locationMap = parseData(data)
    locationMap = mapRanges(locationMap)
    print(solution(seeds, locationMap))
    # solution 2
    print(solution2(*parseData2(data)))
