def task1():
    import numpy as np

    logs = read_input()
    logs = np.array(logs)

    gamma = ''
    epsilon = ''
    for dim in range(logs.shape[1]):
        curr = logs[:, dim]
        unique, count = np.unique(curr, return_counts=True)
        zipped = dict(zip(unique, count))
        max_bit = max(zipped, key=zipped.get)
        min_bit = min(zipped, key=zipped.get)
        gamma += str(max_bit)
        epsilon += str(min_bit)

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)

    power_consumption = gamma_decimal * epsilon_decimal

    print(f"Solution: {power_consumption}")

def task2():
    commands = read_input()

    depth = 0
    horizontal = 0
    vertical = 0

    for command in commands:
        direction, value = command
        if direction == "forward":
            horizontal += int(value)
            depth += (vertical * int(value))
        elif direction == "down":
            vertical += int(value)
        elif direction == "up":
            vertical -= int(value)
        else:
            raise Exception

    print(f"Solution: {horizontal * depth}")


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        vals = [list(line.strip()) for line in lines]
        vals = [[int(x) for x in sublist] for sublist in vals]
    return vals


if __name__ == "__main__":
    task1()
    task2()