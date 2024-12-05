import numpy as np

def isSafe(report):
    differences = np.diff(report)  # Compute differences between adjacent levels
    is_increasing = np.all((differences >= 1) & (differences <= 3))
    is_decreasing = np.all((differences >= -3) & (differences <= -1))
    return is_increasing or is_decreasing

def isSafeDampner(report):
    if isSafe(report):  # Check if already safe
        return True
    # Check if removing one level makes the report safe
    for i in range(len(report)):
        modified_report = np.delete(report, i)  # Remove the ith level
        if isSafe(modified_report):
            return True
    return False

def findSaveReports(data):
    safe_count = sum(isSafe(report) for report in data)
    return safe_count

def findSaveReportsDampner(data):
    safe_count = sum(isSafeDampner(report) for report in data)
    return safe_count

def main():
    with open("dataDay2.txt", "r") as file:
        dataFile = [list(map(int, line.split())) for line in file.readlines()]

    data = np.array(dataFile, dtype=object)
    print("Safe Reports: ", findSaveReports(data))
    print("Safe Reports with Dampner: ", findSaveReportsDampner(data))

if __name__ == "__main__":
    main()