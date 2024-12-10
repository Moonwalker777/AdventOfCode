import numpy as np
from collections import deque

def searchPaths(i: int, j: int, data: np.ndarray, directions: np.ndarray, memo: dict) -> int:
    if (i, j) in memo:
        return memo[(i, j)]

    currentHeight = data[i, j]

    if currentHeight == 9:
        memo[(i, j)] = 1
        return 1

    row, cols = data.shape
    totalPaths = 0
    nextHeight = currentHeight + 1

    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < row and 0 <= ny < cols:
            if data[nx, ny] == nextHeight:
                totalPaths += searchPaths(nx, ny, data, directions, memo)

    memo[(i, j)] = totalPaths
    return totalPaths

def searchPeaks(i: int, j: int, data: np.ndarray, directions: np.ndarray):
    row, col = data.shape

    visited = set()
    reachablePeaks = set()

    queue = deque()
    queue.append((i, j))
    visited.add((i, j))

    while queue:
        x,y = queue.popleft()
        currentHeight = data[x, y]

        if currentHeight == 9:
            reachablePeaks.add((x, y))
            continue

        nextHeight = currentHeight + 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col:
                if data[nx, ny] == nextHeight and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return len(reachablePeaks)

def findPeaksAndPaths(data: np.ndarray) -> int:
    directions = np.array([
        [0, 1],  # right
        [0, -1],  # left
        [1, 0],  # down
        [-1, 0]  # up
    ])

    rows, cols = data.shape
    memo = {}

    totalScore = 0
    totalRating = 0
    for i in range(rows):
        for j in range(cols):
            if data[i,j] == 0:
                score = searchPeaks(i, j, data, directions)
                totalScore += score
                rating = searchPaths(i, j, data, directions, memo)
                totalRating += rating

    return totalScore, totalRating


def main():
    with open("dataDay10.txt", 'r') as file:
            lines = file.read().strip().split('\n')

    digits = [list(map(int, list(line.strip()))) for line in lines]
    data = np.array(digits)
    score, rating = findPeaksAndPaths(data)
    print("Total score:", score)
    print("Total rating:", rating)

if __name__ == "__main__":
    main()