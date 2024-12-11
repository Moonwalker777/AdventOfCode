def simulateGuardPatrol(mapInput):
    # Parse the input map
    mapGrid = [list(row) for row in mapInput.strip().split("\n")]
    rows, cols = len(mapGrid), len(mapGrid[0])

    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    directionIndex = 0  # Start facing up

    # Find the guard's starting position
    guardPos = None
    for r in range(rows):
        for c in range(cols):
            if mapGrid[r][c] in "^>v<":
                guardPos = (r, c)
                directionIndex = "^>v<".index(mapGrid[r][c])
                break
        if guardPos:
            break

    if not guardPos:
        raise ValueError("Guard's starting position not found in the map.")

    visited = set()
    reachable = set((r, c) for r in range(rows) for c in range(cols) if mapGrid[r][c] != "#")

    while True:
        r, c = guardPos

        # Mark visited position with 'X' if it's not an obstacle
        if mapGrid[r][c] != "#":
            mapGrid[r][c] = 'X'

        # Add to visited positions
        visited.add(guardPos)

        # Calculate the next position
        dr, dc = directions[directionIndex]
        nextR, nextC = r + dr, c + dc

        if not (0 <= nextR < rows and 0 <= nextC < cols):
            # Guard leaves the grid
            print("Guard has left the grid, stopping loop.")
            break

        if mapGrid[nextR][nextC] != "#":
            # Move forward if no obstacle
            guardPos = (nextR, nextC)
        else:
            # Turn right if there is an obstacle
            directionIndex = (directionIndex + 1) % 4

        # Check if all reachable positions are visited
        if visited >= reachable:
            print("All reachable positions visited, stopping loop.")
            break

    # Return the updated map
    return "\n".join("".join(row) for row in mapGrid)

def readInputFromFile(filePath):
    with open(filePath, 'r') as file:
        return file.read()


def main():
    # File path to the input map
    filePath = "dataDay6.txt"
    mapInput = readInputFromFile(filePath)
    result = simulateGuardPatrol(mapInput)
    print(result.count("X"))

if __name__ == "__main__":
    main()