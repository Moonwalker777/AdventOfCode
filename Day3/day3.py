import re

def multiply_results(result):
    """Calculate the sum of products of valid mul pairs."""
    sum_pair = 0
    for pair in result:
        sum_pair += pair[0] * pair[1]
    return sum_pair


def findMatchesPattern(data, enabled = True):
    """Find and process mul patterns based on do() and don't() instructions."""
    pattern = r"mul\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)"
    control_pattern = r"(do\(\)|don't\(\))"

    chunks = re.split(control_pattern, data)
    results = []

    for chunk in chunks:
        if chunk == "do()":
            enabled = True
        elif chunk == "don't()":
            enabled = False
        elif enabled:
            matches = re.findall(pattern, chunk)
            for num1, num2 in matches:
                num1 = float(num1) if '.' in num1 else int(num1)
                num2 = float(num2) if '.' in num2 else int(num2)
                results.append((num1, num2))

    return results

def findMatches(data):
    pattern = r"mul\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)"
    matches = re.findall(pattern, data)
    results = [(float(num1) if '.' in num1 else int(num1), float(num2) if '.' in num2 else int(num2)) for num1, num2 in
               matches]
    return results

def main():
    with open('dataDay3.txt', 'r') as file:
        data = file.read().replace('\n', '')

    result = findMatches(data)
    resultPattern = findMatchesPattern(data)
    print(multiply_results(result))
    print(multiply_results(resultPattern))

if __name__ == "__main__":
    main()
