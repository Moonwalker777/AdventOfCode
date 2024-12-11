from tooling import timingWrapper
from collections import Counter

def splitStone(stone):
    stoneStr = str(stone)
    mid = len(stoneStr) // 2
    left = int(stoneStr[:mid])
    right = int(stoneStr[mid:])
    return [left, right]

def blink(data):
    newCounter = Counter()
    for stone, count in data.items():
        if stone == 0:
            # Rule 1: Replace 0 with 1
            newCounter[1] += count
        elif len(str(stone)) % 2 == 0:
            # Rule 2: Split even-numbered stones to two digits (left and right)
            left, right = splitStone(stone)
            newCounter[left] += count
            newCounter[right] += count
        else:
            # Rule 3: Replace with a new stone by 2024
            newCounter[stone * 2024] += count
    return newCounter

@timingWrapper.timeit
def runBlink(data, times):
    counter = Counter(data)
    for _ in range(times):
        counter  = blink(counter)
    return sum(counter.values())

def main():
    with open("dataDay11.txt", 'r') as file:
        data = list(map(int, file.readline().strip().split()))

    nrStones = runBlink(data, 75)
    print("Number of stones:", nrStones)

if __name__ == '__main__':
    main()