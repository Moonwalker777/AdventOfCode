from functools import wraps
from concurrent.futures import ProcessPoolExecutor
import time
import numpy as np

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function took {total_time:.10f} seconds')
        return result
    return timeit_wrapper

@timeit
def findDistance(list1, list2):
    list1.sort()
    list2.sort()

    distance = [abs(a - b) for a, b in zip(list1, list2)]
    return sum(distance)

@timeit
def findDistanceNP(list1, list2):
    list1 = np.sort(list1)
    list2 = np.sort(list2)

    return np.sum(np.abs(list1 - list2))

@timeit
def similarityScoreNP(list1, list2):
    # Compute the intersection and their counts using NumPy broadcasting
    unique_elements, counts_in_list2 = np.unique(list2, return_counts=True)

    # Find common elements and their counts
    common_elements = np.intersect1d(list1, unique_elements)
    counts_in_common = np.array([counts_in_list2[np.where(unique_elements == num)[0][0]] for num in common_elements])

    similarity = np.sum(common_elements * counts_in_common)
    return similarity


def main():
    list1 = []
    list2 = []
    with open("dataDay1.txt", 'r') as file:
        for line in file:
            if line.strip():  # Ensure the line is not empty
                num1, num2 = map(int, line.split())
                list1.append(num1)
                list2.append(num2)

    print(findDistance(list1, list2))

    data = np.loadtxt("dataDay1.txt", dtype=int)
    list1np, list2np = data[:, 0], data[:, 1]
    print(findDistanceNP(list1np, list2np))

    print(similarityScoreNP(list1np, list2np))

if __name__ == "__main__":
    main()