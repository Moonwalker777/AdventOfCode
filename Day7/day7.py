from tooling import timingWrapper

def evalExpression(numbers, ops):
    result = numbers[0]

    for i, op in enumerate(ops):
        if op == "+":
            result = result + numbers[i+1]
        elif op == "*":
            result = result * numbers[i+1]
        elif op == "||":
            result = int(str(result) + str(numbers[i+1]))

    return result

def parser(lines, task1):
    totalSum = 0

    for line in lines:
        parts = line.split(':')
        target = int(parts[0].strip())
        numbers = list(map(int, parts[1].strip().split()))

        if len(numbers) == 1:
            if numbers[0] == target:
                totalSum += target
            continue

        n = len(numbers)
        operators = ['+', '*', '||']

        found = False

        if task1:
            for mask in range(2 ** (n-1)):
                ops = []
                for i in range(n - 1):
                    if (mask & (1 << i) == 0):
                        ops.append("+")
                    else:
                        ops.append("*")

                value = evalExpression(numbers, ops)
                if value == target:
                    found = True
                    break
        else: #Task 2
            from itertools import product
            for ops in product(operators, repeat=n - 1):
                value = evalExpression(numbers, ops)
                if value == target:
                    found = True
                    break

        if found:
            totalSum += target

    return totalSum


def main():
    with open("dataDay7.txt", 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    print(parser(lines, False))

if __name__ == '__main__':
    main()