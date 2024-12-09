from tooling import timingWrapper

@timingWrapper.timeit
def findMiddlepageSum(pages):
    middlePage = []
    for page in pages:
        middleIndex = len(page) // 2
        middlePage.append(page[middleIndex])

    sumMiddlePage = sum(middlePage)
    return sumMiddlePage

def findOccurances(pageorder, printorder):
    for rule in pageorder:
        first, second = rule
        if first in printorder and second in printorder:
            if printorder.index(first) > printorder.index(second):
                return False  # Rule is violated
    return True  # Rule is satisfied


def reorderPages(pageorder, rules):
    # Reorder based on rules
    dependencies = {page: set() for page in rules}
    for rule in pageorder:
        first, second = rule
        if first in dependencies and second in dependencies:
            dependencies[second].add(first)

    # Topological sort
    result = []
    visited = set()

    def visit(page):
        if page in visited:
            return
        visited.add(page)
        for dep in dependencies[page]:
            visit(dep)
        result.append(page)

    for page in rules:
        visit(page)

    # Reverse the result to get the correct order
    result.reverse()
    return result

@timingWrapper.timeit
def reorderIncorrectPages(pageorder, incorretlyOrderedUpdates):
    reorderedUpdates = []
    for rule in incorretlyOrderedUpdates:
        reorderedUpdates.append(reorderPages(pageorder, rule))
    return reorderedUpdates

@timingWrapper.timeit
def checkOrdering(pageOrder, pageUpdate):
    correctlyOrderedUpdates = []
    incorrectlyOrderedUpdates = []
    for printOrder in pageUpdate:
        if findOccurances(pageOrder, printOrder):
            correctlyOrderedUpdates.append(printOrder)
        else:
            incorrectlyOrderedUpdates.append(printOrder)

    return correctlyOrderedUpdates, incorrectlyOrderedUpdates


def readData(filename):
    pageorder = []
    pageupdate = []
    with open(filename, 'r') as file:
        for line in file:
            if "|" in line:
                tuples = tuple(map(int, line.split("|")))
                pageorder.append(tuples)
            elif "," in line:
                lst = list(map(int, line.split(",")))
                pageupdate.append(lst)
    return pageorder, pageupdate

def main():
    pageorder, pageupdate = readData("dataDay5.txt")
    orderedUpatesCorrect, orderedUpatesIncorrect = checkOrdering(pageorder, pageupdate)
    reorderedPages = reorderIncorrectPages(pageorder, orderedUpatesIncorrect)
    middlePageSum = findMiddlepageSum(orderedUpatesCorrect)
    reorderedMiddlePageSum = findMiddlepageSum(reorderedPages)
    print(middlePageSum)
    print(reorderedMiddlePageSum)

if __name__ == "__main__":
    main()