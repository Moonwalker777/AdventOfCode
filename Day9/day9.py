from tooling import timingWrapper

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
def moveData(data: str) -> str:
    dataList = list(data)
    while True:
        gapIndex = findGap(dataList)
        if gapIndex == -1:
            # No gaps found, we are done
            break

        rightBlockIndex = findRightmostBlock(dataList)
        if rightBlockIndex == -1:
            # No rightmost block found (all empty?), just break
            break

        # Move the block from rightBlockIndex to gapIndex
        dataList[gapIndex] = dataList[rightBlockIndex]
        dataList[rightBlockIndex] = '.'

    return ''.join(dataList)

def calculateChecksum(data: str) -> int:
    dataList = list(data)
    stippedList = [point for point in dataList if point != '.']
    checksum = 0
    for i, data in enumerate(stippedList):
        checksum += int(data) * i

    return checksum

@timingWrapper.timeit
def blockRepresentation(data: str) -> str:
    file_id = 0
    result = []

    for i, ch in enumerate(data):
        length = int(ch)
        if i % 2 == 0:
            # Even index: file length
            if length > 0:
                result.append(str(file_id) * length)
                file_id += 1
        else:
            # Odd index: free space length
            if length > 0:
                result.append('.' * length)

    return "".join(result)

def main():
    with open("testData.txt", 'r') as file:
        data = file.readline().strip()

    block = blockRepresentation(data)
    print(block)
    defragmentedData = moveData(block)
    print(defragmentedData)
    checkSum = calculateChecksum(defragmentedData)
    print("Checksum is:", checkSum)

if __name__ == "__main__":
    main()

# 0.0000070001
# 0.0000237999