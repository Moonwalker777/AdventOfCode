def findXMAS(data, searchWord, searchWordMAS):
    rows = len(data)
    colums = len(data[0])
    countXMAS = 0
    countMAS = 0
    lenSearchWord = len(searchWord)
    searchWordMASReversed = searchWordMAS[::-1]

    def checkWord(row, col, dr, dc):
        word = ""
        for i in range(lenSearchWord):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < rows and 0 <= c < colums:
                word += data[r][c]
            else:
                return False
        return word == searchWord

    def checkMAS(row, col):
        if 0 <= row - 1 < rows and 0 <= row + 1 < rows and 0 <= col - 1 < colums and 0 <= col + 1 < colums:
            top_left = data[row - 1][col - 1] + data[row][col] + data[row + 1][col + 1]
            bottom_left = data[row + 1][col - 1] + data[row][col] + data[row - 1][col + 1]
            return (top_left == searchWordMAS or top_left == searchWordMASReversed) and \
                   (bottom_left == searchWordMAS or bottom_left == searchWordMASReversed)
        return False

    directions = [
        (0, 1),     # Horizontal right
        (0, -1),    # Horizontal left
        (1, 0),     # Vertical down
        (-1, 0),    # Vertical up
        (1, 1),     # Diagonal down-right
        (1, -1),    # Diagonal down-left
        (-1, 1),    # Diagonal up-right
        (-1, -1)    # Diagonal up-left
    ]

    for row in range(rows):
        for col in range(colums):
            for dr, dc in directions:
                if checkWord(row, col, dr, dc):
                    countXMAS += 1

    for row in range(rows):
        for col in range(colums):
            if checkMAS(row, col):
                countMAS += 1

    return countXMAS, countMAS



def main():
    with open("dataDay4.txt", 'r') as file:
        data = []
        for line in file:
            data.append(line.strip())

    searchWord = "XMAS"
    searchWordMAS = "MAS"
    resultXMAS, resultMAS = findXMAS(data, searchWord, searchWordMAS)
    print("XMAS occurs", resultXMAS, "times.")
    print("MAS-Pattern occurs", resultMAS, "times.")


if __name__ == '__main__':
    main()