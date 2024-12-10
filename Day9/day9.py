from tooling import timingWrapper
import bisect

def findRightmostBlock(dataList: list) -> int:
    for i in range(len(dataList)-1, -1, -1):
        if dataList[i] != ".":
            return i
    return -1

def findGap(dataList)-> int:
    lastBlockPosition = findRightmostBlock(dataList)
    if lastBlockPosition == -1:
        return -1

    for i, ch in enumerate(dataList):
        if ch == '.' and i < lastBlockPosition:
            return i
    return -1

@timingWrapper.timeit
def moveData(data: list) -> list:
    dataList = data.copy()

    # Track gaps and blocks
    blocks = [i for i, ch in enumerate(dataList) if ch != "."]
    gaps = [i for i, ch in enumerate(dataList) if ch == "."]

    while blocks and gaps:
        rightmost_block_pos = blocks[-1]

        if gaps[0] >= rightmost_block_pos:
            break

        gap_pos = gaps[0]
        old_block_char = dataList[rightmost_block_pos]
        dataList[gap_pos] = old_block_char
        dataList[rightmost_block_pos] = '.'

        # Update blocks and gaps
        blocks.pop()
        bisect.insort(blocks, gap_pos)

        del gaps[0]
        bisect.insort(gaps, rightmost_block_pos)

    return dataList

from tooling import timingWrapper
import bisect

def findRightmostBlock(dataList: list) -> int:
    for i in range(len(dataList)-1, -1, -1):
        if dataList[i] != ".":
            return i
    return -1

def findGap(dataList)-> int:
    lastBlockPosition = findRightmostBlock(dataList)
    if lastBlockPosition == -1:
        return -1

    for i, ch in enumerate(dataList):
        if ch == '.' and i < lastBlockPosition:
            return i
    return -1

@timingWrapper.timeit
def moveData(data: list) -> list:
    dataList = data.copy()

    # Efficiently track gaps and blocks
    blocks = [i for i, ch in enumerate(dataList) if ch != "."]
    gaps = [i for i, ch in enumerate(dataList) if ch == "."]

    while blocks and gaps:
        rightmost_block_pos = blocks[-1]

        if gaps[0] >= rightmost_block_pos:
            break

        gap_pos = gaps[0]
        old_block_char = dataList[rightmost_block_pos]
        dataList[gap_pos] = old_block_char
        dataList[rightmost_block_pos] = '.'

        # Update blocks and gaps
        blocks.pop()
        bisect.insort(blocks, gap_pos)

        del gaps[0]
        bisect.insort(gaps, rightmost_block_pos)

    return dataList

def calculateChecksum(data: list) -> int:
    checksum = 0
    for i, ch in enumerate(data):
        if ch != '.':
            checksum += int(ch) * i
    return checksum

@timingWrapper.timeit
def blockRepresentation(data: str) -> list:
    remapped = []
    fileID = 0
    for i in range(len(data)):
        for _ in range(int(data[i])):
            remapped.append(str(fileID) if i % 2 == 0 else ".")
        if i % 2 == 0:
            fileID += 1
    return remapped

def main():
    with open("dataDay9.txt", 'r') as file:
        data = file.readline().strip()
    block = blockRepresentation(data)
    defragmentedData = moveData(block)
    checkSum = calculateChecksum(defragmentedData)
    print("Checksum is:", checkSum)

if __name__ == "__main__":
    main()